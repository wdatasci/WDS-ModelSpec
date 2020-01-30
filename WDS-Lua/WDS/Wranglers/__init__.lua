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

--- A package of data wranglers for the WDS lua library.
-- @module WDS.Wranglers

local wds=require "WDS"

local module_name_dots=( ... or "main-call-without-args" )
local module_name="Wranglers"

local module_path=""
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
end

local _M={}
local _G=_G
_ENV=wds.EnvExtension(_M,_G)

info={name=module_name
    ,path=module_path
    , docmap={}
    ,doc=module_name .. " ("..module_path..")"..[==[
            A collection of data wranglers.
]==]
}

if module_name_dots=="main-call-without-args" or wds.bIsMain(table.pack(...)) then
    print("TODO")
end

return wds.EnvLock(_M)
