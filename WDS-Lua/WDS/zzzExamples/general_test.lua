
arg=nil
wds=require("WDS")
print(package.path)
wdsu=require("WDS.Util")

lcb=require("WDS.zzzExamples.lua_Couchbase_capi_minimal")
print("wds.show(lcb)")
print(wds.show(lcb));
print("wds.show(lua_Couchbase_capi_minimal)")
print(wds.show(lua_Couchbase_capi_minimal));
rc=lua_Couchbase_capi_minimal("couchbase://localhost/SEC","CJWypasek","CJWypasek","general_test_example",[[{
    "x":"huh","y":"what"
}]])
rc=lua_Couchbase_capi_minimal("couchbase://localhost/SEC","CJWypasek","CJWypasek","general_test_example2",[[{
"directory": {
"item": [
{
"last-modified": "2019-12-13 17:41:54",
"name": "0000950131-19-004146-index-headers.html",
"type": "text.gif",
"size": ""
},
{
"last-modified": "2019-12-13 17:41:54",
"name": "0000950131-19-004146-index.html",
"type": "text.gif",
"size": ""
},
{
"last-modified": "2019-12-13 17:41:54",
"name": "0000950131-19-004146.txt",
"type": "text.gif",
"size": ""
},
{
"last-modified": "2019-12-13 17:41:54",
"name": "sdart171absee_1212-0814.htm",
"type": "text.gif",
"size": "25457"
},
{
"last-modified": "2019-12-13 17:41:54",
"name": "sdart171ex102.xml",
"type": "text.gif",
"size": "122930977"
},
{
"last-modified": "2019-12-13 17:41:54",
"name": "sdart171ex103.xml",
"type": "text.gif",
"size": "23096"
}
],
"name": "hey",
"parent-dir": "/Archives/edgar/data/1696935"
}
}]])
print("rc=",rc)

print("fin")
q()

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




