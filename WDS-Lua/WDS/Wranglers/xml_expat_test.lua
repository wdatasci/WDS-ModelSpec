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
xml_expat=require("WDS.Wranglers.xml_expat")

local args_opts=require("WDS.Util.args_opts")
options=args_opts.ArgumentParser('usual')

options:add_argument{name="file"
    , hasArgument=true
    , help="optional argument to run parser on a test file"
    , default="" 
    }

opts_rv1, opts_rv2=options:parse(arg)

if opts_rv1.help then
    options:help()
    print()
    print("Module help()")
    print(wds.help(wjson))
    os.exit()
end

print("options=",options:show())
print("arg=",wds.show(arg))
print("wds.show(opts_rv1)=",wds.show(opts_rv1))
print("wds.show(opts_rv2)=",wds.show(opts_rv2))

print("wds.dir()=",wds.show(wds.dir()))

if opts_rv1.file and string.len(opts_rv1.file)>0 then
    fd=io.open(opts_rv1.file,"r")
    fd_xml=fd:read("*all")
    fd:close()
    rc,fd_xml_parsed,msg=xml_expat.base_parse(fd_xml,"UTF-8")
    --print("fd_xml=",fd_xml)
    print("rc=",rc,"\nfd_xml_parsed=")
end



x=[==[<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<RowSet X="hey" huh="what">
    <Row>
        <x>1.2</x>
        <y>hey</y>
    </Row>
    <Row>
        <x>4.5</x>
        <y>stuff</y>
        <!--   
            internal notes
            second line -->
    </Row>
</RowSet>
]==]

print("x=",x)

rc,d,msg=xml_expat.base_parse(x)
print("rc=",rc,", type(d)=",type(d),", d=",wds.show(d))

x=[==[<Row>3</Row>]==]

print("x=",x)

rc,d,msg=xml_expat.base_parse(x)
print("rc=",rc,", type(d)=",type(d),", d=",wds.show(d))


x=[==[<?xml version="1.0" encoding="Windows-1252"?>
<assetData xmlns="http://www.sec.gov/edgar/document/absee/autoloan/assetdata" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <assets>
    <assetTypeNumber>Sponsor Assigned</assetTypeNumber>
    <assetNumber>XXX</assetNumber>
    <reportingPeriodBeginningDate>12-01-2019</reportingPeriodBeginningDate>
    <reportingPeriodEndingDate>12-31-2019</reportingPeriodEndingDate>
    <originatorName>YYYY</originatorName>
    <originationDate>08/2014</originationDate>
    <originalLoanAmount>32000.00</originalLoanAmount>
  </assets>
</assetData>
]==]


print("x=",x)

d=xml_expat.XML(x)
print("type(d)=",type(d),", xml_expat.bIsXML(d)=",xml_expat.bIsXML(d),", d=",wds.show(d))

for i,v in d:children() do
    print("i=",i,", v=",v)
end

for i,v in d:children() do
    print("i,v=",i,v,xml_expat.bIsXML(v))
    for ii,vv in v:children() do
        print("ii,vv=",ii,vv,xml_expat.bIsXML(vv))
        for iii,vvv in vv:children() do 
            print("iii,vvv=",iii,vvv,xml_expat.bIsXML(vvv),wds.show(vvv,{hidden=true})) 
        end
    end
end



