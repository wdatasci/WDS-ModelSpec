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

--- A simple collection of tools for to add a few wget-like functionalities.
-- @submodule WDS.Wranglers
-- @within WDS.Wranglers

local wds=require("WDS")
local wdsu=require("WDS.Util")
local pesc=require("WDS.Util.python_esc")
local lcurl=require "lcurl"

local __parent__="Wranglers"
local __name__="url"
local module_name=__parent__.."."..__name__
local module_path=""

local docstring=module_name .. " ("..module_path..")"..[==[
    A simple collection of tools for to add a few wget-like functionalities.
]==]

local dbg
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
    dbg=require("debugger")
    dbg.auto_where=2
else
    dbg=function() end
end

if wds.bIsMain(table.pack(...),module_name) then
    print("test with "..__parent__.."/"..__name__.."_test.lua")
    print(docstring)
    os.exit()
end

local _M={}
local _G=_G
_ENV=wds.EnvExtension(_M,_G)

info={name=module_name
    ,path=module_path
    ,doc=docstring
    ,docmap={}
}

local AddToModuleHelp=function(tbl); tbl.info=info; return wds.AddToModuleHelp(tbl); end


get=AddToModuleHelp{
    get=[==[--[[--
            A wrapper for lcurl.easy which returns the input url.
--]]--]==]
-- @function get
} ..
function(url,dlm)
    dlm=(dlm or "\n")
    local __data={}
    local __data_writer=function(line) table.insert(__data,line) end
    lcurl.easy {url=url, writefunction=__data_writer} :perform()
    return table.concat(__data,dlm)
end

pcall_get=AddToModuleHelp{
    pcall_get=[==[--[[--
            A pcall wrapper for lcurl.easy which returns the input url.
            Returns true if successful, nil otherwise.
            The second argument, rv, is a by-reference for the return value, placed in rv[1].
--]]--]==]
-- @function get
} ..
function(url,rv,dlm)
    dlm=(dlm or "\n")
    local rc,lrv=pcall(get,url,dlm)
    if rc then
        rv[1]=lrv
        return true
    else
        rv[1]=lrv
        return nil
    end
end


return wds.EnvLock(_M)



