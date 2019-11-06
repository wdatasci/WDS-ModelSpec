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

--[[ a Python-argsparse-like object --]]

local wds=require("WDS")
local wdsu=require("WDS.Util")

local module_name="WDS.Util.args_opts"
local is_main=wds.is_main(arg,module_name)
if is_main then
    print("test with WDS.Util/args_opts_test")
end

local module_path=""
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
end

local getopt=require("alt_getopt")

-- switching the ENV for this module, accessing globals through _M_G
local _M_G=_G
local _M_ENV={}
_ENV=_M_ENV

local ArgumentParser_MTI={}

ArgumentParser_MTI.add_argument=function(self,...)
    _M_G.table.insert(self,{...})
end

ArgumentParser_MTI.parse=function (self,args)
    local shortargs
    shortargs=""
    local longargs
    longargs={}
    local short_to_name={}
    local short_to_name_negatible={}
    local word_to_name_negatible={}
    for i,o in _M_G.ipairs(self) do
        o=o[1]
        -- _M_G.print("i,o=",i,wds.show(o))

        if o.short then
            shortargs=shortargs .. o.short
            if o.hasArgument then
                shortargs=shortargs .. ":"
            end
            longargs[o.name]=o.short
            short_to_name[o.short]=o.name
            if o.aliases then
                for j,vj in _M_G.ipairs(o.aliases) do
                    longargs[vj]=o.short
                end
            end

        else
            if o.hasArgument then
                longargs[o.name]=1
            else
                longargs[o.name]=0
            end
            if o.aliases then
                for j,vj in _M_G.ipairs(o.aliases) do
                    longargs[vj]=o.name
                end
            end
        end

        if o.short_negatible then
            shortargs=shortargs .. o.short_negatible
            short_to_name_negatible[o.short_negatible]=o.name
        end

        if o.negatible then
            if o.short_negatible then
                longargs["no-"..o.name]=o.short_negatible
                if o.aliases then
                    for j,vj in _M_G.ipairs(o.aliases) do
                        longargs["no-"..vj]=o.short_negatible
                    end
                end
                if o.aliases_negatible then
                    for j,vj in _M_G.ipairs(o.aliases_negatible) do
                        longargs[vj]=o.short_negatible
                    end
                end
            else
                longargs["no-"..o.name]=0
                word_to_name_negatible["no-"..o.name]=o.name
                if o.aliases then
                    for j,vj in _M_G.ipairs(o.aliases) do
                        longargs["no-"..vj]="no-"..o.name
                    end
                end
                if o.aliases_negatible then
                    for j,vj in _M_G.ipairs(o.aliases_negatible) do
                        longargs[vj]="no-"..o.name
                        word_to_name_negatible[vj]=o.name
                    end
                end
            end
        end

    end
    -- _M_G.print("args=",wds.show(args))
    -- _M_G.print("shortargs=",shortargs)
    -- _M_G.print("longargs=",wds.show(longargs))
    --local opts_rv1, opts_rv2=getopt.get_opts(args,shortargs,longargs)
    local opts_rv1, opts_rv2, opts_rv3 =getopt.get_ordered_opts(args,shortargs,longargs)
    -- _M_G.print("opts_rv1=",wds.show(opts_rv1))
    -- _M_G.print("opts_rv2=",wds.show(opts_rv2))
    -- _M_G.print("opts_rv3=",wds.show(opts_rv3))
    local rv={}
    for i,o in _M_G.ipairs(self) do
        if o[1].default ~= nil then
            rv[o[1].name]=o[1].default
        end
    end
    for i,o in _M_G.pairs(opts_rv1) do
        if short_to_name[o] then
            if rv[short_to_name[o]]==true or rv[short_to_name[o]]==false then
               rv[short_to_name[o]]=true
            end
            if opts_rv3[i] then
               rv[short_to_name[o]]=opts_rv3[i]
            end
        elseif short_to_name_negatible[o] then
            if rv[short_to_name_negatible[o]]==true or rv[short_to_name_negatible[o]]==false then
                rv[short_to_name_negatible[o]]=false
            end
            if opts_rv3[i] then
                rv[short_to_name_negatible[o]]=opts_rv3[i]
            end
        elseif word_to_name_negatible[o] then
            if rv[word_to_name_negatible[o]]==true or rv[word_to_name_negatible[o]]==false then
                rv[word_to_name_negatible[o]]=false
            end
            if opts_rv3[i] then
                rv[word_to_name_negatible[o]]=opts_rv3[i]
            end
        else
            if opts_rv3[i] then
                rv[o]=opts_rv3[i]
            end
        end
    end
    local rv_remaining={}
    local j=0
    for i=opts_rv2,#args do
        j=j+1
        rv_remaining[j]=args[i]
    end
    return rv, rv_remaining
end

ArgumentParser_MTI.show=function(self)
    local usual_suspects={"name", "help", "aliases", "short", "hasArgument", "default", "negatible", "short_negatible", "aliases_negatible"}
    for ia,a in _M_G.ipairs(self) do
        --_M_G.print(wds.show(a[1]))
        local seen={}
        _M_G.print("Argument",ia)
        for ib,b in _M_G.ipairs(usual_suspects) do
            if a[1][b] then
                _M_G.print("   ",b,wds.show(a[1][b]))
                seen[b]=true
            end
        end
        for ib,b in _M_G.pairs(a[1]) do
            if seen[ib]==nil then
                _M_G.print("   ",ib,b)
            end
        end
    end
end

ArgumentParser_MTI.help=function(self,obj)
    if obj and obj.info and obj.info.doc then
        _M_G.print(obj.info.doc)
    end
    _M_G.print("Arguments:")
    ArgumentParser_MTI.show(self)
end



ArgumentParser=function(obj)
    local rv={}
    if obj then
        if _M_G.type(obj)=="string" then
            _M_G.assert(obj=="usual","ArgumentParser can only be called ArgumentParser() or ArgumentParser('usual')")
            ArgumentParser_MTI.add_argument(rv,{name="help",short="h",help="USAGE:",negatible=true,default=false})
            ArgumentParser_MTI.add_argument(rv,{name="debug",short="d",help="Sets debug flags",negatible=true,default=false})
        end
    end
    return _M_G.setmetatable(rv,{__index=ArgumentParser_MTI})
end


return _M_ENV


