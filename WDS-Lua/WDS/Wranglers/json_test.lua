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

--- A test of WDS.Wranglers.json
-- @within WDS.Wranglers
-- @script json_test


local wds=require("WDS")
local wdsu=require("WDS.Util")
local pesc=require("WDS.Util.python_esc")
wjson=require("WDS.Wranglers.json")

local args_opts=require("WDS.Util.args_opts")
options=args_opts.ArgumentParser('usual')
opts_rv1, opts_rv2=options:parse(arg)
if opts_rv1.help then
    options:help()
    print()
    print("Module help()")
    print(wds.help(wjson))
    os.exit()
end



x=wjson.JSON(wjson.jtype.array)
rc=x << 3
rc=x << 3
print(wds.show(x))


z=wds.deeper_copy(x)
print(wds.show(z))

--setmetatable(x,nil)
z=wds.deeper_copy(x)
print(wds.show(x))
print(wds.show(z))


a=wjson.JSON()
b=wds.deeper_copy(a)
rc= a << {x=1,y=3}
rc= b << {c=3,l=20,b=a}

c=wds.show(x,{hidden=true,maxdepth=10,linesep="\n",itemsep=",",indent="    "})
--c=wds.__show_str__(ca,"   ")


--print(wds.show(x.data))
--z=wds.deeper_copy(x.data)
--print(wds.show(z))


a=[==[    
  {
    "d" : [
        { 
            "size" : "",
            "name" : "hey"
        },
        {
            "size" : "10",
            "name" : "huh"
        }
        ],
    "name" : "other",
    "x" : 20,
    "b" : false
}

]==]

print("x=",wds.show(x))
b=wjson.JSON(x)
print("b=wjson.JSON(x)=",wds.show(b))
b=wds.deeper_copy(x)
print("b=wds.deeper_copy(x)=",wds.show(b))

b=wjson.JSON(wjson.jtype.boolean)
print("b=wjson.JSON(wjson.jtype.boolean)=",wds.show(b))

b=wjson.JSON(a)
print("b=wjson.JSON(a)=",wds.show(b))

c=wjson.parse(a)

print("c=",c)

c=wjson.JSON({1,5})
print("c=",c)


c=wjson.JSON({a=1,b=5})
print("c=",c)

rc= c << {z=10}
print("c=",c)




print("a=","||"..a.."||")
print("wds.trim(a)=","||"..wds.trim(a).."||")

print()

b=wjson.parse(a)

print("b=",b)
print()
print("b=",wds.show(b))
for i,v in pairs(b) do
    print("i=",i," v=",wds.show(v))
end
print()

aa=" \"hey\" "
c=wjson.parse(aa)
print("aa=",aa)
print("c=",wds.show(c))
aa=" -1.34 "
c=wjson.parse(aa)
print("aa=",aa)
print("c=",wds.show(c))
aa=" false "
c=wjson.parse(aa)
print("aa=",aa)
print("c=",wds.show(c))
aa=" null "
c=wjson.parse(aa)
print("aa=",aa)
print("c=",wds.show(c))


aa=[==[ [1, 3, 4.5   

    , "Hey"

] 


]==]

print("aa=",aa)
c=wjson.parse(aa)
print("c=",wds.show(c))


aa=[==[ [1, 3, 4.5   

    , "Hey"

] 


]==]

print("aa=",aa)
c=wjson.parse(aa)
print("c=",wds.show(c))






