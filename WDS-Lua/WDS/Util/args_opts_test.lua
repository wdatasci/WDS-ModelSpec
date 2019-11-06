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

local arg=arg or table.pack(...)
local is_main=wds.is_main(arg)
print("is_main=",is_main)
print("arg=",wds.show(arg))

local args_opts=require("WDS.Util.args_opts")

if is_main then
    
    -- options=args_opts.ArgumentParser()
    options=args_opts.ArgumentParser('usual')

    -- print("options=",wds.show(options))
    -- print("options=",options:show())
    -- print("options.MT=",wds.show(getmetatable(options)))
    -- print("options.MT.__index=",wds.show(getmetatable(options).__index))

    print("try: lua " .. arg[0] .. " --help")
    print("try: lua " .. arg[0] .. " -h")
    --[[
    options:add_argument{name="help"
            , short="h"
            , help="USAGE:"
            , negatible=true
            , default=false
    }
    --]]

    options:add_argument{name="path_of_target_directory"
            , hasArgument=true
            , help="first argument, path of target directory"
            , default=""
    }

    options:add_argument{name="glob_pattern"
            , hasArgument=true
            , help="optional argument for unix-like glob pattern (watch escaping when using p_m)"
            , default="" --{__nil__=true}
    }

    options:add_argument{name="CaseInsensitive"
            , short="i"
            , short_negatible="I"
            , aliases={"case-insensitive"}
            , aliases_negatible={"CaseSensitive","case-sensitive"}
            , help="optional argument, for case insensitive"
            , negatible=true
            , default=true
    }
   
    options:add_argument{name="recursive"
            , short="r"
            , help="optional argument, for recursive flag for glob"
            , negatible=true
            , default=true 
    }
    
    --[[
    options:add_argument{name="debug"
            , aliases={"pudb"}
            , help="turn on the debugging info"
            , negatible=true
            , default=false
    }
    --]]
    
    opts_rv1, opts_rv2=options:parse(arg)
    if opts_rv1.help then
        options:help()
        os.exit()
    end
    print("options=",options:show())
    print("arg=",wds.show(arg))
    print("wds.show(opts_rv1)=",wds.show(opts_rv1))
    print("wds.show(opts_rv2)=",wds.show(opts_rv2))


end


