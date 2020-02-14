--[[Copyright (c) 2019 Wypasek Data Science, Inc.
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

--- A wrapper of expat that preserves order and comments
-- @submodule WDS.Wranglers
-- @within WDS.Wranglers


local wds=require("WDS")
local wdsu=require("WDS.Util")
local pesc=require("WDS.Util.python_esc")
local wdsm=require("WDS.Comp.Matrix")

local __parent__="Wranglers"
local __name__="xml_expat"
local module_name_dots=( ... or "main-call-without-args" )
local module_name=__parent__.."."..__name__
local module_path=""

local docstring=module_name .. " ("..module_path..")"..[==[
    A wrapper of expat that preserves order and comments.

    --under construction

    The format was necessary for processing certain schemas where comments
    associated with an element preceed the element.

    The premise the following:
        - An xml node is mapped to a table {}.
            - In the underlying lua structure: 
                - node contents are indexed contents
                    - only empty whitespace nodes are ignored
                    - comments are added as empty tables with a
                        __Comment__="..." field
                    - a single content value split by comments will 
                      be returned as multiple entries
                    - child nodes are unique table elements
                - a table to be treated as an xml node has a 
                    __XML__ field
                - the node QName is in the __QName__
                - any attributes are in the __Attributes__ field
                - other hidden fields may contain:
                    __Prefix__ : namespace
                    __LocalPart__ : QName without prefix
                    __Schema__ : type information
        - Calling a name field will return an iterator over 
          child nodes of that name.

]==]


local dbg
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
    dbg=require("debugger")
    dbg.auto_where=2
else
    dbg=function() end
end

if module_name_dots=="main-call-without-args" or wds.bIsMain(table.pack(...),module_name) then
    print("test with "..__parent__.."/"..__name__.."_test.lua")
    print(docstring)
    os.exit()
end

local _M={}
local _G=_G
_ENV=wds.EnvExtension(_M,_G)

-- to use with out prefix....
wds.AddToEnv_Raw_ByName(_M, wds, {"bIsHiddenFieldName","NULL","Nan"} )

-- this module's info table for use with wds.help
info={name=module_name
    ,path=module_path
    ,doc=docstring
    ,docmap={}
}

-- localizing AddToModuleHelp to globally assign to this module's info table
local AddToModuleHelp=function(tbl,tbl2); tbl.info=info; return wds.AddToModuleHelp(tbl,tbl2); end

local xml_expat_base=require("WDS.Wranglers.xml_expat_base")
local bIsTable=xml_expat_base.bIsTable

__XML_class__={__classname__="XML"}

base_parse=AddToModuleHelp{
    base_parse=[==[--[[--
            The base parse used for the xml_expat module, returns raw tables without xml_expat metafunctions.
--]]--]==]
-- @function base_parse
} .. function(a,enc)
    enc=enc or "UTF-8"
    return xml_expat_base.parse(a,__XML_class__,enc)
end


bIsXML=AddToModuleHelp{
    bIsXML=[==[--[[--
            A boolean check for argument as an xml_expat object instance. <br>
--]]--]==]
-- @function bIsXML
} .. function(a)
    if not bIsTable(a) then return false end
    if getmetatable(a)==__XML_class__ then return true end
    return false;
end

bIsComment=AddToModuleHelp{
    bIsComment=[==[--[[--
            A boolean check for argument as an xml_expat comment object (#obj=0, obj.__Comment__=string). <br>
--]]--]==]
-- @function bIsXML
} .. function(a)
    if (not bIsTable(a)) or (#a~-0) or (a.__Comment__==nil) or type(a.__Comment__)~="string" then return false end
    return true;
end

bIsQName=AddToModuleHelp{
    bIsQName=[==[--[[--
            A boolean check for first argument is an xml_expat object instance with a given QName. <br>
--]]--]==]
-- @function bIsXML
} .. function(a)
    if not bIsXML(a) then return false end
    local nm=rawget(a,"__LocalName__")
    if nm and nm==a then return true end
    nm=rawget(a,"__QName__")
    if nm and nm==a then return true end
    return false
end



__XML_class__.__index=function(self,a)
    if a=="__class__" then return __XML_class__
    elseif a=="__classname__" then return __XML_class__.__classname__
    elseif a=="name" then return function() return rawget(self,"__QName__") end
    elseif a=="child" then
        return function(self,i,opts)
            opts=opts or {}
            opts.ignore_comments=opts.ignore_comments or true
            local j,k,v
            k=0
            for j=1,rawlen(self),1 do
                v=rawget(self,j)
                if bIsTable(v) and v.__comment__ then
                    if not opts.ignore_comments then
                        k=k+1
                    end
                else
                    k=k+1
                end
                if i==k then 
                    return v
                end
            end
            return nil
        end
    elseif a=="children" then -- return an iterator that can be evaluated on a single index
        return function(self,opts)
            if opts and type(opts)=="number" then -- return a child
                return self:child(opts)
            end
            opts=opts or {}
            opts.ignore_comments=opts.ignore_comments or true
            local __state__={0,opts.ignore_comments,0,self}
            return function(s, var)
                if var==nil and type(s)=="number" then -- fetch single
                    return __state__[4]:child(s)
                else
                    if var>0 then
                        var=s[1]
                    end
                    var=var+1
                    local v=rawget(s[4],var)
                    if v==nil then return nil,nil end
                    if s[2] then
                        while (v and bIsTable(v) and v.__Comment__) do
                            var=var+1
                            v=rawget(s[4],var)
                            if v==nil then return nil,nil end
                        end
                    end
                    s[1]=var
                    return var,v
                end
            end, __state__, 0
        end
    else 
        local found=false
        local i=0
        local v, qnm
        while (true) do
            i=i+1
            v=rawget(self,i)
            if v==nil then break end
            found=bIsXML(v) and rawget(v,"__QName__")==a 
            if found then break end
        end
        if not found then return nil end
        local __nodelist__={v}
        while (true) do
            i=i+1
            v=rawget(self,i)
            if v==nil then break end
            found=bIsXML(v) and rawget(v,"__QName__")==a 
            if found then table.insert(__nodelist__,v) end
        end
        return function(self,opts)
            if opts and type(opts)=="number" then -- return a child
                return __nodelist__[opts]
            end
            local __state__={0,#__nodelist__,self,__nodelist__}
            return function(s, var)
                if var==nil and type(s)=="number" then -- fetch single
                    return __nodelist__[s]
                else
                    if var>0 then
                        var=s[1]
                    end
                    var=var+1
                    if var>s[2] then return nil,nil end
                    local v=s[4][var]
                    s[1]=var
                    return var,v
                end
            end, __state__, 0
        end
    end
end




XML=AddToModuleHelp{
    XML=[==[--[[--
            The constructor for an xml_expat object.
--]]--]==]
-- @function XML
} .. function(a,enc)
    enc=enc or "UTF-8"
    local rc,rv,msg=xml_expat_base.parse(a,__XML_class__,enc)
    if rc==nil or rc~=0 then
        error("Error XML (xml_expat): cannot parse input, msg="..msg)
    end
    return rv
end

return wds.EnvLock(_M)

