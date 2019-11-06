--Normal Lua comment
--[[
Block Comment
--]]

--[[
    1: Hello World
    2: importing modules
        -- see below with WDSUtil/WDS.lua
    3: debugging
        -- see below, not great, but a start
    4: argparse
        -- see below for a version of getopts
    5: exception handling
        -- see treatment with and without pcall for dump function below
--]]

-- require('debug')  -- not require'd to require

-- this simplest case

print("Hello World!")

-- see misc_tests.lua for odds and ends


-- for a basic modules example, we are using the base code in WDSUtil/WDS.lua
-- this requires ../?.lua on the LUA_PATH (this does allow WDSUtil.WDS to match WDSUtil/WDS.lua)

-- calling debug.debug() will allow and view of the stack....

print("use <return>cont<return> to continue....")

-- debug.debug()

wds=require("WDSUtil.WDS")

--wds is now a table "module"


print("use <return>cont<return> to continue....")
-- debug.debug()


X=3;

print(type("Hello world"))  --> string
print(type(10.4*3))         --> number
print(type(print))          --> function
print(type(type))           --> function
print(type(true))           --> boolean
print(type(nil))            --> nil
print(type(type(X)))        --> string

-- if not scoped elsewhere except in for-loop, i is local to the loop..

for i=1,10,2 do  -- start,stop[,step]
    print("i=",i)
end

for i=1,10 do; print("i=",i); end;

print("use <return>cont<return> to continue....")
-- debug.debug()

b={}

do; 
    -- local keyword can create local variable, even within an free do-end block
    --local a = {}     -- create a table and store its reference in `a'
    a = {}     -- create a table and store its reference in `a'
    local b=b  
    --since b and local b are references, but to a table/dictionary/record type, assignment inside still changes outside, unless local b is changed
    --b={}
    k = "x"
    a[k] = 10        -- new entry, with key="x" and value=10
    a[20] = "great"  -- new entry, with key=20 and value="great"
    print(a["x"])    --> 10
    k = 20
    print(a[k])      --> "great"
    a["x"] = a["x"] + 1     -- increments entry "x"
    print(a["x"])    --> 11
    b.hey="What"
    print(b.hey)
    print(b["hey"])
end;

print(a["x"])    --> 11
print(a.x)    --> 11
print(a[20])    --> 11
print(b.hey)

-- globals.lua
-- show all global variables

local seen={}

-- CJW: see note one page 82 of the 5.3 book, defining a 
-- local function that uses recursion might not compile 
-- correctly unless the recursive function (its variable/container) is declared local
-- before its assigned to a function that calls itself.
-- Otherwise the compilation resolves to the global namespace which 
-- might not be correct, i.e.,
--    local f
--    f=function (x) <<calls f()>>> end
--  (this is different than local f=function......)

-- this example without a pcall (protected mode call) will die
-- on the table.sort(s) call where the default sort comparison 
-- function cannot handle the mixture of string and integer keys
-- Continue to note below on dump_w_pcall
function dump_wo_pcall(t,i)
    seen[t]=true
    local s={}
    local n=0
    for k in pairs(t) do
        n=n+1
        s[n]=k
        -- print(n,k)
    end
    table.sort(s)
    -- local ok, msg = pcall(function () table.sort(s) end)
    for k,v in ipairs(s) do
        print(i,v)
        v=t[v]
        if type(v)=="table" and not seen[v] then
            dump_wo_pcall(v,i.."\t")
        end
    end
end

print("dump_wo_pcall(_G)")
-- dump_wo_pcall(_G,"")

seen={}

-- for dump_w_pcall, there are several ways to fix it,
-- with the first being just fixing the sort function....
function dump_w_pcall(t,i)
    seen[t]=true
    local caught_something=false
    local s={}
    local n=0
    for k in pairs(t) do
        n=n+1
        s[n]=k
        -- print(n,k)
    end
    -- solution 0, do not fix it....
    -- table.sort(s)
    -- solution 1, fix the sort with a comparison function that works for all keys....
    -- local ok, msg = pcall(function () table.sort(s, function (a,b) return tostring(a)<tostring(b) end ) end )
    -- solution 2, wrap the function in a protected mode call, if it does not work, carry on....
    --       note, uncomment the caught_something, error and return lines in the "if ok == false then" block below to cascade out the error.....
    local ok, msg = pcall(function () table.sort(s) end)
    print(tostring(ok))
    print(tostring(msg))
    if ok == false then
        print(">>>>>>>>>>>>>>>>>>>>>>> caught a failure <<<<<<<<<<<<<<")
        --[[
        caught_something=true
        error{code=3}
        return false
        --]]
    end
    for k,v in ipairs(s) do
        print(i,v)
        v=t[v]
        if type(v)=="table" and not seen[v] then
            local lrv=dump_w_pcall(v,i.."\t")
            if lrv == false then
                caught_something=true
                print(">>>>>>>>>>>>>>>>>>>>>>> caught a failure <<<<<<<<<<<<<<")
                error{code=2}
                return false
            end
        end
    end
    if caught_something then
        error{code=1}
    else
        return true
    end
end

print("local ok, msg= pcall(function() dump_w_pcall(_G) end)")
local ok, msg= pcall(function() return dump_w_pcall(_G,"") end)

if ok then
    print("completed successfully")
else
    print("not completed successfully, "..msg.code)
end

--standardized dump call
-- wds.dump(_G)

--using alt_getopt for argument parsing.....
--

getopt=require("alt_getopt")

--local opts,optind,optarg = getopt.get_ordered_opts(arg,"hab:c:",{hey="huh",verbos="v"})

print("wds.show(arg)")
wds.show(arg)

-- ok, the short options are all one string,
-- one letter for each, and those that take an
-- argument are followed by a colon :
-- The long options can either map to a short character or the expected number to follow
-- use a key like ['x-b']. no-* options to be processed later...

opts_rv1,opts_rv2 = getopt.get_opts(arg,"hvab:c:",{hey="b",verbose="v",other=1,['no-v']=0})
print(tostring(opts_rv1))
print(tostring(opts_rv2))
print("wds.show(opts_rv1)")
print(wds.show(opts_rv1))
print("wds.show(opts_rv2)")
print(wds.show(opts_rv2))
print("remaining args")
for i=opts_rv2,#arg do
    print("arg["..i.."]="..arg[i])
end







