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
-- Couchbase_localhost_credentials={user="AAAAAA", password="AAAAAA"}

load(io.open("/home/"..os.getenv("USER").."/Couchbase_localhost_credentials.lua","r"):read("*all"))()
cb_cred=Couchbase_localhost_credentials

print("input Couchbase user > (default: "..cb_cred.user..")")
user=io.read("*l")
if #user==0 then
    user=cb_cred.user
end
print("input Couchbase password > (default from /home/"..os.getenv("USER").."/Couchbase_localhost_credentials.lua)")
password=io.read("*l")
if #password==0 then
    password=cb_cred.password
end

server_address="couchbase://localhost/SEC"
print("input Couchbase server address > (default: "..server_address..")")
s=io.read("*l")
if #s>0 then
    server_address=s
end

doc_name="general_test_example"
print("input Couchbase target document name> (default: "..doc_name..")")
d=io.read("*l")
if #d>0 then
    doc_name=d
end

rc = o << {hey="what"}

rc,rv=Couchbase_CAPI_store(server_address,user,password,doc_name,tostring(o))
print("store rc=",rc," rv=",rv)

rc,rv=Couchbase_CAPI_get(server_address,user,password,doc_name)
print("get rc=",rc," rv=",rv)


