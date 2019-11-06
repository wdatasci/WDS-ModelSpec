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

--some python-esc things, especially for the WDS test code......

local wds=require("WDS")
local wdsu=require("WDS.Util")

local arg 

local module_name_dots=( ... or "main-call-without-args" )
-- to hard-code use.......
local module_name="WDS.Util.python_esc"

local module_path=debug.getinfo(1,"S").source

local mrv={}

-- 

mrv.info={name=module_name
    ,path=module_path
    ,doc=module_name .. " ("..module_path..")"..[==[
    A set of functions which mirror some of the python code
        (especially in the WDS test code)
    
    For example:
        x=list_range(l) will return the python equivalent of list(range(l))

    ]==]
}

--a python3-ish range iterator, but lua-ish in that end-points are inclusive
mrv.range=function(a,b,c) 
    if b==nil then a,b=1,a end 
    if c==nil then c=1 end 
    local _t={a,b,c,0,a-c} 
    return function(t, j) 
                _t[5]=_t[5]+_t[3]
                if _t[5]<=_t[2] then 
                    return _t[5] 
                end 
            end,_t,0 
end

mrv.list=function(f) local rv={} for v in (function () return f, {}, 0 end)()  do table.insert(rv,v) end return rv end


mrv.list_range=function(obj)
    if type(obj)~="number" then
        return nil
    end
    local rv={}
    for i=0,(tonumber(obj)-1),1 do
        table.insert(rv,i)
    end
    return rv
end


return mrv

