--[[Copyright 2018-2022, Wypasek Data Science, Inc.  (WDataSci, WDS)
--Released under the MIT open source license.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
--]]

--[[-- A base module for the WDS-Lua libraries, developed for use by Wypasek Data Science, Inc., but released under the MIT open source license.

<p>Links</p>
<ul>
<li><a href="https://wypasekdatascience.com">Wypasek Data Science</a></li>
<li><a href="https://github.com/wdatasci/WDS-ModelSpec/tree/master/WDS-Lua">WDS-Lua github</a></li>
</ul>

<p>For the WDS-Lua library, WDS.lua is the primary module interface.  It provides
for several common treatments across languages, and some general utility functions.</p>


<p>Usage example:</p>
<ul>
<li><font size="1">Assuming parent directory of WDS.lua and the WDS directory tree is within the LUA_PATH variable, i.e., LUA_PATH contains WDS-Lua/?.lua:</font>
<code><br>
-- By including the following at the top of a CLI session:<br>
        wds=require("WDS")<br>
-- One can use:<br>
        help()  --i.e., to display help for all modules if exists
-- or <br>
        help(module_name)         --i.e., help(wds)<br>
-- To display the info object of module_name, which was built during the definition <br>
-- of module_name via a decorator as used below.<br>
</code>
</li>
</ul>

<p>Conventions used in the WDS-Lua libraries:</p>
<ul>
<li>Within the module definitions, new free names are placed directly into the returned environment. See <i>EnvExtension</i> use at the top of sub-modules for usage.</li>
<li>Several conventions and globalized functions will be familiar to python and R users:
    <ul>
    <li>Hidden Field Names start and end with "__", i.e., "__AAA__". Of course, these names are not actually hidden but intended for internal class purposes.</li>
    <li>Boolean test functions usually start with "bIs", such as "bIsMain" for use in testing a module.</li>
    <li>Sub module/directories will have a common __init__.lua file. The base module, WDS.lua, modifies the search path so that require("WDS.Util") will load WDS/Util/__init__.lua (of course, if WDS/Util.lua does not exist). The exception is the WDS.lua module which defines this behavior and so there is no WDS/__init__.lua file.
    <li>Familiar functions implemented and globalized for the CLI:
        <ul>
            <li>help( obj ) - returns obj.info.doc, if it exists (see AddToModuleHelp), or calls os.execute("ldoc -m "..obj)</li>
            <li>dir( obj ) - calls print(wds.show_keys(obj))</li>
            <li>show( obj ) - calls print(wds.show(obj))</li>
            <li>q() - calls os.exit() (as in R)</li>
        </ul>
    </li>
</li>
<li>The help(module) CLI functionality is based first on an info table in module environment. A module's info table is initialized at the top with inserted information via an <i>AddToModuleHelp</i> decorator. See WDS.lua and submodules for examples.
</li>
<li>The <i>AddToModuleHelp</i> decorator gobbles (an old TeX term) a table that contains at least one key-value pair for object name and doc string.  The doc string can contain luadoc information which will be stripped, see the WDS.lua source.
</li>
</ul>

@module WDS
@copyright 2018-2022
@license MIT
@author Christian Wypasek, Wypasek Data Science, Inc.

--]]--

-- the localizing of arg below shorts the global arg of a program that might require this module
local arg 

local module_name_dots=( ... or "main-call-without-args" )
-- to hard-code use.......
local module_name="WDS"

local dbg
local module_path=""
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
    dbg=require("debugger")
    dbg.auto_where=2
else
    dbg=function() end
end

--[[
For localizing the module environment:
  using _M for module-specific placements with _M as the return table
  using a local _G for the global environment and direct placements
  to avoid copying the usuals from _G into _M, the metafunction __index pulls from _G as needed
  new values are placed directly into _M (and kept from _G) via _M's __newindex metafunction
--]]

local _M={}
local _G=_G
-- __env_extension__ is added to module help later in this file....
local __env_extension__=function(env,base)
    return _G.setmetatable(env,{
        __index=function(self,k) 
            if _G.rawget(self,k)~=nil then 
                return _G.rawget(self,k) 
            else 
                return _G.rawget(base,k)
            end 
        end
        , __newindex=function(self,k,v) _G.rawset(env,k,v) end
    })
end
_ENV=__env_extension__(_M,_G)


--[[
This is a simplified way of providing an info element which the help function
can be used to query.
--]]

info={name=module_name
    ,path=module_path
    ,doc=module_name .. " ("..module_path..")\n"..[==[
    A general set of utilities to add the usual suspects to programs 
    and the interactive session.

    For example, for a WDS lua module:
        wds=require("WDS")
        wds.help(wds)  -- will show this wds.info.doc string
        wds.dir(x)     -- will return the variables in namespace x
        wds.dir() or wds.dir(_G)    -- will return the variables in the global namespace
        wds.show(x)    -- will simple-print an array or table
        wds.show(wds.dir(_G)) -- will print the list in the global namespace

    Globals added:
        help( obj ) - returns obj.info.doc
        dir( obj ) - calls print(wds.show_keys(obj,1))
        show( obj ) - calls print(wds.show(obj,1))
        q() - calls os.exit() (as in R)

    ]==]
    , docmap={}
    , _ENV=_M
}


--[[
For the AddToModuleHelp decorator, it is a function which returns a table with a specialized
".." metaoperation which updates the an info table while passing through the argument.
--]]

__AddToModuleHelp__luadocstrip__=function(infoblock)
    local k,v
    for k,v in pairs(infoblock) do
        if type(v)=="string" and string.find(v,"^%-%-%[%[%-%-(.*)%-%-%]%]%-%-") then
            v=string.sub(v,7,#v-6)
            v=string.gsub(v,"<br>\n","\n")
            infoblock[k]=v
        end
    end
    return infoblock
end

__AddToModuleHelp=function(infoblock)
    local usuals={_ENV=1, name=1, path=1, doc=1, ldoc=1, info=1}
    __AddToModuleHelp__luadocstrip__(infoblock)
    local k,v
    for k,v in pairs(infoblock) do
        if (not usuals[k]) and type(v)=="string" then
            infoblock.name=k
            infoblock.doc=v
            break
        end -- if not usuals
    end -- k,v
    return setmetatable({},{__concat=
    function(tmp,obj,obj2)
        infoblock.info.docmap[infoblock.name]={name=infoblock.name,doc=infoblock.doc,obj=obj}
        if infoblock._ENV then
            infoblock._ENV[infoblock.name]=obj
        end
        if obj2~=nil then
            return obj,obj2
        else
            return obj
        end
    end})
end


AddToModuleHelp=__AddToModuleHelp{
    AddToModuleHelp=[==[--[[--
            A decorator for adding entries to a module's info.docmap table.
--]]--]==]
-- @function AddToModuleHelp
, info=info} ..
__AddToModuleHelp


EnvExtension=AddToModuleHelp{
    EnvExtension=[==[--[[--
            A environment customizer for use at the top of modules.

                General usage:<br>
                    --top of module<br>
                    local wds=require("WDS")<br>
                    local _M={}<br>
                    local _G=_G<br>
                    _ENV=wds.EnvExtension(_M,_G)<br>
                    <<< module body >>><br>
                    return _M<br>
                    --or 
                    return wds.EnvLock(_M)
--]]--]==]
-- @function EnvExtension
, info=info} ..
__env_extension__

EnvLock=AddToModuleHelp{
    EnvLock=[==[--[[--
            A environment locker for use at the return of modules.

                General usage:<br>
                    --top of module<br>
                    <<< module body >>><br>
                    return EnvLock(_ENV)<br>

--]]--]==]
-- @function EnvLock
, info=info} ..
function(env) return setmetatable({},{__index=env,__newindex=function(t,k,v) error("Error, cannot change locked table") end
    ,__metatable=false
}) end


__indent_newlines=function(arg,indent)
    return indent..string.gsub(arg,"\n","\n"..indent)
end
__ldoc_m=function(arg)
    local tmp=io.popen("LUA_INIT=;ldoc -m "..arg.." 2>&1")
    local rv=tmp:read("*all")
    rc=tmp:close();
    return rc,"ldoc -m "..arg.."\n"..__indent_newlines(rv,"      ")
end


help=
function(obj,...)
    local arg=table.pack(...)
    local rv=""
    local found=false
    if type(obj)=="table" then
        local obj_info=rawget(obj,"info")
        if obj_info then
            local obj_info_doc=rawget(obj_info,"doc")
            if obj_info_doc then
                local obj_info_docmap=rawget(obj_info,"docmap")
                if obj_info_docmap then
                    found=true
                    rv=rv.."\n  Module with docmap: " .. obj_info.name .. "\n  " .. obj_info.doc
                    rv=rv.."\n    DocMap:"
                    for a,b in pairs(obj_info_docmap) do
                        rv=rv.."\n         " .. b.name .. ": " .. b.doc
                    end
                elseif obj_info_doc then
                    found=true
                    rv=rv.."\n    " .. obj_info.name .. ": " .. obj_info.doc
                end
            end
        end
    end
    if type(obj)=="string" then
        local a,b=__ldoc_m(obj)
        if a then return b end
    end
    if found or (#arg>0 and arg[1].quiet~=nil) then
        return rv
    end
    if getmetatable(obj) then
        local objmt=getmetatable(obj)
        if objmt.info==nil or objmt.info.doc==nil then
            rv="help (a .info or .info.doc string) not avialable"
        elseif objmt.info and objmt.info.doc then
            rv= objmt.info.doc
            if objmt.info.docmap then
                rv=rv .. "\n  DocMap Table"
                for k,v in pairs(objmt.info.docmap) do
                    rv=rv .. "\n    " .. v.name .. " - " .. v.doc
                end
            end
        else 
            rv="help (.info.doc string) not avialable"
        end
    elseif type(obj) ~= "table" then
        rv="help not available for a non-table"
    elseif ( obj.info == nil or obj.info.doc == nil ) then
        rv="help (a .info or .info.doc string) not avialable"
    else 
        rv=obj.info.doc
        if obj.info.docmap then
            rv=rv .. "\n  DocMap Table"
            for k,v in pairs(obj.info.docmap) do
                rv=rv .. "\n    " .. v.name .. " - " .. v.doc
            end
        end
    end
    return rv
end

--[[-- A global help function.

            help(module) will display a module.info.doc if exists<br>
            help(string_arg) will attempt to call "ldoc -m "..string_arg<br>

            @function help
--]]--
_G.help=
function (obj)
    local k,v,rv,a,b
    if obj==nil then
        print("Global help")
        for k,v in pairs(_G) do
            if type(v)=="table" and v.info then
                print("WDS help for "..k)
                print(help(v,{quiet=true}))
            else
                a,b=__ldoc_m(k)
                if a then
                    print(b)
                end
            end
        end
        if rv=="Global help" then
            rv="Global help\n  help .info.doc strings not found"
        end
        return
    end
    if type(obj)=="string" then
        a,b=__ldoc_m(obj)
        if a then return b end
        obj=_G[obj]
    end
    return help(obj)
end


dir=AddToModuleHelp{
    dir=[==[--[[--
            A python-like dir() function to show table keys.
--]]--]==]
-- @function dir
,info=info } ..
function (obj) 
    if obj == nil then
        obj=_G
    end
    local rv={}
    local i=0
    for k, f in pairs(obj) do
        i=i+1
        rv[i]=k
    end
    return rv
end

local __show__
__show__=
function (obj,opts,ldepth)
    opts=opts or {}
    opts.maxdepth=opts.maxdepth or 10
    opts.depth=opts.depth or 1
    ldepth=ldepth or opts.depth
    opts.hidden=opts.hidden or false
    opts.indent=opts.indent or ""
    local depth,indent,hidden
    depth=ldepth or opts.depth
    hidden=opts.hidden
    if type(obj) ~= "table" then
        return {__depth__=depth,__type__=type(obj),k=nil,v=tostring(obj)}
    end
    local i,j,k,f,rv
    rv={__depth__=depth,__type__="table"}
    local hiddenfields={}
    for k,f in pairs(obj) do
        if bIsHiddenFieldName(k) then
            if hidden then
                if bIn(type(f),"string","number","function","boolean") then
                    table.insert(rv,{__type__="hidden",k=k,v=tostring(f)})
                else
                    table.insert(rv,{__type__="hidden",k=k,v=k})
                end
            else
                -- continue
            end
        else
            if type(f)=="function" then
                table.insert(rv,{__type__="function",k=k,v=tostring(f)})
            elseif type(f)=="table" then
                if depth and depth<=opts.maxdepth then
                    local lrv=__show__(f,opts,ldepth+1)
                    table.insert(rv,{__type__="table",k=k,v=lrv})
                else
                    table.insert(rv,{__type__="depthexceedtable",k=k,v="<<show depth exceeded>>"})
                end
            else    
                table.insert(rv,{__type__=type(f),k=k,v=tostring(f)})
            end
        end
    end
    if hidden then
        local mt=getmetatable(obj)
        if mt~=nil then
            table.insert(rv,{__depth__=1,__type__="metatable",k="metatable",v=tostring(mt)})
        end
    end
    return rv
end

local __show_str__
__show_str__=function(arg,opts,ldepth)
    ldepth=ldepth or opts.depth or 0
    local maxdepth=opts.maxdepth or 10
    if ldepth>maxdepth then
        ldepth=maxdepth
    end
    local linesep=opts.linesep or " "
    local itemsep=opts.itemsep or ","
    local indent=opts.indent or " "
    local lindent=string.rep(indent,ldepth)
    local b,i,j,k,v
    if arg.__type__~="table" then
        return arg.v
    end
    local rv={}
    for i,b in ipairs(arg) do
        local s=""
        if b.k~=nil then
            s=s.."["..b.k.."]="
        end
        if b.__type__~="table" then
            s=s..b.v
        else
            s=s..__show_str__(b.v,opts,ldepth+1)
        end
        table.insert(rv,s)
    end
    return "{"..linesep..lindent..table.concat(rv,itemsep..linesep..lindent)..linesep..lindent.."}"
end


local __show
__show=
function (obj,opts,depth)
    depth=depth or 1
    opts=opts or {}
    opts.maxdepth=opts.maxdepth or 10
    opts.depth=opts.depth or depth
    opts.hidden=opts.hidden or false
    opts.indent=opts.indent or ""
    opts.itemsep=opts.itemsep or ","
    opts.linesep=opts.linesep or " "
    opts.sep=opts.sep or ", "
    local lrv=__show__(obj,opts)
    return __show_str__(lrv,opts)
end

show=AddToModuleHelp{
        show=[==[--[[--
            A simple table dump to string
--]]--]==]
-- @function show
, info=info} ..
__show

_G.show_str=show
_G.show=function(obj,opts,ldepth) print(show(obj,opts,ldepth)) end

show_values=
AddToModuleHelp{
        show_values=[==[A simple print of just a table's values.]==]
    , info=info} ..
function (obj)
    local rv=""
    local i=0
    for k,f in pairs(obj) do
        i=i+1
        if i>1 then 
            rv=rv .. ", "
        end
        if type(f)=="function" then
            rv=rv .. k.."="..tostring(f)
        elseif type(f)=="table" then
            rv=rv .. k.."="..tostring(f)
        else    
            rv=rv .. tostring(f)
        end
    end
    return rv
end

keys=AddToModuleHelp{
    keys=[==[--[[--
            A simple function to pull a table's keys into a indexed table.
--]]--]==] 
-- @function keys
, info=info} ..
function (obj,opts)
    if type(obj) ~= "table" then
        return nil
    end
    opts=opts or {}
    local tosort = opts.sort or false
    local rv={}
    for k,f in pairs(obj) do
        table.insert(rv,k)
    end
    if tosort then
        table.sort(rv, function (a,b) return tostring(a)<tostring(b) end)
    end
    return rv
end

show_keys=AddToModuleHelp{
    show_keys=[==[--[[--
            As simple function that returns a string of a table's keys.
--]]--]==]
-- @function show_keys
, info=info} ..
function (obj, opts)
    if type(obj) ~= "table" then
        return ""
    end
    opts=opts or {sort=false,sep=", "}
    local lsep=opts.sep or ", "
    if opts.newlinesep then
        lsep="\n"
    end
    local lkeys=keys(obj,opts)
    return table.concat(lkeys,lsep)
end

--- A global dir() function.
-- @function _G.dir
_G.dir=
function (obj,opts) 
    opts=opts or {}
    opts.sort=opts.sort or true
    if obj ~= nil then
        print(show_keys(obj,opts))
    else
        print(show_keys(_G,opts))
    end
    return
end

locals=AddToModuleHelp{
    locals=[==[--[[--
            A simple query of the locals available (uses debug library).
--]]--]==]
-- @function locals
, info=info} ..
function ()
    local rv={}
    local i=0
    while true do
        i=i+1
        local k, v = debug.getlocal(2,i)
        if not k then break end
        rv[k]=v
    end
    return rv
end

-- semi-standard dump example
do
    local seen={}
    local function local_dump(t, indentation)
        indentation=(indentation or "")
        seen[t]=true
        local s={}
        local n=0
        for k in pairs(t) do
            n=n+1
            s[n]=k
            -- print(n,k)
        end
        -- table.sort(s)
        local ok, msg = pcall(function () table.sort(s) end)
        for k,v in ipairs(s) do
            print(indentation,v)
            v=t[v]
            if type(v)=="table" and not seen[v] then
                local_dump(v,indentation.."\t")
            else
                print(indentation.."\t",v)
            end
        end
    end
    _M.dump=local_dump
end

StringUnquote=
AddToModuleHelp{
    StringUnquote=[==[--[[--
            Returns a string without surrounding quotes.
--]]--]==]
-- @function StringUnquote
, info=info} ..
function(arg)
    if type(arg)~="string" then
        return tostring(arg)
    elseif string.sub(arg,1,1)=="\"" and string.sub(arg,#arg,#arg)=="\"" then
        return string.sub(arg,2,#arg-1)
    else
        return arg
    end
end


StringExportable=
AddToModuleHelp{
    StringExportable=[==[--[[--
            A simple function to return a string for serialization purposes.
--]]--]==]
-- @function StringExportable
, info=info} ..
function(word,keyquote)
    local rv=string.format("%q",word)
    rv=string.sub(rv,2,#rv-1)
    local rv_needs_to_be_quoted=false --quote_string 
    if rv_needs_to_be_quoted==false and string.find(rv,"[^%w_]") then
        rv_needs_to_be_quoted=true
    end
    if rv_needs_to_be_quoted==false and string.find(rv,"%d") and string.find(rv,"%D") then
        rv_needs_to_be_quoted=true
    end
    local qrv=rv
    if rv_needs_to_be_quoted then
        if keyquote then
            qrv='["'..rv..'"]'
        else
            qrv='"'..rv..'"'
        end
    else
    end
    return rv, qrv
end

-- using the semi-standard dump example to create an lson
do
    local local_lson
    local_lson=function(obj,opts)
        opts=opts or {}
        local indent=opts.indent or ""
        local name1, qname, kname
        local t1,qt
        if opts.name then
            name1,qname=StringExportable(opts.name,true)
            name1=qname
            qname=qname.." ="
        else
            name1=""
            qname=""
        end
        if opts.kname then
            t1,kname=StringExportable(opts.kname,true)
            kname=kname.." = "
        else 
            kname=""
        end
        if obj == nil then
            return qname..indent..kname.."{__nil__=true}"
        elseif type(obj)=="string" then
            t1,qt=StringExportable(obj)
            return qname..indent..kname.."[["..t1.."]]"
        elseif type(obj)=="boolean" or type(obj)=="number" then
            return qname..indent..kname..tostring(obj)
        elseif type(obj)=="function" then
            return qname..indent..kname.."[["..string.dump(obj).."]]"
        elseif type(obj)=="userdata" or type(obj)=="thread" then
            return qname..indent..kname.."[[cannot be serialized, "..type(obj).."]]"
        end
        local rvs=qname..indent..kname.."{\n"

        local i,k,v
        local seen={}
        local bSep=false
        local n=rawlen(obj)
        for i=1,n,1 do
            v=rawget(obj,i)
            if bSep then rvs=rvs..",\n" end
            seen[i]=i
            rvs=rvs..local_lson(v,{indent=indent.."   "})
            bSep=true
        end
        i=next(obj)
        while i do
            if seen[i]==nil then
                seen[i]=i
                v=rawget(obj,i)
                if bSep then rvs=rvs..",\n" end
                rvs=rvs..local_lson(v,{indent=indent.."   ",kname=i})
                bSep=true
            end
            i=next(obj,i)
        end
        if opts.includereturn then
            if opts.name then
                return rvs.."}\nreturn "..name1.."\n"
            else
                return "return "..rvs.."}\n"
            end
        else
            return rvs.."}\n"
        end
    end
    _M.lson=local_lson
end
_G.lson=_M.lson

rtrim=AddToModuleHelp{
    rtrim=[==[--[[--
            A simple string right trim function.
--]]--]==]
-- @function rtrim
, info=info } .. 
function(arg,to_be_removed)
    to_be_removed=to_be_removed or "([%s%c\a\b\f\n\r\t\v]*)"
    local a
    a = string.find(arg,to_be_removed.."$")
    if a then
        return string.sub(arg,1,a-1)
    else
        return arg
    end
end

ltrim=AddToModuleHelp{
    rtrim=[==[--[[--
            A simple string left trim function.
--]]--]==]
-- @function ltrim
, info=info } .. 
function(arg,to_be_removed)
    to_be_removed=to_be_removed or "([%s%c\a\b\f\n\r\t\v]*)"
    local a
    local b
    a, b = string.find(arg,"^"..to_be_removed)
    if a then
        return string.sub(arg,b+1)
    else
        return arg
    end
end

trim=AddToModuleHelp{
    trim=[==[--[[--
            A simple string trim function.
--]]--]==]
-- @function trim
, info=info } .. 
function(arg,to_be_removed)
    to_be_removed=to_be_removed or "([%s%c\a\b\f\n\r\t\v]*)"
    local a
    local b
    local c
    a, b = string.find(arg,"^"..to_be_removed)
    if a then
        c = string.find(arg,to_be_removed.."$",b+1)
        if c then
            return string.sub(arg,b+1,c-1)
        else 
            return string.sub(arg,b+1)
        end
    else
        c = string.find(arg,to_be_removed.."$")
        if c then
            return string.sub(arg,1,c-1)
        else 
            return arg
        end
    end
end

string_startswith_exp=AddToModuleHelp{
    string_startswith_exp=[==[--[[--
            A simple boolean test if a string starts with a match pattern.
--]]--]==]
-- @function string_startswith_exp
, info=info} ..
function (arg1,arg2)
    i,j=string.find(arg1,"^"..arg2) 
    return i and i==1
end

string_startswith=AddToModuleHelp{
    string_startswith=[==[--[[--
            A simple boolean test if a string starts with another string.
--]]--]==]
-- @function string_startswith
, info=info} ..
function (arg1,arg2)
    if type(arg1)~="string" then
        arg1=tostring(arg1)
    end
    if type(arg2)~="string" then
        arg2=tostring(arg2)
    end
    -- check for magic characters which will need to be escaped
    local i,j=string.find(arg2,"[%(%_%.%%%+%-%*%?%[%]%^%$]") 
    if i then
        arg2=string.gsub(arg2,"[%(%_%.%%%+%-%*%?%[%]%^%$]","%%%1") 
    end
    return string_startswith_exp(arg1,arg2)
end

string_split=AddToModuleHelp{
    string_split=[==[--[[--
            A simple string split.
--]]--]==]
-- @function string_split
, info=info} ..
function (s,dlm,quoted,trimit)
    if dlm==nil then
        dlm=" "
    end
    local rv={}
    -- for the pattern "(.-)"..dlm 
    --  . finds any character
    --  .- finds 0 or more characters, but the smallest matching string
    --  (.-) captures 0 or more characters, but the smallest matching string
    --  "(.-)"..dlm finds 0 or more characters, but the smallest matching
    --      string which is followed by the dlm string
    --  Note that the dlm string is not captured, so it does not have to 
    --  be removed, but a trailing dlm does need to be added to capture
    --  the tail.
    local _s
    if trimit then
        _s=string.gsub(s,"^%s*(.-)%s*$","%1")..dlm
        if quoted then
            _s=dlm.._s
        end
    else
        _s=s..dlm
        if quoted then
            _s=dlm.._s
        end
    end
    if quoted then
        local starti=1
        local stop=false
        while not stop do
            local a,b,c,d=string.find(_s,"^"..dlm.."%s-([\"'])(.-)%1%s-"..dlm,starti)
            if a~=nil then
                if d==nil or #d==0 then
                    table.insert(rv,"")
                else
                    table.insert(rv,d)
                end
                starti=b-#dlm+1
                stop=(b==#_s)
            else
                a,b,c=string.find(_s,"^"..dlm.."(.-)"..dlm,starti)
                if a~=nil then
                    if c==nil or #c==0 then
                        table.insert(rv,"")
                    else
                        table.insert(rv,c)
                    end
                    starti=b-#dlm+1
                    stop=(b==#_s)
                else
                    stop=true
                end
            end
        end
    else
        for _seg in string.gmatch(_s,"(.-)"..dlm) do
            table.insert(rv,_seg)
        end
    end
    return rv
end

-- For the WDS.lua module, in a location with a WDS subdirectory,
-- check to see if python-esc module __init__.lua files can be found on paths
-- with /WDS/ or :\WDS\ 

if string.find(package.path,"%?.__init__.lua") == nil then
    local s=""
    for k,v in pairs(string_split(package.path,";")) do
        if ( string.find(v,"WDS(.-)%?%.lua$") ~= nil ) 
            and ( string.find(v,"%?.%?") == nil ) then
            if string.find(v,":\\") == nil then
                s= s .. ";" .. string.match(v,"(.-)%?%.lua$") .. "?/__init__.lua"
            else
                s= s .. ";" .. string.match(v,"(.-)%?%.lua$") .. "?\\__init__.lua"
            end
        end
    end
    if s~="" then
        package.path=package.path..s
        -- print("updated lua search path ",package.path)
    end
end


-- bIsMain, if called in the ``main'' function includes arg[-1]=lua<<version>>
bIsMain=AddToModuleHelp{
    bIsMain=[==[--[[--
            A boolean for tests in module files, usage wds.bIsMain(table.pack(...),modulename).
--]]--]==]
-- @function bIsMain
, info=info} ..
function(args,module_name)
    if module_name and args[0] then
        return (string.find(args[0],module_name..".lua")~=nil)
    end
    return ( args and ( 
            ( args[0] and args[-1] and string_startswith_exp(args[-1],"lua[56]%.") )
            or args[1]=="--main" )
            )
end
    
q=AddToModuleHelp{
    q=[==[--[[--
            An R-like q() function to exit.  Added to globals.
--]]--]==]
-- @function q
, info=info} ..
    function()
    os.exit()
end

--- A global R-like q() function to exit.
-- @function _G.q
_G.q=q

bIn=AddToModuleHelp{
    bIn=[==[--[[--
            An SQL-like in() function, but use as bIn(arg, a1, a2, ..., an) for 'arg in(a1, a2, ..., an)'.
--]]--]==]
-- @function bIn
, info=info} ..
    function(a,...)
    local arg=table.pack(...)
    for i,v in ipairs(arg) do
        if a==v then
            return true
        end
    end
    return false
end

bIsHiddenFieldName=AddToModuleHelp{
    bIsHiddenFieldName=[==[--[[--
            A boolean check for python-like fields expected to be hidden, i.e, __AAA__.
--]]--]==]
-- @function bIsHiddenFieldName
, info=info } ..
function(arg)
    if type(arg)~="string" then 
        return false 
    elseif string.find(arg,"^__(.*)__$")~=nil then 
        return true
    elseif bIn(string.lower(arg),"pass","password","passwd") then
        return true
    else
        return false;
    end
end

local local_table_simple_value_comp
local_table_simple_value_comp=function(a,b)
    if #a==nil or #b==nil then
        return false
    end
    if #a ~= #b then
        return false
    end
    local na=0
    local nb=0
    for i,v in pairs(b) do
        nb=nb+1
    end
    for i,v in pairs(a) do
        local tai=type(a[i])
        na=na+1
        if b[i] then
            if type(b[i])~=tai then
                return false
            elseif bIn(tai,"string","boolean","number") then
                if a[i]~=b[i] then
                    return false
                end
            elseif tai=="table" then
                if ~local_table_simple_value_comp(a[i],b[i]) then
                    return false
                end
            else
                return false
            end
        else
            return false
        end
    end
    return true
end

table_simple_value_comp=AddToModuleHelp{
    table_simple_value_comp=[==[--[[--
            A not-too-deep comp of two tables.
--]]--]==]
-- @function table_simple_value_comp
, info=info} ..
local_table_simple_value_comp

simple_copy=AddToModuleHelp{
    table_simple_copy=[==[--[[--
            A not-too-deep copy of an object.
--]]--]==]
-- @function simple_copy
, info=info} ..
function(obj)
    if bIn(type(obj),"string","number") then
        local rv=obj
        return rv
    elseif type(obj)=="table" then
        local rv={}
        for k,v in pairs(obj) do
            rv[k]=v
        end
        return rv
    else
        error("simple copy for object of type, "..type(obj)..", not implemented")
    end
end

local __deeper_copy__
__deeper_copy__=function(obj,opts,lopts)

    opts=opts or {}
    opts.depth=(opts.depth or 0) +1
    opts.special_handling=opts.special_handling or {}
    if opts.special_handling.__parent__==nil then
        opts.special_handling.__parent__=true
    end
    lopts=lopts or {}

    local tobj=type(obj)
    local rv
    if tobj~="table" then
        rv=obj
        return rv
    end
    local obj___copy__=obj.__copy__
    if obj___copy__~=nil then
        if type(obj___copy__)=="function" then
        rv=obj___copy__()
    else
        rv=obj___copy__
    end
        return rv
    else
        rv={}
        local seen={}
        local i,k,v
        local n=rawlen(obj)
        for i=1,n,1 do
            v=rawget(obj,i)
            seen[i]=i
            rv[i]=__deeper_copy__(v,opts,{__parent__=rv})
        end
        i=next(obj)
        while i do
            if seen[i]==nil then
                seen[i]=i
                v=rawget(obj,i)
                if opts.special_handling[i]==nil then
                    rv[i]=__deeper_copy__(v,opts,{__parent__=rv})
                else
                    if i=="__parent__" then
                        rv[i]=lopts.__parent__
                    else
                        error("Error __deeper_copy__: other special_handling instruction for "..i.." not added.")
                    end
                end
            end
            i=next(obj,i)
        end
        return setmetatable(rv,getmetatable(obj))
    end
end

deeper_copy=AddToModuleHelp{
    deeper_copy=[==[--[[--
                A deeper copy of an object (metatables, userdata, and threads are pointed to for class and reference purposes).
                    Notes:
                        - the hidden field name, __parent__, will point to newly created logical parents
--]]--]==]
-- @function deeper_copy
, info=info} ..
function(obj)
    return __deeper_copy__(obj)
end

nilable_instance_of=function(obj,extension_methods)
    local __mt=getmetatable(obj) or {}
    local __extension_methods=extension_methods or {}
    local __index
    local __newindex
    __index=function(t,k) 
        if __mt[k] then
            return obj[k]
        elseif k=="new" then
            do
                local rv={}
                for i,v in pairs(obj) do
                    rv[i]=v
                end
                return setmetatable(rv,{__index=__index,__newindex=__newindex})
            end
        elseif k=="__class__" then
            return obj
        elseif rawget(t,k) then 
            return rawget(t,k) 
        elseif obj[k] then 
            rawset(t,k,obj[k]) 
            return rawget(t,k) 
        elseif extension_methods and extension_methods[k] then
            return extension_methods[k]
        else 
            error(k.."  is not a valid key") 
        end 
    end
    __newindex=function(t,k,v) 
        if v==nil and obj[k] then 
            rawset(t,k,{__nil__=true}) 
        elseif obj[k] then 
            rawset(t,k,v) 
        else 
            error(k.." is not a valid key") 
        end 
    end
    return setmetatable({__proto=obj},{__index=__index,__newindex=__newindex})
end

length=AddToModuleHelp{
    length=[==[--[[--
            A length function to count pairs of a table (since # does not work that way...).

                    By default, the first returned value does not include hidden field names (i.e., __AAA__).<br>
                    Returns N,N1,N2,NH,N2Fields,NHFields <br>
                        where N=#pairs, N1=#arg, N2=N-N1, NH=#hidden, and N[2H]Fields is a list of N[2H] field names.<br>
--]]--]==]
-- @function length
, info=info} ..
function(obj)
    if type(obj)~="table" then
        return 1
    end
    local k,v
    local n=0
    local n1=rawlen(obj)
    local n2=0
    local nh=0
    local n2fields={}
    local nhfields={}
    for k,v in pairs(obj) do
        if bIsHiddenFieldName(k) then
            nh=nh+1
            nhfields[k]=k
        elseif type(k)=="number" and 1<=k and k<=n1 then
            -- continue
        else
            n2=n2+1
            n2fields[k]=k
        end
    end
    n=n1+n2
    return n,n1,n2,nh,n2fields,nhfields
end


EnumLike=AddToModuleHelp{
    EnumLike=[==[--[[--
            A decorator to create an Enum like table that is read only.
--]]--]==]
-- @function EnumLike
, info=info} ..
function(obj)
    assert(type(obj)=="table", "Error EnumLike: decorator must be called on a table")
    obj.__aliases__=obj.__aliases__ or {}
    obj.__keys_rev__={}

    local __n__,i,k,v,__min__,__max 

    -- convert lists to keys
    __min__=obj.__min__ or 0
    for k,v in ipairs(obj) do 
        assert(type(v)=="string", "Error EnumLike: if initiating with a list, entries must be strings")
        i=__min__+k-1 
        obj[v]=i
        obj.__keys_rev__[i]=v
    end
    for k=#obj,1,-1 do table.remove(obj) end

    __max__=__min__
    __n__=0
    for k,v in pairs(obj) do
        if bIsHiddenFieldName(k)==false then
            __n__=__n__+1
            assert(type(v)=="number", "Error EnumLike: non-private fields must be integers, (k,v)=("..k..", "..v..")")
            if obj.__keys_rev__[v]==nil then obj.__keys_rev__[v]=k end
            if v<__min__ then __min__=v end
            if v>__max__ then __max__=v end
            if obj.__aliases__[k]==nil then
                obj.__aliases__[k]=k
            end
            if obj.__aliases__[string.lower(k)]==nil then
                obj.__aliases__[string.lower(k)]=k
            end
            if obj.__aliases__[v]==nil then
                obj.__aliases__[v]=k
            end
        end
    end
    obj.__n__=__n__
    obj.__min__=__min__
    obj.__max__=__max__
    obj.__prototype__=true

    local rv={data=__min__}
    local rv_ClassMT={}
    local rv_new
    local rv_bIsValid
    local rv__index=function(t,k)
        local tk=_G.type(k)
        if k==nil then
            return "EnumLikeObject"
        elseif k=="data" then
            return rawget(t,"data")
        elseif k=="__objref__" then
            return obj
        elseif k=="__copy__" then
            return setmetatable({data=t.data},rv_ClassMT)
            -- return function()return setmetatable({data=t.data},rv_ClassMT) end
        elseif tk=="number" then
            if obj.__keys_rev__[k]==nil then
                error("Error EnumLike, enum value "..k.." not in object")
            end
            return setmetatable({data=k},rv_ClassMT)
        elseif tk=="table" and k.__class__ and k.__class__==rv_ClassMT then
            return setmetatable({data=k.data},rv_ClassMT)
        elseif k=="bIsValid" then
            return rv_bIsValid
        elseif k=="bIsTheSameEnumLike" then
            return function(arg)return type(arg)=="table" and rv_bIsValid(arg.data) and getmetatable(arg)==rv_ClassMT end
        elseif k=="__classname__" then
            return _G.rawget(obj,"__classname__") or "EnumLike"
        elseif k=="__class__" then
            return rv_ClassMT
        elseif string.find(k,"^__(.*)__$")==nil and obj[obj.__aliases__[k]] then
            local lrv=setmetatable({data=obj[obj.__aliases__[k]]},rv_ClassMT)
            return lrv
        elseif string.find(k,"^__(.*)__$")~=nil and obj[k] then
            if k=="__prototype__" then
                if t==obj then
                    return true
                else
                    return false
                end
            else 
                return obj[k]
            end
        elseif obj.__aliases__ and obj.__aliases__[k] then
            local lrv=setmetatable({data=obj[obj.__aliases__[k]]},rv_ClassMT)
            return lrv
        elseif k=="len" or k=="length" then
            return obj.__n__
        elseif k=="min" then
            return obj.__min__
        elseif k=="max" then
            return obj.__max__
        else
            return nil
        end
    end
    local rv__eq=function(a,b)
        local ta=_G.type(a)
        local tb=_G.type(b)
        if ta=="table" and tb=="table" then
            if a.__class__==b.__class__ then
                return a.data==b.data
                -- return _G.rawget(a,1)==_G.rawget(b,1)
            elseif a.__class__==rv_ClassMT then
                return a.data==b.data
                -- return _G.rawget(a,1)==b[1]
            elseif b.__class__==rv_ClassMT then
                return a.data==b.data
                -- return _G.rawget(b,1)==a[1]
            end
        elseif ta=="table" then 
            if tb=="number" then
                return a.data==b
                -- return _G.rawget(a,1)==b
            elseif tb=="string" then
                return a.data==_G.rawget(obj,b)
                -- return _G.rawget(a,1)==_G.rawget(obj,b)
            else
                error("Unknown comp in EnumLike object between "..a.." and "..b)
            end
        elseif tb=="table" then
            if ta=="number" then
                return b.data==a
                -- return _G.rawget(b,1)==a
            elseif ta=="string" then
                return b.data==_G.rawget(obj,a)
                -- return _G.rawget(b,1)==_G.rawget(obj,c)
            else
                error("Unknown comp in EnumLike object between "..a.." and "..b)
            end
        else
            error("Unknown comp in EnumLike object between "..a.." and "..b)
        end
    end
    rv_ClassMT={
        __call=function(self,a) 
            local ta=_G.type(a)
            if bIn(ta,"string","number") then 
                return rv__index(self,a) 
            elseif bIn(ta,"table") and a.__class__ and a.__class__==rv_ClassMT then 
                return _G.setmetatable({data=a.data},rv_ClassMT)
            end 
            return _G.setmetatable({data=obj.__min__},rv_ClassMT)
        end
        , __len=function(self) return obj.__n__ end
        , __eq=rv__eq
        , __tostring=function(self)
            local rv=obj.__keys_rev__[self.data]
            assert(rv~=nill,"Error EnumLike: internal error, no internal reverse key")
            return rv
        end
        , __index=rv__index
        , __newindex=function(t,k,v) error('cannot set a value') end
    }
    local rv_bIsThisEnum
    rv_bIsThisEnum=function(a)
        if _G.type(a)=="table" and a.__class__ and a.__class__==rv_ClassMT and a.data~=nil and obj.__keys_rev__[a.data]~=nil then
            return true
        else
            return false
        end
    end
    rv_bIsValidValue=function(a)
        if bIn(_G.type(a),"string","number") and ( (obj[a]~=nil) or (obj.__aliases__ and obj.__aliases__[a]~=nil) ) then
            return true
        else
            return false
        end
    end
    rv_bIsValid=function(a)
        if rv_bIsValidValue(a) then
            return true
        elseif rv_bIsThisEnum(a) then
            return true
        else
            return false
        end
    end
    rv_new=function(a) 
        if rv_bIsThisEnum(a) then
            return setmetatable({data=a.data},rv_ClassMT) 
        elseif rv_bIsValidValue(a) then
            return setmetatable({data=obj[obj.__aliases__[a]]},rv_ClassMT)
        else
            error("Error EnumLike: call of new on invalid value")
        end
    end
    return setmetatable(rv,rv_ClassMT),obj
end

AddToEnv=AddToModuleHelp{
    AddToEnv=[==[--[[--
            Takes a table and adds key/value pairs to a target table/environment.
--]]--]==]
-- @function AddToEnv
, info=info} ..
function(env,obj)
    if type(obj)~="table" or type(env)~="table" then
        error('Input to AddToEnv must be a single target table/env and a single source table.')
    end
    for k,v in pairs(obj) do
        env[k]=v
    end
    return env
end

AddToEnv_Raw=AddToModuleHelp{
    AddToEnv_Raw=[==[--[[--
            Takes a table and adds key/value pairs to a target table/environment using rawset.
--]]--]==]
-- @function AddToEnv_Raw
, info=info} ..
function(env,obj)
    if type(obj)~="table" or type(env)~="table" then
        error('Input to AddToEnv must be a single target table/env and a single source table.')
    end
    for k,v in pairs(obj) do
        rawset(env,k,v)
    end
    return env
end

AddToEnv_Raw_ByName=AddToModuleHelp{
    AddToEnv_Raw_ByName=[==[--[[--
            Takes a table and adds key/value pairs to a target table/environment using rawset.
--]]--]==]
-- @function AddToEnv_Raw_ByName
, info=info} ..
function(env,obj,names)
    if type(env)~="table" or type(obj)~="table" or type(names)~="table" then
        error('Input to AddToEnv must be a single target table/env and a single source table.')
    end
    for i,k in ipairs(obj) do
        rawset(env,k,rawget(obj,v))
    end
    return env
end


local wdsnull=require("WDS.NULL")

NULL=AddToModuleHelp{
    NULL=[==[--[[--
            A null object singleton.

            Since a lua nil object is collected, NULL represents a persistent, non-mutable singleton.<br>
            All variables assigned a NULL reference the same object and the test x==y holds if both x and y are NULLs.<br>
--]]--]==]
-- @field NULL
, info=info } ..  wdsnull.NULL


NaN=AddToModuleHelp{
    NaN=[==[--[[--
            A floating point NaN constant.
--]]--]==]
-- @field NaN
, info=info } ..  (0/0)

Inf=AddToModuleHelp{
    Inf=[==[--[[--
            A floating point inf constant.
--]]--]==]
-- @field Inf
, info=info } ..  (math.huge)

NegInf=AddToModuleHelp{
    NegInf=[==[--[[--
            A floating point -inf constant.
--]]--]==]
-- @field NegInf
, info=info } ..  (-1/0)

bIsNaN=AddToModuleHelp{
    bIsNaN=[==[--[[--
            A check for floating point NaN.
--]]--]==]
-- @function bIsNaN
, info=info} ..
function(arg) 
    if type(arg)=="number" then return (arg~=arg) end
    if type(arg)=="string" then 
        if bIn(arg,"NaN","NAN","nan","0/0") then 
            return true
        end
        error("Error bIsNaN: cannot check \""..arg.."\" for nan.")
    end
    return false
end

local __bIsFinite= function(arg) 
    if type(arg)=="number" then 
        local mtarg=math.type(arg)
        if mtarg=="float" then
            return not (bIsNaN(arg) or (arg==Inf) or (arg==NegInf))
        else
            return not (arg==math.mininteger or arg==math.maxinteger)
        end
    else
        return false
    end
end
        
bIsFinite=AddToModuleHelp{
    bIsFinite=[==[--[[--
            A check for a finite number.
--]]--]==]
-- @function bIsFinite
, info=info } ..
function(arg) 
    if type(arg)=="number" then return __bIsFinite(arg) end
        if bIn(string.lower(arg),"inf","infinity","+inf","-inf","1/0","-1/0","nan","na") then 
            return false
        elseif bIn(string.lower(arg),"true","false") then 
            return true
        else
            return __bIsFinite__(tonumber(arg))
        end
    return false
end

bIsInf=AddToModuleHelp{
    bIsNaN=[==[--[[--
            A check for floating point +inf.
--]]--]==]
-- @function bIsInf
, info=info
} ..
function(arg) 
    if type(arg)=="number" then return (arg==Inf) end
    if type(arg)=="string" then 
        if bIn(string.lower(arg),"inf","infinity","+inf","1/0") then 
            return true
        end
        error("Error bIsInf: cannot check \""..arg.."\" for +inf.")
    end
    return false
end

bIsNegInf=AddToModuleHelp{
    bIsNaN=[==[--[[--
            A check for floating point -inf.
--]]--]==]
-- @function bIsNegInf
, info=info } ..
function(arg) 
    if type(arg)=="number" then 
        return (arg==NegInf) 
    end
    if type(arg)=="string" then 
        if bIn(string.lower(arg),"-inf","-infinity","-1/0") then 
            return true
        else
            error("Error bIsInf: cannot check \""..arg.."\" for -inf.")
        end
    end
    return false
end

bIsTrue=AddToModuleHelp{
    bIsTrue=[==[--[[--
            A boolean check for a boolean true value, checking the usual suspects across data types, such as "true","yes",1, etc..
--]]--]==]
-- @function bIsTrue
, info=info } ..
function(arg)
    if arg==true then return true end
    if arg==nil or arg==false or arg==NULL then return false end
    local targ=type(arg)
    if targ=="number" then
        -- un-lua-like, take a 0 value, NaN, or +/-Inf as false
        return bIsFinite(arg) and math.abs(arg)>1e-10
    elseif targ=="string" then
        local larg=trim(string.lower(arg))
        if larg=="false" then
            return false
        elseif larg=="true" then
            return true
        elseif bIn(larg,"0","f","no","n") then
            return false
        elseif bIn(larg,"1","t","yes","y") then
            return true
        end
    else
        return (arg==arg)
    end
end

bIsEmpty=AddToModuleHelp{
    bIsEmpty=[==[--[[--
            A boolean check for what are considered empty values (nil,NULL,"",{}).<br>

                Note: Unless the optional second argument includes {hidden=true}, <br>
                    hidden field names (i.e., of the form __AAA__), are not counted.<br>
--]]--]==]
-- @function bIsEmpty
, info=info } ..
function(obj,opts)
    opts=opts or {}
    opts.hidden=opts.hidden or false
    if obj==nil then
        return true
    elseif type(obj)=="string" then
        return obj:len()==0
    elseif type(obj)=="table" then
        if #obj>0 then
            return false
        else
            for k,v in pairs(obj) do
                if opts.hidden and not bIsHiddenFieldName(k) then
                    return false
                end
            end
        end
        return true
    end
    return false
end

--- A test function for WDS, used if bIsMain(...)
-- @function __testcall__
__testcall__=function()
    print("testing in "..module_name)
    print("module_path "..module_path)
    print()
    print("help on "..module_name)
    print(help(_M))
    print()
    print("show(_G)")
    print(show(_G))
    print(show_keys(_G,{depth=3}))
    t={1,3,4,hey="what",["x.1"]=44}
    print("wds.show(t)=",show(t))
    ts=lson(t,{name="t",includereturn=true})
    print("wds.lson(\"t\",t,1)=",ts)
    t2=load(ts)()
    print("wds.show(load(ts)())=",show(t2))
    t2=load(ts)
    print("wds.show(load(ts))=",show(t2))
    print("wds.table_simple_value_comp(t,load(ts)())=",table_simple_value_comp(t,load(ts)()))

    s="hey what the hey is going on hey there"
    print(">>>s<<<=",">>>"..s.."<<<")
    print("split-test, dlm=hey:",show(string_split(s,"hey")))
    s="' what the hey is going on 'hey there"
    print("split-test, dlm=hey, >>>s<<<=>>>"..s.."<<< :",show(string_split(s,"hey",true)))
    s="the rain, in spain,' falls mainly, in the', plain"
    print("split-test, dlm=',', >>>s<<<=>>>"..s.."<<< :",show(string_split(s,',',true)))
    s="the rain, in spain,     \" falls mainly, in the\" , plain"
    print("split-test, dlm=',', >>>s<<<=>>>"..s.."<<< :",show(string_split(s,',',true)))
    s="the rain, in spain,     \" falls mainly, in the , plain"
    print("split-test, dlm=',', >>>s<<<=>>>"..s.."<<< :",show(string_split(s,',',true)))
    s="the rain, in spain,   '  \" falls mainly, in the \" ' , plain"
    print("split-test, dlm=',', >>>s<<<=>>>"..s.."<<< :",show(string_split(s,',',true)))


    print("testing EnumLike....")
    jtype=EnumLike{unk=0,object=1,array=2,number=3,string=4,boolean=5,null=6}
    print("jtype=",jtype)
    x=jtype.array
    print("x=",x,", (x==jtype.array)=",(x==jtype.array))
    print("jtype.bIsValid(3)",jtype.bIsValid(3))
    print("jtype.bIsValid(jtype.array)",jtype.bIsValid(jtype.array))
    print("jtype.bIsValid(jtype.huh)",jtype.bIsValid(jtype.huh))

end

if module_name_dots=="main-call-without-args" or bIsMain(table.pack(...),module_name) then
    __testcall__()
end

return EnvLock(_M)

