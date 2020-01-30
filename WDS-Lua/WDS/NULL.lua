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

--[[-- A base module that returns a NULL singleton.
--]]--
-- @classmod NULL

local _M={}

-- NULL singleton constructor

local NULL_Builder=function()
    local rv={} -- unless NULL_Builder is called again, will be the singular class instance
    return setmetatable(rv,{
        __tostring=function(a) return "NULL" end
        , __metatable=false
        , __call=function() return nil end
        , __eq=function(a,b)
            if type(a)=="table" and a.__classname__ and a.__classname__=="NULL" then
                if b==nil then 
                    return true 
                elseif type(b)=="table" then
                    if b.__class__ and b.__class__==a.__class__ then 
                        return true 
                    elseif b.__classname__ and b.__classname__=="NULL" then 
                        return true 
                    elseif b.__nil__ then 
                        return true 
                    end
                elseif type(b)=="number" then
                    return math.isinf(b) or math.isnan(b)
                elseif type(b)=="string" then
                    return b:len()==0
                end
            else
                if a==nil then 
                    return true 
                elseif type(a)=="table" then
                    if a.__class__ and a.__class__==rv then 
                        return true 
                    elseif a.__nil__ then 
                        return true 
                    end
                elseif type(a)=="number" then
                    return math.isinf(a) or math.isnan(a)
                elseif type(a)=="string" then
                    return a:len()==0
                end
            end
            return false
        end
        , __index=function(t,k)
            if k=="__class__" then 
                return rv 
            elseif k=="__classname__" then 
                return "NULL"
            end
        end
        , __newindex=function(t,k,v) error("Cannot change anything about a NULL singleton") end
        })
end

--- A NULL singleton
-- @type NULL
_M.NULL=NULL_Builder()

return setmetatable({},{__index=_M
    ,__newindex=function(t,k,v) error("Error NULL Module, cannot change values in the module.") end
    ,__metatable=false
})

