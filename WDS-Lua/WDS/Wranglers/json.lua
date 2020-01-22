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
local pesc=require("WDS.Util.python_esc")
local wdsm=require("WDS.Comp.Matrix")

local __parent__="Wranglers"
local __name__="json"
local module_name=__parent__.."."..__name__
local module_path=""

local dbg
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
    dbg=require("debugger")
    dbg.auto_where=2
else
    dbg=function() end
end

local docstring=module_name .. " ("..module_path..")"..[==[
    A pure-lua simple implementation of a few json utilities.
    ]==]

local isMain=wds.is_main(arg,module_name)
if isMain then
    print("test with "..__parent__.."/"..__name__.."_test.lua")
    print(docstring)
    os.exit()
end

--for localizing the module environment:
--  using wds.EnvExtension to pass unknown __index lookups to _G but place new free names into _M
--  return _M at the end of the module

local _M={}
local _G=_G
_ENV=wds.EnvExtension(_M,_G)

--to use with out prefix....
bIsHiddenFieldName=wds.bIsHiddenFieldName
NULL=wdsm.NULL
NaN=wds.NaN

--this module's info table for use with wds.help
info={name=module_name
    ,path=module_path
    ,doc=docstring
    ,docmap={}
}

--localizing AddToModuleHelp to globally assign to this module's info table
local AddToModuleHelp=function(tbl,tbl2); tbl.info=info; return wds.AddToModuleHelp(tbl,tbl2); end

--And EnumLike object for a json value type
jtype=
AddToModuleHelp{
    jtype=[==[An EnumLike object of json value types.]==]
} ..  wds.EnumLike{ 
      unk=0
    , object=1
    , array=2
    , number=3
    , string=4
    , boolean=5  -- true and false are not enumerated separately as they are lua keywords
    , null=6
    , __classname__="jtype"
}
__jtype_obj=jtype.__objref__

bIsWSP=
AddToModuleHelp{
    bIsWSP=[==[A check to see if a single character input is json whitespace.]==]
} ..
function(arg)
    if type(arg)~="string" and string.len(arg)~=1 then 
        return false
    end
    local c=utf8.codepoint(arg)
    if type(c)=="table" then
        c=c[1]
    end
    if wds.bIn(c,9,10,11,12,13,32,133,160,5760) then
        return true
    elseif 8192<=c and c<=8202 then
        return true
    elseif wds.bIn(c,8232,8233,8239,8287,12288) then
        return true
    end
    return false
end

-- The metatable and __index function for a json value
local __JSON_class__={}
local __JSON_class__index_base={}

-- A JSON value class in lua
-- data and keys are ordered to preserve input structure
local __JSON_prototype__={
    data=nil            -- data will be used for atoms, objects and arrays
    , keys=nil          -- keys and keys_rev will only be used for objects
    , keys_rev=nil
    , jtype=jtype.unk
    , __parent__=nil    -- for tree structures and assignments
}

bIsJSON=
AddToModuleHelp{
    bIsJSON=[==[A boolean check for argument as a JSON instance.]==]
} .. function(a)
    if a==nil then return false end
    if type(a)~="table" then return false end
    if a.__class__==nil then return false end
    if jtype.bIsValid(a.jtype) and a.__class__==__JSON_class__ then return true end
    return false;
end

bIsJTypeUnk=function(a) return a==jtype.unk end
bIsJTypeBoolean=function(a) return a==jtype.boolean end
bIsJTypeNULL=function(a) return a==jtype.null end
bIsJTypeLiteralNameToken=function(a) return wds.bIn(a,jtype.boolean,jtype.null) end
bIsJTypeAtom=function(a) return wds.bIn(a,jtype.string,jtype.number,jtype.boolean,jtype.null) end
bIsJTypeArray=function(a) return a==jtype.array end
bIsJTypeObject=function(a) return a==jtype.object end

bIsJSONUnk=function(a) return (bIsJSON(a)) and bIsJTypeUnk(a.jtype) end
bIsJSONBoolean=function(a) return (bIsJSON(a)) and bIsJTypeBoolean(a.jtype) end
bIsJSONNULL=function(a) return (bIsJSON(a)) and bIsJTypeNULL(a.jtype) end
bIsJSONLiteralNameToken=function(a) return (bIsJSON(a)) and bIsJTypeLiteralNameToken(a.jtype) end
bIsJSONAtom=function(a) return (bIsJSON(a)) and bIsJTypeAtom(a.jtype) end

--Predefines are for use within other functions before they are defined.
--Note:  AAA_insert inserts variable type argument into a type AAA self.
--       insert_AAA inserts a type AAA argument into variable type self.
local __JSON_new__=function()end
local __JSON_new_object__=function()end
local __JSON_new_array__=function()end
local __JSON_new_raw__=function()end
local __JSON_new_string__=function()end
local __JSON_new_number__=function()end
local __JSON_new_boolean__=function()end
local __JSON_new_null__=function()end
local __JSON_new_unk__=function()end

local __JSON_new_object__raw__=function()end
local __JSON_new_array__raw__=function()end
local __JSON_new_atom__raw__=function()end
local __JSON_new_string__raw__=function()end
local __JSON_new_number__raw__=function()end
local __JSON_new_boolean__raw__=function()end
local __JSON_new_unk__raw__=function()end

local __JSON_parse__=function()end
local __JSON_parse_value__=function()end
local __JSON_copy__=function()end
local __JSON_empty__=function()end
local __JSON_array_empty__=function()end
local __JSON_object_empty__=function()end
local __JSON_repoint__=function()end
local __JSON_repoint__raw__=function()end

local __JSON_null_insert__=function()end
local __JSON_boolean_insert__=function()end
local __JSON_number_insert__=function()end
local __JSON_string_insert__=function()end
local __JSON_atom_insert__=function()end
local __JSON_array_insert__raw__=function()end
local __JSON_object_insert__raw__=function()end
 
local __JSON_insert__=function()end
local __JSON_insert_null__=function()end
local __JSON_insert_null__raw__=function()end
local __JSON_insert_boolean__=function()end
local __JSON_insert_number__=function()end
local __JSON_insert_string__=function()end
local __JSON_insert_atom__=function()end
local __JSON_insert_atom__raw__=function()end
local __JSON_insert_array__=function()end
local __JSON_insert_object__=function()end

local __JSON_parse__=function()end
local __JSON_parse_value__=function()end
local __parse_move_to_next_non_WSP=function()end

local __JSON_class_____shl
local __JSON_class_____tostring

--The suffix 'raw__' will be used here for functions without argument assertions which 
--are redundant in functions where argument assertions have already been performed.
--The unk, null, true, and false constructors are raw__ trivially.

__JSON_new_unk__=function(__parent__) return setmetatable({jtype=jtype.unk,__parent__=__parent__},__JSON_class__) end
__JSON_new_null__=function(__parent__) return setmetatable({jtype=jtype.null,__parent__=__parent__},__JSON_class__) end
__JSON_new_true__=function(__parent__) return setmetatable({data=true,jtype=jtype.boolean,__parent__=__parent__},__JSON_class__) end
__JSON_new_false__=function(__parent__) return setmetatable({data=false,jtype=jtype.boolean,__parent__=__parent__},__JSON_class__) end

__JSON_new_boolean__raw__=function(arg,__parent__) return setmetatable({data=(arg==true),jtype=jtype.boolean,__parent__=__parent__},__JSON_class__) end
__JSON_new_number__raw__=function(arg,__parent__) return setmetatable({data=arg,jtype=jtype.number,__parent__=__parent__},__JSON_class__) end
__JSON_new_string__raw__=function(arg,__parent__) return setmetatable({data=arg,jtype=jtype.string,__parent__=__parent__},__JSON_class__) end
__JSON_new_atom__raw__=function(arg,arg2,__parent__) return setmetatable({data=arg,jtype=arg2,__parent__=__parent__},__JSON_class__) end
__JSON_new_array__raw__=function(__parent__) return setmetatable({data={},jtype=jtype.array,__parent__=__parent__},__JSON_class__) end
__JSON_new_object__raw__=function(__parent__) return setmetatable({data={},keys={},keys_rev={},jtype=jtype.object,__parent__=__parent__},__JSON_class__) end

--a simple repointing of fields
__JSON_repoint__raw__=function(self,arg,opts)
    __JSON_empty__(self)
    self.data=arg.data
    if wds.bIn(arg.jtype,jtype.object,jtype.array) then 
        local k,v
        for k,v in ipairs(arg.data) do
            v.__parent__=self
        end
    end
    self.keys=arg.keys
    self.keys_rev=arg.keys_rev
    self.jtype=arg.jtype
    --__parent__ does not get reassigned
    if opts~=nil then
        local k,v
        for k,v in opts do
            rawset(self,k,v)
        end
    end
    return self
end

__JSON_array_empty__=function(self)
    __JSON_empty__(self)
    self.data={}
    self.jtype=jtype.array
end

__JSON_array_insert__raw__=function(self,arg,karg,opts)
    if self.data==nil then
        __JSON_array_empty__(self)
    end
    if karg~=nil then
        if type(karg)~="number" then
            error("Error JSON: inserts into arrays have to have nil or numeric keys")
        elseif karg<=0 or ((self.data~=nil) and (karg>(#self.data)+1)) then
            error("Error JSON: inserts into arrays must indices in 1..(#self.data+1)")
        end
    end
    if arg==nil or arg==NULL then --inserting a json null
        local self_data=rawget(self,"data")
        assert((karg==nil) or ( (karg>=1) and (karg<=(#self_data)+1) ),"Error JSON: inserts into arrays must have nil or valid integer key.")
        if karg==nil or karg==#self_data then
            table.insert(self_data,__JSON_new_null__())
            self_data[#self_data].__parent__=self
        else
            self_data[karg]=__JSON_new_null__()
            self_data[karg].__parent__=self
        end
    elseif bIsJSON(arg) then
        local self_data=rawget(self,"data")
        assert((karg==nil) or ( (karg>=1) and (karg<=(#self_data)+1) ),"Error JSON: inserts into arrays must have nil or valid integer key.")
        if karg==nil or karg==#self.data then
            table.insert(self_data,wds.deeper_copy(arg,{special_handling={__parent__=true}},{__parent__=self}))
        else
            self_data[karg]=wds.deeper_copy(arg,{special_handling={__parent__=true}},{__parent__=self})
        end
    else
        local self_data=rawget(self,"data")
        if self_data==nil then
            __JSON_array_empty__(self)
        end
        assert((karg==nil) or ( (karg>=1) and (karg<=(#self_data)+1) ),"Error JSON: inserts into arrays must have nil or valid integer key.")
        local targ=type(arg)
        if wds.bIn(targ,"boolean","number","string") then
            if karg==nil or karg==#self_data then
                table.insert(self_data,__JSON_new_atom__raw__(arg,jtype(targ)))
                self_data[#self_data].__parent__=self
            else
                self_data[karg]=__JSON_new_atom__raw__(arg,jtype(targ))
                self_data[karg].__parent__=self
            end
        elseif targ=="table" then -- insert integer indexed values
            local i,v
            for i=1,#arg,1 do
                v=arg[i]
                __JSON_array_insert__raw__(self,v)
            end
        else
            error("Error JSON: unknown insert type into array json value")
        end
    end
    return self
end

__JSON_object_empty__=function(self)
    __JSON_empty__(self)
    self.data={}
    self.keys={}
    self.keys_rev={}
    self.jtype=jtype.object
end

__JSON_object_insert__raw__=function(self,arg,karg)
    if self.data==nil or self.keys==nil or self.keys_rev==nil then
        if self.data then
            print("Warning JSON: insertion attempt into object with incorrect structure, object data is emptied first")
        end
        __JSON_object_empty__(self)
    end

    local v
    local foundarray=false
    local foundobject=false
    local targ=type(arg)

    if arg==nil or arg==NULL then

        v=__JSON_new_null__()

    elseif bIsJSON(arg) then

        if karg==nil then
            if arg.jtype==jtype.object then -- insert key-values one at a time
                local i,k,v
                for k,i in pairs(arg.keys) do
                    v=arg.data[i]
                    __JSON_object_insert__raw__(self,v,k)
                end
                return self
            else
                error("Error JSON: inserts into objects require keys")
            end
        end

        v=wds.deeper_copy(arg,{special_handling={__parent__=true}},{__parent__=self})

    elseif targ=="table" then

        local n,n1,n2,nh
        n,n1,n2,nh=wds.length(arg)
        assert(n1==0 or n2==0,"Error JSON: converting a table into an array or object must be either have #arg==0 for an object or only have keys 1..#arg for an array.")
        if n1>0 then -- found array, only take indexed entries
            if karg==nil then
                error("Error JSON: inserts into an object require keys.")
            end
            foundarray=true
            v=__JSON_new_array__(arg)
        else
            foundobject=true

            v=__JSON_new_object__raw__()
            if karg==nil then
                local kk,vv
                for kk,vv in pairs(arg) do
                        __JSON_object_insert__raw__(self,vv,kk)
                end
                return self
            else
                local kk,vv
                for kk,vv in pairs(arg) do
                        __JSON_object_insert__raw__(v,vv,kk)
                end
            end

        end

    elseif wds.bIn(targ,"boolean","string","number") then

        v=__JSON_new_atom__raw__(arg,jtype(targ))

    else

        error("Error JSON: internal error")

    end

    v.__parent__=self

    assert(karg~=nil,"Error JSON: inserts into objects require keys")
    local keyi=self.keys[karg]
    if keyi==nil then
        table.insert(rawget(self,"data"),v)
        table.insert(rawget(self,"keys_rev"),karg)
        rawget(self,"keys")[karg]=rawlen(rawget(self,"data"))
    else
        __JSON_repoint__raw__(self.data[keyi],v)
    end

    return self

end

--Functions that do not need argument checks.

--__JSON_empty__ is used to remove references recursively.
__JSON_empty__=function(self)
    local i,j,k,v
    if self.jtype==jtype.object or self.jtype==jtype.array then
        for k,v in ipairs(rawget(self,"data")) do 
            v.__parent__=nil 
            __JSON_empty__(v) 
        end
    end
    self.data=nil
    self.keys=nil
    self.keys_rev=nil
    self.jtype=jtype.unk
end
        
--Functions with argument checks (non-raw__).

__JSON_new_boolean__=function(arg) 
    assert(type(arg)=="boolean","Error __JSON_new_boolean__: argument must be boolean")
    return __JSON_new_boolean__raw__(arg) 
end

__JSON_new_number__=function(arg) 
    if type(arg)~="number" then arg=tonumber(arg) end
    return __JSON_new_number__raw__(arg) 
end

__JSON_new_string__=function(arg) 
    if type(arg)~="string" then arg=tostring(arg) end
    return __JSON_new_string__raw__(arg) 
end

__JSON_new_array__=function(arg,__parent__)
    local rv=__JSON_new_array__raw__(__parent__)
    __JSON_array_insert__raw__(rv,arg)
    return rv
end

__JSON_new_object__=function(arg,__parent__)
    local rv=__JSON_new_object__raw__(__parent__)
    __JSON_object_insert__raw__(rv,arg)
    return rv
end

__JSON_repoint__=function(self,arg)
    assert(bIsJSON(arg),"Error JSON: in __JSON_repoint__, target must be a valid JSON object.")
    return __JSON_repoint__raw__(self,arg)
end

__JSON_atom_insert__=function(self,arg,karg,opts)
    opts=opts or {}
    if arg==nil or arg==NULL then
        __JSON_empty__(self)
        self.jtype=jtype.null
    elseif bIsJSON(arg) then
        if opts.__preserve_jtype__ and self.jtype~=arg.jtype and not bIsJTypeNULL(self.jtype) then
            error("Error JSON: cannot insert different jtype into non-NULL atom when __preserve_jtype__ option is used")
        end
        if bIsJTypeAtom(arg.jtype) then
            if karg==nil then
                if opts.__array_insert__ then --perserve existing value as the first element of a list
                    local tmpjtype=self.jtype
                    local tmpdata=self.data
                    __JSON_array_empty__(self)
                    __JSON_array_insert__raw__(self,__JSON_new_atom__raw(tmpdata,tmpjtype,self))
                    __JSON_array_insert__raw__(self,arg)
                elseif opts.__preserve_jtype__ and self.jtype~=arg.jtype and not bIsJTypeNULL(self.jtype) then --does not preserve NULL
                    if self.jtype==jtype.boolean then
                        if wds.bIn(arg.jtype,jtype.unk,jtype.NULL) then
                            rawset(self,"data",false)
                        elseif arg.jtype==jtype.number then
                            local d=rawget(arg,"data")
                            rawset(self,"data",not ((d==nil) or (wds.bIsNaN(d)) or (math.abs(arg)<1e-10)) )
                        else 
                            local d=string.lower(rawget(arg,"data"))
                            if d=="true" then
                                rawset(self,"data",true)
                            elseif d=="false" then
                                rawset(self,"data",false)
                            else
                                d=tonumber(d)
                                rawset(self,"data",not ((d==nil) or (wds.bIsNaN(d)) or (math.abs(arg)<1e-10)) )
                            end
                        end
                    elseif self.jtype==jtype.number then
                        local d=rawget(arg,"data")
                        if d==false then
                            d=0
                        elseif d==true then
                            d=1
                        else
                            d=tonumber(d)
                        end
                        rawset(self,"data",d)
                    else -- string
                        rawset(self,"data",tostring(rawget(arg,"data")))
                    end
                else
                    --change atom type
                    self.jtype=arg.jtype
                    rawset(self,"data",rawget(self,"data"))
                end
            else
                --change to an object
                __JSON_object_empty__(self)
                __JSON_object_insert__raw__(self,arg,karg)
            end
        elseif arg.jtype==jtype.array then
            __JSON_array_empty__(self)
            __JSON_array_insert__raw__(self,arg,karg)
        elseif arg.jtype==jtype.object then
            __JSON_object_empty__(self)
            __JSON_object_insert__raw__(self,arg,karg)
        else
            error("Error JSON: internal error")
        end
    else
        local targ=type(arg)
        if karg==nil then
            if wds.bIn(targ,"boolean","number","string") then
                if opts.__array_insert__ and rawget(self,"data")~=nil then
                    local ldata=self.data
                    local ljtype=self.jtype
                    __JSON_array_empty__(self)
                    __JSON_array_insert__raw__(self,__JSON_new_atom__raw__(ldata,ljtype))
                    __JSON_array_insert__raw__(self,__JSON_new_atom__raw__(arg,jtype(targ)))
                else
                    __JSON_empty__(self)
                    self.data=arg
                    self.jtype=jtype(targ)
                end
            elseif targ=="table" then
                local n,n1,n2,nh,n2fields,nhfields
                n,n1,n2,nh,n2fields,nhfields=wds.length(arg)
                assert(n1==0 or n2==0,"Error JSON: converting a table into an array or object must be either have #arg==0 for an object or only have keys 1..#arg for an array.")
                if n1>0 then
                    if opts.__array_insert__ then
                        local i,j,k,v
                        for i=1,n1,1 do
                            v=arg[i]
                            if self.jtype==jtype.array then
                                __JSON_array_insert__raw__(self,v,karg,opts)
                            else
                                __JSON_atom_insert__(self,v,karg,opts)
                            end
                        end
                    elseif n1==1 then
                        __JSON_atom_insert__(self,v[1],karg,opts)
                    else
                        error("Error JSON: internal error")
                    end
                elseif n2>0 then
                    if opts.__preserve_jtype__ then
                        error("Error JSON: cannot insert into an atomic a key-value table when __preserve_jtype__ option is used.")
                    end
                    local k,v
                    for k,v in pairs(n2fields) do
                        if self.jtype==jtype.object then
                            __JSON_object_insert__raw__(self,arg[k],k,opts)
                        else
                            __JSON_atom_insert__(self,arg[k],k,opts)
                        end
                    end
                else
                    print("Warning JSON: did not change atomic value when insert with an empty table was called.")
                end
            end
        else
            if opts.__preserve_jtype__ then
                error("Error JSON: cannot insert into an atomic a key-value table when __preserve_jtype__ option is used.")
            end
            if wds.bIn(targ,"boolean","number","string") then
                local v=__JSON_new_atom__raw__(arg,jtype(targ))
                __JSON_atom_insert__(self,v,karg,opts)
            elseif targ=="table" then
                __JSON_object_empty__(self)
                __JSON_object_insert__raw__(self,arg,karg,opts)
            end
        end
    end
    return self
end

__JSON_copy__=function(obj)
    assert(bIsJSON(obj),"Error __JSON_copy__: argument must pass bIsJSON")
    -- the JSON values without children
    local jt=obj.jtype
    if bIsJTypeUnk(jt) then return __JSON_new_unk__() end
    if bIsJTypeNULL(jt) then return __JSON_new_null__() end
    if bIsJTypeAtom(jt) then return __JSON_new_atom__raw__(obj.data,jt) end
    if bIsJTypeArray(jt) then
        local rv=__JSON_new_array__raw__()
        __JSON_array_insert__raw__(rv,obj.data)
        return rv
    end
    if bIsJTypeObject(jt) then
        local rv=__JSON_new_object__raw__()
        __JSON_object_insert__raw__(rv,obj)
        return rv
    end
end

__JSON_insert__=function(self,arg,karg,opts)
    if self.jtype==jtype.unk or bIsJTypeAtom(self.jtype) then
        return __JSON_atom_insert__(self,arg,karg,opts)
    elseif self.jtype==jtype.array then
        return __JSON_array_insert__raw__(self,arg,karg,opts)
    elseif self.jtype==jtype.object then
        return __JSON_object_insert__raw__(self,arg,karg,opts)
    else
        error("Error JSON: internal error")
    end
    return self
end

--insert_AAA atom inserts into atoms can change type
--insert_AAA with a key can change an atom or empty array into an object
__JSON_insert_atom__=function(self,targ,arg,karg)
    assert(targ~jtype.null or arg==nil or arg==NULL,"Error JSON: inserting a NULL can only take a nil or NULL argument")
    if karg==nil then
        if self.jtype==jtype.unk then
            if targ==jtype.null then
                self.jtype=jtype.null
            else
                self.jtype=targ
                self.data=arg
            end
        elseif bIsJTypeAtom(self.jtype) then
            __JSON_empty__(self)
            self.jtype=targ
            self.data=arg
        elseif self.jtype==jtype.array then
            __JSON_array_insert__raw__(self,arg,karg)
        elseif self.jtype==jtype.object then
            __JSON_object_insert__raw__(self,arg,karg)
        else
            error("Error JSON: internal error")
        end
    return self
end
end

__JSON_new__=function(arg)
    local rv
    if arg==nil then
        rv=__JSON_new_unk__()
    elseif arg==NULL then
        rv=__JSON_new_null__()
    elseif bIsJSON(arg) then
        rv=wds.deeper_copy(arg)
    elseif jtype.bIsValid(arg) then
        if arg==jtype.unk then
            rv=__JSON_new_unk__()
        elseif arg==jtype.null then
            rv=__JSON_new_null__()
        elseif arg==jtype.boolean then
            rv=__JSON_new_false__()
        elseif arg==jtype.number then
            rv=__JSON_new_number__raw__(NaN)
        elseif arg==jtype.string then
            rv=__JSON_new_number__raw__("")
        elseif arg==jtype.array then
            rv=__JSON_new_array__raw__()
        elseif arg==jtype.object then
            rv=__JSON_new_object__raw__()
        else
            error("Error JSON: internal error")
        end
    else
        local targ=type(arg)
        if targ=="boolean" then
            rv=__JSON_new_boolean__raw__(arg)
        elseif targ=="number" then
            rv=__JSON_new_number__raw__(arg)
        elseif targ=="string" then
            rv=__JSON_new_string__raw__(arg)
        elseif targ=="table" then
            local n,n1,n2,nh
            n,n1,n2,nh=wds.length(arg)
            assert(n1==0 or n2==0,"Error JSON: converting a table into an array or object must be either have #arg==0 for an object or only have keys 1..#arg for an array.")
            if n1>0 then -- found array, only take indexed entries
                rv=__JSON_new_array__(arg)
            else
                rv=__JSON_new_object__(arg)
            end
        else
            error("Error JSON: cannot instantiate a new value from a value of type "..targ)
        end
    end
    return rv
end

__JSON_class__index_base.new=__JSON_new__
__JSON_class__index_base.AsStringValue=function(self, arg) 
    assert(type(arg)=="string", "Error: attempted JSON.AsStringValue() with non-string argument")
    self.jtype=jtype.string
    self.data=nil
    self.keys=nil
    self.keys_rev=nil
    self.data=arg
end
__JSON_class__index_base.AsNumberValue=function(self, arg) 
    assert(type(arg)=="number", "Error: attempted JSON.AsNumberValue() with non-number argument")
    self.jtype=jtype.number
    self.data=nil
    self.keys=nil
    self.keys_rev=nil
    self.data=arg
end
__JSON_class__index_base.AsBooleanValue=function(self, arg) 
    assert(type(arg)=="boolean", "Error: attempted JSON.AsBooleanValue() with non-boolean argument")
    self.jtype=jtype.boolean
    self.data=nil
    self.keys=nil
    self.keys_rev=nil
    self.data=arg
end
__JSON_class__index_base.AsNULLValue=function(self, arg) 
    if arg~=nill then
        if arg~=wdsm.NULL then
            error("Error: attempted JSON.AsNULLValue() with non-nil or NULL argument")
        end
    end
    self.jtype=jtype.null
    self.data=nil
    self.keys=nil
    self.keys_rev=nil
end
__JSON_class__index_base.AsArrayValue=function(self, arg) 
    self.jtype=jtype.array
    self.data=nil
    self.keys=nil
    self.keys_rev=nil
    self.data={}
    local rc=self << arg
    return rc
end
__JSON_class__index_base.AsObjectValue=function(self, arg) 
    self.jtype=jtype.object
    self.data=nil
    self.keys=nil
    self.keys_rev=nil
    self.data={}
    self.keys={}
    self.keys_rev={}
    local rc=self << arg
    return rc
end

__JSON_class__index_base.data=function(self,arg) return rawget(self,"data") end

__JSON_class__index_base.dataref=function(self,arg) 
    if rawget(self,"data")==nil then
        rawset(self,"data",{})
    end
    return rawget(self,"data") end

__JSON_class__index_base.keysref=function(self,arg) 
    if rawget(self,"keys")==nil then
        rawset(self,"keys",{})
    end
    if rawget(self,"keys_ref")==nil then
        rawset(self,"keys_rev",{})
    end
    return rawget(self,"keys") end

__JSON_class__index_base.keys_revref=function(self,arg) 
    if rawget(self,"keys")==nil then
        rawset(self,"keys",{})
    end
    if rawget(self,"keys_ref")==nil then
        rawset(self,"keys_rev",{})
    end
    return rawget(self,"keys_rev") end

__JSON_class__index_base.jtype=function(self,arg) return rawget(self,"jtype") end

__JSON_class__index_base.len=function(self,arg)
    if self.jtype==jtype.object or self.jtype==jtype.array then
        return #self.data
    else
        return 1
    end
end

__JSON_class__index_base.length=__JSON_class__index_base.len
__JSON_class__index_base.__class__=__JSON_class__
__JSON_class__index_base.__classname__="JSON"
__JSON_class__index_base.print="TODO"

__JSON_class__.__index=function(self,arg)
    local rv=__JSON_class__index_base[arg] 
    if rv~=nil then
        return rv
    elseif arg==nil then
        return rawget(self,"data")
    else
        if bIsHiddenFieldName(arg) then
            return nil
        end
        if self.jtype==jtype.object then
            local dataref=__JSON_class__index_base.dataref(self)()
            local keysref=__JSON_class__index_base.keysref(self)()
            local keys_revref=__JSON_class__index_base.keys_revref(self)()
            if keys_revref[arg]~=nil then
                return dataref[arg]
            elseif keysref[arg]~=nil then
                return dataref[keysref[arg]]
            else
                return nil
            end
        elseif self.jtype==jtype.array and type(arg)=="number" then
            local dataref=rawget(self,"data")
            if arg==1 and type(dataref)~="table" then
                return dataref
            elseif arg>=1 and arg<=#dataref then
                return dataref[arg]
            else 
                return nil
            end
        else
            return nil
        end
    end
end

__JSON_class__.__len=function(self)
    if self.jtype==jtype.object or self.jtype==jtype.array then 
        if self.data==nil then
            return 0
        else
            return #self.data 
        end
    end
    return 1
end

__JSON_class_____tostring=function(self,opts,lopts)

    opts=opts or {}
    opts.depth=opts.depth or 1
    opts.maxdepth=opts.maxdepth or 100
    opts.indent=opts.indent or "  "
    opts.linesep=opts.linesep or "\n"
    opts.itemsep=opts.itemsep or ", "
    opts.kvsep=opts.kvsep or " : "

    lopts=lopts or {}
    lopts.depth=lopts.depth or opts.depth
    lopts.extraindent=lopts.extraindent or ""
    
    local indent=string.rep(opts.indent,lopts.depth)..lopts.extraindent
    local indentM1=string.rep(opts.indent,lopts.depth-1)..lopts.extraindent
    
    if self.jtype==jtype.unk then
        return "unk"
    elseif self.jtype==jtype.null then
        return "null"
    elseif wds.bIn(self.jtype,jtype.boolean,jtype.number) then 
        return tostring(self.data)
    elseif self.jtype==jtype.string then
        return "\""..(self.data or "").."\""
    elseif self.jtype==jtype.array then
        local i,j,v
        local tmp={}
        for i,v in ipairs(self.data or {}) do
            table.insert(tmp,__JSON_class_____tostring(v
                ,opts,{depth=lopts.depth+1,extraindent=lopts.extraindent}))
        end
        return "["..opts.linesep..indent..table.concat(tmp,opts.itemsep..opts.linesep..indent)..opts.linesep..indentM1.."]"
    elseif self.jtype==jtype.object then
        local i,j,v,k
        local rv=indent.."{\n"
        local tmp={}
        j=0
        for i,v in pairs(self.data) do
            k=self.keys_rev[i]
            local tmpindent=string.rep(" ",#k+#opts.itemsep)
            table.insert(tmp,"\""..k.."\""..opts.kvsep..__JSON_class_____tostring(v
                ,opts,{depth=lopts.depth+1,extraindent=lopts.extraindent..tmpindent}))
        end
        return "{"..opts.linesep..indent..table.concat(tmp,opts.itemsep..opts.linesep..indent)..opts.linesep..indentM1.."}"
    else
        error("Error JSON: internal error")
    end

end

__JSON_class__.__tostring=__JSON_class_____tostring

__JSON_class__index_base.toggle_tostring=function()
    if __JSON_class__.__tostring then
        __JSON_class__.__tostring=nil
    else
        __JSON_class__.__tostring=__JSON_class_____tostring
    end
end

__JSON_insert_null__raw__=function(self,karg)
    if wds.bIn(self.jtype,jtype.unk,jtype.null) then 
        self.jtype=jtype.null
    elseif bIsJTypeAtom(self.jtype) then
        __JSON_empty__(self)
        self.jtype=jtype.null
    elseif self.jtype==jtype.array then
        __JSON_array_insert__raw__(self,arg,karg)
    elseif self.jtype==jtype.object then
        assert(karg~=nil, "Error JSON: << into object requires a key")
        local ltmp=__JSON_new_null__()
        _JSON_object_insert(self,ltmp,karg)
    else
        error("Error JSON: internal error")
    end
    return self
end

__JSON_insert_atom__raw__=function(self,arg,karg)
    if self.jtype==jtype.unk or self.jtype==jtype.null then 
        self.jtype=jtype(type(arg))
        self.data=arg
        return self 
    end
    if bIsJTypeAtom(self.jtype) and karg==nil then
        self.jtype=jtype(type(arg))
        self.data=arg
        return self
    end
    if self.jtype==jtype.array then
        __JSON_array_insert__raw__(self,arg,karg)
        return self
    elseif self.jtype==jtype.object then
        assert(karg~=nil, "Error JSON: << into object requires a key")
        local ltmp=__JSON_new_null__()
        _JSON_object_insert(self,ltmp,karg)
        return self
    else
        error("Error JSON: internal error")
    end
end

__JSON_class_____shl=function(self, arg, karg) --k[ey]arg is used for pushing in a keyed value to an object
    local targ=type(arg)
    if arg==nil or arg==NULL then
        __JSON_insert_null__raw__(self,karg)
        return self
    elseif self.jtype==jtype.unk or bIsJTypeAtom(self.jtype) then
        return __JSON_atom_insert__(self,arg,karg)
    elseif self.jtype==jtype.array then 
        return __JSON_array_insert__raw__(self,arg,karg)
    elseif self.jtype==jtype.object then
        return __JSON_object_insert__raw__(self,arg,karg)
    elseif self.jtype==jtype.unk then
        assert(karg==nil, "Error JSON: cannot insert keyed element into an atomic")
        if karg==nil then
            if targ=="number" then
                return __JSON_repoint__(self,__JSON_new_number__raw__(arg))
            elseif targ=="boolean" then
                return __JSON_repoint__(self,__JSON_new_boolean__raw__(arg==true))
            elseif targ=="string" then
                return __JSON_repoint__(self,__JSON_new_string__raw__(arg))
            elseif targ=="table" then
                if #arg>0 then
                    __JSON_repoint__(self,__JSON_new_array__raw__())
                    local k,v
                    for k,v in ipairs(arg) do
                        __JSON_array_insert__raw__(self,v)
                    end
                else
                    __JSON_repoint__(self,__JSON_new_object__raw__())
                    local k,v
                    for k,v in pairs(arg) do
                        __JSON_object_insert__raw__(self,v,k)
                    end
                end
                return self
            else
                error("Error JSON: cannot determine type to insert")
            end
        else
            __JSON_repoint__(self,__JSON_new_object__raw())
            return __JSON_object_insert__raw(self,arg,karg)
        end
    else
        error("Error JSON: internal error")
    end
    return self
end

__JSON_class__.__shl=function(self,arg)
    return __JSON_class_____shl(self,arg)
end

__JSON_class__.__call=function(self,k)
    if k==nil then
        return self.data
    elseif type(k)=="string" and self.jtype==jtype.object then
        return self.data[self.keys[k]]
    elseif type(k)=="number" and wds.bIn(self.jtype,jtype.object,jtype.array) then
        return self.data[k]
    else 
        error("Other calls to JSON() not implemented")
    end
end

__parse_move_to_next_non_WSP=function(arg,start,stop)
    local i=start
    local c=string.sub(arg,i,i)
    while (i<stop) and bIsWSP(c) do
        i=i+1
        c=string.sub(arg,i,i)
    end
    return i,stop,c
end

__JSON_parse__=function(self,arg,start,stop)
    start=start or 1
    stop=stop or string.len(arg)
    local lrv
    print("arg=",wds.show(arg))
    start,stop,lrv=__JSON_parse_value__(nil,arg,start,stop)
    print("lrv=",wds.show(lrv))
    if self.jtype==jtype.unk or bIsJTypeAtom(self.jtype) then
        __JSON_empty__(self)
        __JSON_repoint__raw__(self,lrv)
    elseif self.jtype==jtype.array then
        __JSON_array_insert__raw__(self,lrv)
    elseif self.jtype==jtype.object then
        __JSON_object_insert__raw__(self,lrv)
    else
        error("Error JSON: internal error")
    end
    return self
end
__JSON_class__index_base.parse=__JSON_parse__

JSON=
AddToModuleHelp{
    JSON=[==[A simple class for holding JSON data.]==]
} ..
function(arg)
    if arg==nil then
        return __JSON_new_unk__()
    elseif arg==NULL then
        return __JSON_new_null__()
    elseif arg==true then
        return __JSON_new_true__()
    elseif arg==false then
        return __JSON_new_false__()
    elseif jtype.bIsValid(arg) then
        return __JSON_new__(arg)
    elseif bIsJSON(arg) then
        return wds.deeper_copy(arg)
    end
    if type(arg)=="string" and string.find(arg,"^([%s%c\a\b\f\n\r\t\v]*)[\"{[]")~=nil then --a json string value
        local rv=__JSON_new__()
        return rv:parse(arg)
    else
        local rv=__JSON_new__()
        __JSON_insert__(rv,arg,nil,{__array_insert__=true})
        return rv
    end
end

__JSON_parse_value__=function(self,arg,start,stop,targettype)
    start=start or 1
    stop=stop or string.len(arg)
    targettype=targettype or jtype.unk
    local rv
    local i=start
    local j=start
    local lstart=start
    local lstop=stop
    local lrv={}
    local llen=0
    local cM1=""
    local c=""
    local s=""
    local lkey=""
    local found=false
    local found2=false
    local foundstart=false
    local foundstop=false

    cM1=c
    start,stop,c = __parse_move_to_next_non_WSP(arg,start,stop)

    if targettype==jtype.string or c=="\"" then -- parsing one string, must be enclosed in double quotes (")

        i=start
        if c~="\"" then
            error("JSON parsing error, substring does not start as string: ||"..string.sub(arg,start,start+10).."||")
        end
        foundstart=true
        foundstop=false
        j=i
        while (j<stop) and not foundstop do
            j=j+1
            cM1=c
            c=string.sub(arg,j,j)
            foundstop=(cM1~="\\" and c=="\"")
        end
        if not foundstop then
            error("JSON parsing error, substring does not end as string: ||"..string.sub(arg,start,start+10).."||")
        end
        rv=__JSON_new_string__raw__(wds.StringUnquote(string.sub(arg,i,j)),self)
        return i,j,rv

    end

    rv=__JSON_new__(targettype,self)

    if c=="{" then -- parsing one object

        foundstart=true
        foundstop=false

        i=start

        llen=0

        j=i

        __JSON_object_empty__(rv)

        while (j<stop) and not foundstop do
        
            j=j+1

            --first, pull a key
            lstart,lstop,lrv=__JSON_parse_value__(rv,arg,j,stop,jtype.string)
            lkey=wds.StringUnquote(lrv.data)

            if lstop==stop then
                error("JSON parsing error, ends with key: ||"..string.sub(arg,lstart,lstop).."||")
            end
            j=lstop+1
            lstart,lstop,c = __parse_move_to_next_non_WSP(arg,j,stop)
            if c~=":" then
                error("JSON parsing error, ends with key without following \":\" : ||"..string.sub(arg,lstart,lstop).."||")
            end
            j=lstart+1
            lstart,lstop,lrv=__JSON_parse_value__(nil,arg,j,stop)
            __JSON_object_insert__raw__(rv,lrv,lkey)
            j=lstop+1
            lstart,lstop,c = __parse_move_to_next_non_WSP(arg,j,stop)
            if c=="," then
                --continue
                j=lstart
            elseif c=="}" then
                j=lstart
                foundstop=true
            else
                error("JSON parsing error, object ends incorrectly : ||"..string.sub(arg,lstart,lstop).."||")
            end

        end

        if not foundstop then
                error("JSON parsing error, object ends incorrectly : ||"..string.sub(arg,lstart,lstop).."||")
        end

        return i,j,rv

    end
        

    if c=="[" then -- parsing one array

        foundstart=true
        foundstop=false

        i=start
        j=i

        llen=0

        __JSON_array_empty__(rv,self)

        while (j<stop) and not foundstop do

            j=j+1
            lstart,lstop,lrv=__JSON_parse_value__(rv,arg,j,stop)
            llen=llen+1
            __JSON_array_insert__raw__(rv,lrv)
            j=lstop+1
            lstart,lstop,c = __parse_move_to_next_non_WSP(arg,j,stop)
            if c=="," then
                --continue
                j=lstart
            elseif c=="]" then
                foundstop=true
                j=lstart
            else
                error("JSON parsing error, object ends incorrectly : ||"..string.sub(arg,lstart,lstop).."||")
            end

        end

        if not foundstop then
                error("JSON parsing error, object ends incorrectly : ||"..string.sub(arg,lstart,lstop).."||")
        end

        return i,j,rv

    end

    local lcmpword

    if wds.bIn(c,"f","t","n") then --parsing a boolean or null which must be precisely false, true, or null

        i=start
        if c=="f" then
            j=start+5
            lcmpword="false"
            rv=__JSON_new_false__(self)
        elseif c=="t" then
            j=start+4
            lcmpword="true"
            rv=__JSON_new_true__(self)
        else
            j=start+4
            lcmpword="null"
            rv=__JSON_new_null__(self)
        end

        if string.find(arg,lcmpword,start) then

            if j<stop then
                -- look ahead to make sure it ended correctly
                s=string.sub(arg,j+1,j+1)
                assert( wds.bIn(s,",","}","]") or bIsWSP(s) 
                    , "Error JSON: parsing error, object ends incorrectly : ||"..string.sub(arg,lstart,lstop).."||")
            end

            return i,j,rv

        else
            error("JSON parsing error, boolean value parsing fails ||"..string.sub(arg,lstart,lstop).."||")
        end

    end

    if string.find(c,"[+%-%d]") then --parsing a number

        if start==stop then -- last character case
            if string.find(c,"[%d]") then --parsing a single digit integer (ending on [+-] is not valid)
                lrv=tonumber(string.sub(arg,start,stop))
                if lrv==nil then
                    error("JSON parsing error, number value parsing fails ||"..string.sub(arg,start,stop).."||")
                end
                rv=__JSON_new_number__raw__(lrv,self)
                return start,stop,rv
            else
                error("JSON parsing error, number value parsing fails ||"..string.sub(arg,start,stop).."||")
            end
        end

        i=start
        j=start
        found=false
        while (j<stop) and not found do
            j=j+1
            c=string.sub(arg,j,j)
            found=bIsWSP(c) or wds.bIn(c,",","]","}")
        end
        if found then
            j=j-1
        end
        lrv=tonumber(string.sub(arg,i,j))
        if lrv==nil then
            error("JSON parsing error, number value parsing fails ||"..string.sub(arg,start,stop).."||")
        end
        rv=__JSON_new_number__raw__(lrv,self)
        return i,j,rv

    end

    error("JSON value parsing error, uknown: ||"..string.sub(arg,start,stop).."||")

end

parse=
AddToModuleHelp{
    parse=[==[A simple json parser returning a lua structure.]==]
} .. 
function(arg)
    local start=1
    local stop=string.len(arg)
    local rv=__JSON_new__()
    local lrv
    local f=rv.parse
    start,stop,lrv=rv:parse(arg,start,stop)
    return rv
end

return _M
