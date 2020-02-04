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

--- A test of WDS.Wranglers.Couchbase
-- @within WDS.Wranglers
-- @script Couchbase_test


wds=require("WDS")
wdsu=require("WDS.Util")
pesc=require("WDS.Util.python_esc")
lcb=require("WDS.Wranglers.Couchbase")
wjson=require("WDS.Wranglers.json")
args_opts=require("WDS.Util.args_opts")
url=require("url")

options=args_opts.ArgumentParser('usual')

options:add_argument{name="fetch"
, short="f"
, help="(true) fetch the test url or (false) read from file"
, default=false
}

p=string.sub(wds.info.path,1,#wds.info.path-7) -- removing WDS.lua
if wds.string_startswith(p,"@") then
    p=string.sub(p,2)
end
p=p.."WDS/zzzExamples/output/tmp.txt"

options:add_argument{name="targetfile"
, short="t"
, help="target file for the fetched url"
, default=p
}

opts_rv1, opts_rv2=options:parse(arg)
if opts_rv1.help then
    options:help()
    print()
    print("Module help()")
    print(wds.help(lcb))
    os.exit()
end


u="https://www.sec.gov/Archives/edgar/data/1696935/000095013119004146/index.json"
print("URL u=",u)

if opts_rv1.fetch then
    a=url.get(u)
    fd=io.open(opts_rv1.targetfile,"w")
    fd:write(a)
    fd:close()
else
    fd=io.open(opts_rv1.targetfile,"r")
    a=fd:read()
end
    
print("a=",wds.show(a))

o=wjson.JSON(a)

-- Note: CJW - For a local credential file to simplify the test, 
-- on WSL/ubuntu, a file in my home directory has
-- Couchbase__credentials.localhost={host="localhost",user="AAAAAA", password="AAAAAA",bucket="AAAAAA"}
-- ...others...
-- Couchbase_credentials.default=Couchbase_credentials.localhost

cb_cred=load(io.open("/home/"..os.getenv("USER").."/Couchbase_credentials.lua","r"):read("*all"))()

print("input Couchbase user > (default: "..cb_cred.default.user..")")
user=io.read("*l")
if #user==0 then
    user=cb_cred.default.user
end
print("input Couchbase password > (default from /home/"..os.getenv("USER").."/Couchbase_localhost_credentials.lua)")
password=io.read("*l")
if #password==0 then
    password=cb_cred.default.password
end

server_address="couchbase://"..cb_cred.default.host
print("input Couchbase server address > (default: "..server_address..")")
s=io.read("*l")
if #s>0 then
    server_address=s
end

bucket=cb_cred.default.bucket
print("input Couchbase bucket > (default: "..bucket..")")
b=io.read("*l")
if #b>0 then
    bucket=b
end

doc_name="general_test_example"
print("input Couchbase target document name> (default: "..doc_name..")")
d=io.read("*l")
if #d>0 then
    doc_name=d
end

rc = o << {hey="what"}

rc,rv=Couchbase_CAPI_store(server_address,bucket,user,password,doc_name,tostring(o))
print("store rc=",rc," rv=",rv)

rc = o << {hey="what",huh="hey"}

rc,rv=Couchbase_CAPI_store(server_address,bucket,user,password,doc_name.."2",tostring(o))
print("store rc=",rc," rv=",rv)

rc,rv,rv2,rv3=Couchbase_CAPI_get(server_address,bucket,user,password,doc_name)
print("get rc=",rc," rv=",rv," rv2=",rv2," rv3=",rv3)

rc,rv,rv2=Couchbase_CAPI_query(server_address,bucket,user,password,"select * from `SEC` where hey=$1 ","\"what\"")
print("get rc=",rc," rv=",rv," rv2=",rv2)

rc,rv,rv2=Couchbase_CAPI_query(server_address,bucket,user,password,"select * from `SEC` where hey=\"what\"")
print("get rc=",rc," rv=",rv," rv2=",rv2)


