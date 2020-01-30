--- Copyright 2018, 2019 Wypasek Data Science, Inc., released under the MIT open source license

--- A general testing script for a collection of modules.
-- Within WDS/zzzExamples.
-- @script general_test


arg=nil
wds=require("WDS")
print(package.path)
wdsu=require("WDS.Util")

-- Couchbase tests moved to WDS/Wranglers/Couchbase_test.lua

lua_swig_example1=require("WDS.zzzExamples.lua_swig_example1")
print("wds.show(lua_swig_example1)")
print(wds.show(lua_swig_example1))
print("dir(lua_swig_example1)")
print(dir(lua_swig_example1))

lua_capi_example1=require("WDS.zzzExamples.lua_capi_example1")
print("wds.show(lua_capi_example1)")
print(wds.show(lua_capi_example1))
print("dir(lua_capi_example1)")
print(dir(lua_capi_example1))
print("wds.show(l_dir(.))")
print(wds.show(l_dir(".")))

q()

print("lua_swig_example1.gcd(12345,800)=",lua_swig_example1.gcd(12345,800))
print("lua_swig_example1.gcd(12345,900)=",lua_swig_example1.gcd(12345,900))

lua_capi_example1=require("WDS.zzzExamples.lua_capi_example1")
print(wds.show(l_dir(".")))

print("wds.help(wds)")
print(wds.help(wds))

print("wds.dir()")
print(wds.dir())
print("wds.show_values(wds.dir())")
print(wds.show_values(wds.dir()))
print("wds.show(_G)")
print(wds.show(_G))
print("wds.show_values(_G)")
print(wds.show_values(_G))


print("wds.show_keys(_G)")
print(wds.show_keys(_G))
print("wds.show_keys(_G,1)")
print(wds.show_keys(_G,1))

print("testing locals")
local function f(a,b)
    local i=3
    local y=1043
    local x=wds.locals()
    return x
end

print("locals in f "..wds.show(debug.getinfo(f)))
print(wds.show(f(10,20)))
print("wds.show(wds.locals()))")
print(wds.show(wds.locals()))




