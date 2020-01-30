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

--[[--
A general collection of scratch examples and local references.  These files are 
either self-sufficient or tests of the library.  There are often parallels with 
other WDS libraries, such as WDS-Python.

The zzz-name is solely for alphabetized sorting purposes.

@example WDS.zzzExamples

--]]--

-- the localizing of arg below shorts the global arg of a program that might require this module
local arg 

local module_name_dots=( ... or "main-call-without-args" )
-- to hard-code use.......
local module_name="Util"

local module_path=""
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
end


local mrv={}
local _M_G=_G

mrv.info={name=module_name
    ,path=module_path
    ,doc=module_name .. " ("..module_path..")"..[==[
    A general set of utilities to add the usual suspects to programs 
    and the interactive session.

    ]==]
    , docmap={}
}

if module_name_dots=="main-call-without-args" or wds.is_main(table.pack(...)) then
    print("testing in "..module_name)
    print("module_path "..module_path)
    print()
    print("help on "..module_name)
    print(wds.help(mrv))
    print()
    print("show(_G)")
    print(wds.show(_G))
    print(wds.show_keys(_G,1))
end


return mrv

