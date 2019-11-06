--[[Copyright 2019, Wypasek Data Science, Inc.  (WDataSci, WDS)
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

--CodeRef: CW - hints from
--https://stackoverflow.com/questions/9145432/load-lua-files-by-relative-path
--https://stackoverflow.com/questions/42217459/how-to-read-a-data-file-at-a-package-path-on-lua-5-1
--https://stackoverflow.com/questions/38800475/confusion-with-debug-getlocal-in-lua

-- the localizing of arg below shorts the global arg of a program that might require this module
local arg 

local module_name_dots=( ... or "main-call-without-args" )
-- to hard-code use.......
local module_name="WDS"

local module_path=""
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
end

local mrv={}
local _M_G=_G


-- this is a simplified way of providing an info element which the help function
-- can be used to query

mrv.info={name=module_name
    ,path=module_path
    ,doc=module_name .. " ("..module_path..")"..[==[
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
}

local AddToModuleHelp=function(infoblock)
    local name="Unk"
    local usuals={_ENV=1, name=1, doc=1, info=1}
    for k,v in pairs(infoblock) do
        if usuals[k] then
            if k=="_ENV" then
                infoblock.info=_ENV.info
            end
        elseif type(v)=="string" then
            infoblock.name=k
            infoblock.doc=v
            break
        end
    end
    return setmetatable({},{__concat=
        function(tmp,obj)
            infoblock.info.docmap[obj]={name=infoblock.name,doc=infoblock.doc}
            if infoblock._ENV then
                infoblock._ENV[infoblock.name]=obj
            end
            return obj
        end})
    end

mrv.AddToModuleHelp=AddToModuleHelp{
    AddToModuleHelp=[==[A decorator for adding entries to a module's info.docmap table.]==]
    , info=mrv.info} ..
    AddToModuleHelp

            
help=AddToModuleHelp{
    help=[==[A global help function]==]
    , info=mrv.info} ..
    function (obj)
    local rv=obj and obj.info and obj.info.doc
    if rv~=nil then
        if obj.info.docmap then
            rv=rv .. "\n  DocMap Table"
            for k,v in pairs(obj.info.docmap) do
                rv=rv .. "\n    " .. v.name .. " - " .. v.doc
            end
        end
        return rv
    else 
        for k,v in pairs(packages) do
            rv=v.info and v.info.docmap and v.info.docmap[obj]
            if rv then
                return rv
            end
        end
        rv="help (.info.doc string) not avialable"
    end
    return rv
end




mrv.help=
    function (obj)
    local rv=""
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


mrv.dir=AddToModuleHelp{
        dir=[==[A python-like dir() function to show table keys.]==]
    ,info=mrv.info} ..
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

local __show
__show=function (obj,depth)
    if type(obj) ~= "table" then
        return tostring(obj)
    end
    local rv=""
    local i=0
    for k,f in pairs(obj) do
        --_M_G.print("k,f=",k,f)
        i=i+1
        if i>1 then 
            rv=rv .. ", "
        end
        if type(f)=="function" then
            --rv=rv .. "["..k.."]=function"
            rv=rv .. "["..k.."]="..tostring(f)
        elseif type(f)=="table" then
            --rv=rv .. "["..k.."]=table"
            if depth and depth>0 then
                rv=rv .. "["..k.."]={"..__show(f,depth-1).."}"
            else
                rv=rv .. "["..k.."]="..tostring(f)
            end
        else    
            rv=rv .. "[k=["..__show(k).."]]="..tostring(f)
        end
    end
    return rv
end

mrv.show=AddToModuleHelp{
        show=[==[A simple table dump to string]==]
    , info=mrv.info} ..
    __show

show=function(obj) print(mrv.show(obj)) end

mrv.show_values=AddToModuleHelp{
        show_values=[==[A simple print of just a table's values.]==]
    , info=mrv.info} ..
    function (obj)
    local rv=""
    local i=0
    for k,f in pairs(obj) do
        i=i+1
        if i>1 then 
            rv=rv .. ", "
        end
        if type(f)=="function" then
            --rv=rv .. k.."=function"
            rv=rv .. k.."="..tostring(f)
        elseif type(f)=="table" then
            --rv=rv .. k.."=table"
            rv=rv .. k.."="..tostring(f)
        else    
            rv=rv .. tostring(f)
        end
    end
    return rv
end

mrv.keys=AddToModuleHelp{
        keys=[==[A simple function to pull a table's keys into a indexed table.]==]
    , info=mrv.info} ..
    function (obj, ... )
    if type(obj) ~= "table" then
        return nil
    end
    local arg=table.pack(...)
    local tosort = (arg.n==1)
    local rv={}
    for k,f in pairs(obj) do
        table.insert(rv,k)
    end
    if tosort then
        table.sort(rv, function (a,b) return tostring(a)<tostring(b) end)
    end
    return rv
end

mrv.show_keys=function (obj, ... )
    if type(obj) ~= "table" then
        return ""
    end
    local rv=""
    local lrv=mrv.keys(obj,...)
    for i,f in ipairs(lrv) do
        if i>1 then 
            rv=rv .. ", "
        end
        rv=rv .. f
    end
    return rv
end

dir=function (obj) 
    if obj ~= nil then
        print(mrv.show_keys(obj,1))
    else
        print(mrv.show_keys(_G,1))
    end
    return
end

mrv.locals=AddToModuleHelp{
        locals=[==[A simple query of the locals available.]==]
    , info=mrv.info} ..
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

    mrv.dump=local_dump
end

mrv.StringExportable=AddToModuleHelp{
    StringExportable=[==[A simple function to return a string for serialization purposes.]==]
    , info=mrv.info} ..
    function(word,keyquote)
    -- print("word=",word)
    -- print("keyquote=",keyquote)
    --[[-- according to the manual, use %q instead of fixing things by hand ....
            local slash_escapes={a="\a",n="\n",r="\r",t="\t",v="\v",bs="\\",dq="\"",sq="\'"}
            local rv=word
            local rv_needs_to_be_quoted=false
            for k,v in pairs(slash_escapes) do
                if string.find(rv,v) then
                    rv=string.gsub(rv,v,"\\"..k)
                    rv_needs_to_be_quoted=true
                end
            end
    --]]
    local rv=string.format("%q",word)
    rv=string.sub(rv,2,#rv-1)
    local rv_needs_to_be_quoted=false
    if rv_needs_to_be_quoted==false and string.find(rv,"[^%w_]") then
        rv_needs_to_be_quoted=true
    end
    local qrv=rv
    if rv_needs_to_be_quoted then
        if keyquote then
            qrv='["'..rv..'"]'
        else
            qrv='"'..rv..'"'
        end
    end
    return rv, qrv
end

-- using the semi-standard dump example to create an lson
do
    local local_lson
    local_lson=function(name,t,includereturn)
        -- print("name=",name)
        -- print("t=",t)
        -- print("t=",mrv.show(t))
        local name1, qname
        if name then
            name1,qname=mrv.StringExportable(name,1)
            name1=qname
            qname=qname.."="
        else
            name1=""
            qname=""
        end
        if t == nil then
            return qname.."{__nil__=true}\n"
        elseif type(t)=="string" then
            local t1,qt=mrv.StringExportable(t)
            return qname.."[["..t1.."]]\n"
        elseif type(t)=="boolean" or type(t)=="number" then
            return qname..""..tostring(t).."\n"
        elseif type(t)=="function" then
            return qname.."[["..string.dump(t).."]]\n"
        elseif type(t)=="userdata" or type(t)=="thread" then
            return qname.."[[cannot be serialized, "..type(t).."]]\n"
        end
        local rvs=qname.."{"
        local seen={}
        local n=0
        for i,v in ipairs(t) do
            n=n+1
            if n==1 then
                rvs=rvs..local_lson(nil,v)
            else
                rvs=rvs..", "..local_lson(nil,v)
            end
            seen[i]=i
        end
        for k,v in pairs(t) do
            if seen[k]==nil then
                n=n+1
                if n==1 then
                    rvs=rvs..local_lson(k,v)
                else
                    rvs=rvs..", "..local_lson(k,v)
                end
            end
        end
        if includereturn then
            if name then
                return rvs.."}\nreturn "..name1.."\n"
            else
                return "return "..rvs.."}\n"
            end
        else
            return rvs.."}\n"
        end
    end
    mrv.lson=local_lson
end


mrv.string_startswith_exp = AddToModuleHelp{
        string_startswith_exp=[==[A simple boolean test if a string starts with a match pattern.]==]
    , info=mrv.info} ..
    function (arg1,arg2)
    i,j=string.find(arg1,"^"..arg2) 
    return i and i==1
end

mrv.string_startswith = AddToModuleHelp{
        string_startswith=[==[A simple boolean test if a string starts with another string.]==]
    , info=mrv.info} ..
    function (arg1,arg2)
    if type(arg1)~="string" then
        arg1=tostring(arg1)
    end
    if type(arg2)~="string" then
        arg2=tostring(arg2)
    end
    --check for magic characters which will need to be escaped
    local i,j=string.find(arg2,"[%(%_%.%%%+%-%*%?%[%]%^%$]") 
    if i then
        arg2=string.gsub(arg2,"[%(%_%.%%%+%-%*%?%[%]%^%$]","%%%1") 
    end
    return mrv.string_startswith_exp(arg1,arg2)
end

mrv.string_split = AddToModuleHelp{
        string_split=[==[A simple string split.]==]
    , info=mrv.info} ..
    function (s,dlm,quoted,trimit)
        if dlm==nil then
            dlm=" "
        end
        local rv={}
        --for the pattern "(.-)"..dlm 
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
            _s=_M_G.string.gsub(s,"^%s*(.-)%s*$","%1")..dlm
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
                local a,b,c,d=_M_G.string.find(_s,"^"..dlm.."%s-([\"'])(.-)%1%s-"..dlm,starti)
                if a~=nil then
                    if d==nil or #d==0 then
                        _M_G.table.insert(rv,"")
                    else
                        _M_G.table.insert(rv,d)
                    end
                    starti=b-#dlm+1
                    stop=(b==#_s)
                else
                    a,b,c=_M_G.string.find(_s,"^"..dlm.."(.-)"..dlm,starti)
                    if a~=nil then
                        if c==nil or #c==0 then
                            _M_G.table.insert(rv,"")
                        else
                            _M_G.table.insert(rv,c)
                        end
                        starti=b-#dlm+1
                        stop=(b==#_s)
                    else
                        stop=true
                    end
                end
            end
        else
            for _seg in _M_G.string.gmatch(_s,"(.-)"..dlm) do
                _M_G.table.insert(rv,_seg)
            end
        end
        return rv
    end

    
-- check to see if python-esc module __init__.lua files can be found on paths
-- with /WDS/ or :\WDS\ 

-- print("package.path=",package.path)
if string.find(package.path,"%?.__init__.lua") == nil then
    local s=""
    for k,v in pairs(mrv.string_split(package.path,";")) do
        if ( string.find(v,"WDS(.-)%?%.lua$") ~= nil ) and ( string.find(v,"%?.%?") == nil ) then
            if string.find(v,":\\") == nil then
                s= s .. ";" .. string.match(v,"(.-)%?%.lua$") .. "?/__init__.lua"
            else
                s= s .. ";" .. string.match(v,"(.-)%?%.lua$") .. "?\\__init__.lua"
            end
        end
    end
    -- print("s=",s)
    if s~="" then
        package.path=package.path..s
        -- print("updated lua search path ",package.path)
    end
end


--is_main, if called in the ``main'' function includes arg[-1]=lua<<version>>

local is_main=function(args,module_name)
    if module_name and args[0] then
        if string.find(args[0],module_name..".lua") then
            return true
        else
            return false
        end
    end
    return ( args and ( 
        ( args[0] and args[-1] and mrv.string_startswith_exp(args[-1],"lua[56]%.") )
        or args[1]=="--main" )
        )
end
    
mrv.is_main=AddToModuleHelp{
    is_main=[==[A boolean for tests in module files, use like wds.is_main(arg,modulename).]==]
    , info=mrv.info} ..
    is_main

q=AddToModuleHelp{
    q=[==[An R-like q() function to exit.  Added to globals.]==]
    , info=mrv.info} ..
    function()
    os.exit()
end

mrv.bIn=AddToModuleHelp{
    bIn=[==[An SQL-like in() function, but use as bIn(arg, a1, a2, ..., an) for 'arg in(a1, a2, ..., an)'.]==]
    , info=mrv.info} ..
    function(a,...)
    local arg=table.pack(...)
    for i,v in ipairs(arg) do
        if a==v then
            return true
        end
    end
    return false
end

local local_table_simple_value_comp
local_table_simple_value_comp=function(a,b)
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
            elseif mrv.bIn(tai,"string","boolean","number") then
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
mrv.table_simple_value_comp=AddToModuleHelp{
    table_simple_value_comp=[==[A not-too-deep comp of two tables.]==]
    , info=mrv.info} ..
    local_table_simple_value_comp

mrv.simple_copy=AddToModuleHelp{
    table_simple_copy=[==[A not-too-deep copy of an object.]==]
    , info=mrv.info} ..
    function(obj)
        if mrv.bIn(type(obj),"string","number") then
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

--[[
local mrv.lson=function(args)
    local s=""
    if type(arg)=="table" then
        
    else
    end
end
--]]

mrv.nilable_instance_of=function(obj,extension_methods)
    local l__index
    local l__newindex
    l__index=function(t,k) 
        if k=="new" then
            do
                local rv={}
                for i,v in pairs(obj) do
                    rv[i]=v
                end
                return setmetatable(rv,{__index=l__index,__newindex=l__newindex})
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
    l__newindex=function(t,k,v) 
        if v==nil and obj[k] then 
            rawset(t,k,{__nil__=true}) 
        elseif obj[k] then 
            rawset(t,k,v) 
        else 
            error(k.." is not a valid key") 
        end 
    end
    return setmetatable({__proto=obj},{__index=l__index,__newindex=l__newindex})
end

mrv.length=AddToModuleHelp{
    length=[==[A length function to count pairs of a table (since # does not work that way...).]==]
    , info=mrv.info} ..
    function(obj)
        if type(obj)~="table" then
            return 1
        end
        local n=0
        for k,v in pairs(obj) do
            n=n+1
        end
        return n
    end

mrv.EnumLike=AddToModuleHelp{
    EnumLike=[==[A decorator to create an Enum like table that is read only.]==]
    , info=mrv.info} ..
    function(obj)
    if type(obj)=="table" then
        _M_G.print("In EnumLike setup for object=",mrv.show(obj))
        if obj.aliases==nil then
            obj.aliases={}
        end
        -- add lowcases to aliases if necessary
        for k,v in pairs(obj) do
            if type(v)=="number" then 
                local kl=string.lower(k)
                if obj[kl]==nil and obj.aliases[kl]==nil then
                    obj.aliases[kl]=k
                end
            end
        end
        for k,v in pairs(obj.aliases) do
            local kl=string.lower(k)
            if obj.aliases[kl]==nil then
                obj.aliases[kl]=v
            end
        end
        local minobj, maxobj
        local n=0
        for i,o in pairs(obj) do 
            if type(o)=="number" then 
                n=n+1
                if minobj==nil or o<minobj then minobj=o end 
                if maxobj==nil or o<maxobj then maxobj=o end 
            end
        end
        obj.__len=n
        obj.__min=minobj
        obj.__max=maxobj
        local rv={minobj}
        local rv_ClassMT={}
        local rv_new=function(a) return _M_G.setmetatable(a,rv_classMT) end
        local rv__index=function(t,k)
                if _M_G.type(k)=="number" and k==_M_G.math.floor(k) then
                    for i,o in _M_G.pairs(obj) do
                        if o==k then return rv_new{k} end
                    end
                    error("Index, "..k..", not in EnumLike object.")
                elseif _M_G.type(k)=="table" and k.__class__ and k.__class__==rv_ClassMT then
                    return setmetatable({_M_G.rawget(k,1)},rv_ClassMT)
                elseif k=="__class__" then
                    return rv_ClassMT
                elseif k~="aliases" and obj[k] then
            --_M_G.print("k=",k)
            --_M_G.print("rv_ClassMT=",mrv.show(rv_ClassMT))
            --_M_G.print("{obj[k]}=",mrv.show({obj[k]}))
                    local lrv=setmetatable({obj[k]},rv_ClassMT)
            --_M_G.print("lrv=",mrv.show(lrv))
            --_M_G.print("lrv MT=",mrv.show(_M_G.getmetatable(lrv)))
                    return lrv
                    --_M_G.setmetatable({obj[k]},rv_ClassMT)
                    -- return rv_new{obj[k]}
                elseif obj.aliases and obj.aliases[k] then
                    return rv_new{obj[obj.aliases[k]]}
                elseif k=="len" or k=="length" then
                    return obj.__len
                elseif k=="min" then
                    return obj.__min
                elseif k=="max" then
                    return obj.__max
                end
            end
        local rv__eq=function(a,b)
                --_M_G.print("a,b=",a,b)
                local ta=_M_G.type(a)
                local tb=_M_G.type(b)
                if ta=="table" and tb=="table" then
                    if a.__class__==b.__class__ then
                        return _M_G.rawget(a,1)==_M_G.rawget(b,1)
                    elseif a.__class__==rv_ClassMT then
                        return _M_G.rawget(a,1)==b[1]
                    elseif b.__class__==rv_ClassMT then
                        return _M_G.rawget(b,1)==a[1]
                    end
                elseif ta=="table" then 
                    if tb=="number" then
                        return _M_G.rawget(a,1)==b
                    elseif tb=="string" then
                        return _M_G.rawget(a,1)==rv__index({},b)
                    else
                        error("Unknown comp in EnumLike object between "..a.." and "..b)
                    end
                elseif tb=="table" then
                    if ta=="number" then
                        return _M_G.rawget(b,1)==a
                    elseif ta=="string" then
                        return _M_G.rawget(b,1)==rv__index({},a)
                    else
                        error("Unknown comp in EnumLike object between "..a.." and "..b)
                    end
                else
                    error("Unknown comp in EnumLike object between "..a.." and "..b)
                end
            end
        rv_ClassMT={
            __call=function(self,a) 
                local ta=_M_G.type(a)
                if mrv.bIn(ta,"string","number") then 
                    return rv__index(self,a) 
                elseif mrv.bIn(ta,"table") then 
                    return _M_G.setmetatable({_M_G.rawget(a,1)},rv_ClassMT)
                end 
                return _M_G.setmetatable({},rv_ClassMT)
            end
            , __eq=rv__eq
            , __tostring=function(a)
                for i,o in pairs(obj) do
                    if _M_G.rawget(a,1)==o then return i end
                end
            end
            , __index=rv__index
            , __newindex=function(t,k,v) error('cannot set a value') end
        }
        --_M_G.print("rv_ClassMT=",mrv.show(rv_ClassMT))
        rv_new=function(a) return _M_G.setmetatable(a,rv_classMT) end
        return setmetatable(rv,rv_ClassMT)
    end
end

mrv.AddToEnv=AddToModuleHelp{
    AddToEnv=[==[Take a table and add key/value pairs to a target table/environment.]==]
    , info=mrv.info} ..
    function(env,obj)
        if type(obj)~="table" or type(env)~="table" then
            error('Input to AddToEnv must be a single target table/env and a single source table.')
        end
        for k,v in pairs(obj) do
            env[k]=v
        end
        return env
    end

mrv.isEmpty=function(obj)
    if obj==nil then
        return true
    elseif type(obj)=="string" then
        return obj:len()==0
    elseif type(obj)=="table" then
        if #obj>0 then
            return false
        else
            for k,v in pairs(obj) do
                return false
            end
        end
        return true
    end
    return false
end

mrv.__testcall__=function()
    print("testing in "..module_name)
    print("module_path "..module_path)
    print()
    print("help on "..module_name)
    print(mrv.help(mrv))
    print()
    print("show(_G)")
    print(mrv.show(_G))
    print(mrv.show_keys(_G,1))
    t={1,3,4,hey="what",["x.1"]=44}
    print("wds.show(t)=",mrv.show(t))
    ts=mrv.lson("t",t,1)
    print("wds.lson(\"t\",t,1)=",ts)
    t2=load(ts)()
    print("wds.show(load(ts)())=",mrv.show(t2))
    print("wds.table_simple_value_comp(t,load(ts)())=",mrv.table_simple_value_comp(t,load(ts)()))

    s="hey what the hey is going on hey there"
    print(">>>s<<<=",">>>"..s.."<<<")
    print("split-test, dlm=hey:",mrv.show(mrv.string_split(s,"hey")))
    s="' what the hey is going on 'hey there"
    print("split-test, dlm=hey, >>>s<<<=>>>"..s.."<<< :",mrv.show(mrv.string_split(s,"hey",true)))
    s="the rain, in spain,' falls mainly, in the', plain"
    print("split-test, dlm=',', >>>s<<<=>>>"..s.."<<< :",mrv.show(mrv.string_split(s,',',true)))
    s="the rain, in spain,     \" falls mainly, in the\" , plain"
    print("split-test, dlm=',', >>>s<<<=>>>"..s.."<<< :",mrv.show(mrv.string_split(s,',',true)))
    s="the rain, in spain,     \" falls mainly, in the , plain"
    print("split-test, dlm=',', >>>s<<<=>>>"..s.."<<< :",mrv.show(mrv.string_split(s,',',true)))
    s="the rain, in spain,   '  \" falls mainly, in the \" ' , plain"
    print("split-test, dlm=',', >>>s<<<=>>>"..s.."<<< :",mrv.show(mrv.string_split(s,',',true)))
end



if module_name_dots=="main-call-without-args" or mrv.is_main(table.pack(...)) then
    mrv.__testcall__()
end



return mrv

