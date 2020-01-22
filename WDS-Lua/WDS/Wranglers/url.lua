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

local wds=require("WDS")
local wdsu=require("WDS.Util")
local pesc=require("WDS.Util.python_esc")

local __parent__="Wranglers"
local __name__="url"
local module_name=__parent__.."."..__name__
local module_path=""
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
end

local docstring=module_name .. " ("..module_path..")"..[==[
    A simple collection of tools for to add a few wget-like functionalities.

    ]==]

local isMain=wds.is_main(arg,module_name)
if isMain then
    print("test with "..__parent__.."/"..__name__.."_test.lua")
    print(docstring)
    os.exit()
end

local _M_G=_G
local _M_ENV={}
_ENV=_M_ENV

info={name=module_name
    ,path=module_path
    ,doc=docstring
    ,docmap={}
}


local AddToModuleHelp=function(tbl); tbl.info=info; return wds.AddToModuleHelp(tbl); end

local lcurl=_M_G.require "lcurl"


get=
AddToModuleHelp{
    get=[==[A wrapper for lcurl.easy which returns the input url.]==]
} ..
function(url,dlm)
    dlm=(dlm or "\n")
    local __data={}
    local __data_writer=function(line) _M_G.table.insert(__data,line) end
    lcurl.easy {url=url, writefunction=__data_writer} :perform()
    return _M_G.table.concat(__data,dlm)
end



return _M_ENV



