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

--- A few utilities similar to common Python elements.
-- @submodule WDS.Util

-- Require the base module and set free names into the module
-- environment to be returned.
local wds=require("WDS")
local _M={}
local _G=_G
_ENV=wds.EnvExtension(_M,_G)

local wdsu=require("WDS.Util")

local __parent__="Util"
local __name__="python_esc"
local module_name_dots=( ... or "main-call-without-args" )
-- to hard-code use.......
local module_name=__parent__.."."..__name__
local module_path=""

local dbg
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
    dbg=require("debugger")
    dbg.auto_where=2
else
    dbg=function() end
end

local arg 

info={name=module_name
    ,path=module_path
    ,doc=module_name .. " ("..module_path..")"..[==[
    A set of functions which mirror some of the python code
        (especially in the WDS test code)
    
    For example:
        x=list_range(l) will return the python equivalent of list(range(l))

    ]==]
    ,docmap={}
    ,_ENV=_M
}
-- localizing AddToModuleHelp to globally assign to this module's info table
local AddToModuleHelp=function(tbl,tbl2) 
    local k,v
    for k,v in pairs(tbl) do
        if type(v)=="string" and string.find(v,"^%-%-%[%[%-%-") and string.find(v,"%-%-%]%]%-%-$") then
            v=string.sub(v,7,#v-6)
            tbl[k]=v
        end
    end
    tbl.info=info 
    return wds.__AddToModuleHelp(tbl,tbl2) 
end

range=AddToModuleHelp{
    range=[==[--[[--
            A python3-ish range iterator, but lua-ish in that end-points are inclusive.
--]]--]==]
--@function range
} .. 
function(a,b,c) 
    if b==nil then a,b=1,a end 
    if c==nil then c=1 end 
    local __state__={a,b,c,0,a-c} 
    return function(t, j) 
                t[5]=t[5]+t[3]
                if t[5]<=t[2] then 
                    return t[5] 
                else
                    return nil
                end 
            end,__state__,0 
end

list=function(f) local rv={} for v in (function () return f, {}, 0 end)()  do table.insert(rv,v) end return rv end


list_range=AddToModuleHelp{
    list_range=[==[--[[--
            A python3-ish list(range()) object, as opposed to the iterator, range().
            @function list_range
--]]--]==]} ..
function(a,b,c)
    if type(a)~="number" then
        a=tonumber(a)
        if a==nil then return nil end
    end
    if b==nil then a,b=1,a end 
    if c==nil then c=1 end 
    local rv={}
    for i=a,b,c do table.insert(rv,i) end
    return rv
end


return _M

