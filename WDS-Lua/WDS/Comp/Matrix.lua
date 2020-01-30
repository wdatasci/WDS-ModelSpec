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

--- A pure-lua simple implementation of a basic matrix library.
--  This lua implementation mirrors the WDS.Comp.Matrix.h C++ library which 
--  is based on the classic Stroustrup C++ library and Armadillo.
--  @submodule WDS.Comp


local wds=require("WDS")
local wdsu=require("WDS.Util")
local pesc=require("WDS.Util.python_esc")

local __parent__="Comp"
local __name__="Matrix"
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


local _M={}
local _G=_G
_ENV=wds.EnvExtension(_M,_G)

local docstring=module_name .. " ("..module_path..")"..[==[
    A pure-lua simple implementation of a basic matrix library.
    This lua implementation mirrors the WDS.Comp.Matrix.h C++ library which 
    is based on the classic Stroustrup C++ library and Armadillo.
    ]==]

if wds.bIsMain(table.pack(...),module_name) then
    print("test with "..__parent__.."/"..__name__.."_test.lua")
    print(docstring)
    os.exit()
end

info={name=module_name
    ,path=module_path
    ,doc=docstring
    ,docmap={}
    ,_ENV=_M
}

-- localizing AddToModuleHelp to globally assign to this module's info table
local AddToModuleHelp=function(tbl); tbl.info=info; return wds.AddToModuleHelp(tbl); end

-- The construction of the NULL singleton has been moved to the WDS module.
NULL=wds.NULL

-- The dMatrix class construction --
-- The proto data object.
local dMatrix_Obj={
    data={}
    , n_rows=0
    , n_cols=0
    , __cellptr__=0
    , __insertmode__=0
}

local _dMatrix_ClassMT={}
local _dMatrix_ClassMTI={}

bIsMatrix=function(obj)
    if type(obj)=="table" then
        if obj.__class__ and obj.__class__==_dMatrix_ClassMT then
            return true
        elseif obj.__classname__ and obj.__classname__=="dMatrix" then
            return true
        else
            return false
        end
    else
        return false
    end
end



local _dMatrix_IJ_index=function(self,i,j)
    if j==nil then
        assert( (self.n_cols==1 or self.n_rows==1)  and i>=1 and i<=self.n_rows*self.n_cols, "index out of bounds")
        return i
    end
    assert(i>=1 and i<=self.n_rows, "index out of bounds, i, "..i.." self.n_rows")
    assert(j>=1 and j<=self.n_cols, "index out of bounds, j, "..j.." self.n_cols")
    return (i-1)*self.n_cols+j
end

local _dMatrix_index_IJ=function(self,index)
    assert(index>=1 and index<=self.n_rows*self.n_cols, "index out of bounds, "..index..", "..wds.show(self))
    local i=math.floor( (index-1)/self.n_cols )
    local j=index-i*self.n_cols
    return i+1, j
end

local _dMatrix_IJ_get=function(self,i,j)
    return self.data[_dMatrix_IJ_index(self,i,j)]
end

local _dMatrix_IJ_set=function(self,i,j,v)
    self.data[_dMatrix_IJ_index(self,i,j)]=v
end

local _dMatrix_wrap=function(self,v,...)
    local args=table.pack(...)
    if #args==1 and type(args[1])=="table" then
        args=args[1]
    end
    self.data=v
    if args.SingleColumn then
        self.n_cols=1
        self.n_rows=#v
    elseif args.SingleRow then
        self.n_cols=#v
        self.n_rows=1
    else
        self.n_rows=args.NRows or args.Rows or args.n_rows
        self.n_cols=args.NCols or args.Cols or args.n_cols
        if self.n_rows==nil and self.n_cols==nil then
            self.n_rows=1
            self.n_cols=#v
        elseif self.n_rows==nil then
            self.n_rows=math.ceil(#v/self.n_cols)
        elseif self.n_cols==nil then
            self.n_cols=math.ceil(#v/self.n_rows)
        end
        if self.n_rows*self.n_cols>#v then
            self.data={}
            for i=1, self.n_rows*self.n_cols do
                table.insert(self.data,v[i])
            end
        elseif self.n_rows*self.n_cols<#v then
            self.data=wds.copy_simple(v)
            for i=#v+1, self.n_rows*self.n_cols do
                table.insert(self.data,0.0)
            end
        end
    end
    self.__cellptr__=0
    self.__insertmode__=0
    return self
end

local _dMatrix_set_size_wo_fill=function(self,n_rows,n_cols)
    self.data={}
    self.n_rows=n_rows
    self.n_cols=n_cols
    self.__cellptr__=0
    self.__insertmode__=0
    return self
end

local _dMatrix_set_size=function(self,n_rows,n_cols,default)
    if default==nil then
        default=0.0
    end
    _dMatrix_set_size_wo_fill(self,n_rows,n_cols)
    if type(default)=="table" and #default==n_rows*n_cols then
        for i=1,n_rows*n_cols do
            table.insert(self.data,default[i])
        end
    elseif type(default)=="function" then
        for i=1,n_rows*n_cols do
            table.insert(self.data,default())
        end
    else
        for i=1,n_rows*n_cols do
            table.insert(self.data,default)
        end
    end
end

local _dMatrix_print=function(self,prefix,lineprefix,depth)
    if lineprefix==nil then
        lineprefix=""
    end
    if prefix then
        print(lineprefix..prefix)
    end
    lineprefix=lineprefix..string.rep(" ",#prefix)

    print(lineprefix.."n_rows:"..self.n_rows)
    print(lineprefix.."n_cols:"..self.n_cols)

    for i=1,self.n_rows do
        local s=lineprefix
        for j=1,self.n_cols do
            local v=self.data[_dMatrix_IJ_index(self,i,j)]
            if type(v)=="number" then
                s=s..string.format(" %10.4f ",v)
            elseif type(v)=="table" then
                s=s..string.format(" {%10s} ",wds.show(v,depth))
            else
                s=s..string.format(" %10s ",v)
            end
        end
        print(s)
    end
    self.__cellptr__=0
    self.__insertmode__=0
end

local _dMatrix_fill=function(self,v)
    for i=1,self.n_rows do
        for j=1,self.n_cols do
            self.data[_dMatrix_IJ_index(self,i,j)]=v
        end
    end
    self.__cellptr__=0
    self.__insertmode__=0
end

local _dMatrix_RowIterator=function(self,i)
    local _t={obj=self,i=i,j=1,n=self.n_cols,init=0,val=0}
    return function(t,o)
        _t.val=_t.val+1
        if _t.val<=_t.n then
            return _t.obj.data[_dMatrix_IJ_index(_t.obj,_t.i,_t.val)]
        end
    end,_t,0
end
    
local _dMatrix_ColumnIterator=function(self,j)
    local _t={obj=self,i=1,j=j,n=self.n_rows,init=0,val=0}
    return function(t,o)
        _t.val=_t.val+1
        if _t.val<=_t.n then
            return _t.obj.data[_dMatrix_IJ_index(_t.obj,_t.val,_t.j)]
        end
    end,_t,0
end

local _dMatrix_Transpose=function(self)
    local rv={}
    _dMatrix_set_size_wo_fill(rv,self.n_cols,self.n_rows)
    for j=1,self.n_cols do
        for i=1,self.n_rows do
            table.insert(rv.data,self.data[_dMatrix_IJ_index(self,i,j)])
        end
    end
    return setmetatable(rv,_dMatrix_ClassMT)
end


    
-- The metatable __index function for dMatrix
_dMatrix_ClassMTI.__index=function(t,k)
    if type(k)=="table" and #k==2 then
        if type(k[1])=="number" then
            if type(k[2])=="number" then
                return t.data[_dMatrix_IJ_index(t,k[1],k[2])]
            elseif wds.bIsEmpty(k[2]) then
                --return an iterator
                return _dMatrix_RowIterator(t,k[1])
            else
                error("unknown index method")
            end
        elseif type(k[2])=="number" then
            if wds.bIsEmpty(k[1]) then
                --return an iterator
                return _dMatrix_ColumnIterator(t,k[2])
            else
                error("unknown index method")
            end
        else
                error("unknown index method")
        end
    elseif type(k)=="number" then
        return t.data[k]
    elseif k=="data" then
        return rawget(t,k)
    elseif k=="n_rows" then 
        --base object may have had n_rows assigned to nil, so the call should return nil
        return rawget(t,k)
        --return nil
    elseif k=="n_cols" then 
        --base object may have had n_cols assigned to nil, so the call should return nil
        return rawget(t,k)
        --return nil
    elseif k=="__classname__" then
        return "dMatrix"
    elseif k=="__class__" then
        return _dMatrix_ClassMT
    elseif k=="set_size" or k=="new" then
        return _dMatrix_set_size
    elseif k=="wrap" then
        return _dMatrix_wrap
    elseif k=="row" then
        return _dMatrix_RowIterator
    elseif k=="col" then
        return _dMatrix_ColumnIterator
    elseif k=="t" then
        return _dMatrix_Transpose
    elseif k=="print" then
        return _dMatrix_print
    elseif k=="fill" then
        return _dMatrix_fill
    elseif k=="set_cellptr" then
        return function(self,x) self.__cellptr__=x end
    elseif k=="reset_cellptr" then
        return function(self) self.__cellptr__=0 end
    elseif k=="isOrdered" then
        return function(self)
            if self.n_rows==1 then
                for i=1,self.n_rows do
                    local v1,v2=nil,self.data[1]
                    for j=2,self.n_cols do
                        v1,v2=v2,rawget(self,"data")[_dMatrix_IJ_index(self,i,j)]
                        if v2<v1 then return false end
                    end
                end
                for j=1,self.n_cols do
                    local v1,v2=nil,self.data[1]
                    for i=2,self.n_rows do
                        v1,v2=v2,rawget(self,"data")[_dMatrix_IJ_index(self,i,j)]
                        if v2<v1 then return false end
                    end
                end
                return true
            end
        end
    elseif k=="__nil__" then
        return false
    elseif k=="save" then
        error("TODO")
    elseif k=="load" then
        error("TODO")
    else
        error("unknown method, "..k)
    end
end

begin_mat="begin_mat"
end_mat="end_mat"
endr="endr"

l__op=function(a,b,c) return NULL end

_dMatrix_ClassMT.__call=function(self,i,j)
        if j==nil and type(i)=="table" and #i==2 then 
            if type(i[1])=="number" and type(i[2])=="number" then
                return self.data[_dMatrix_IJ_index(self,i[1],i[2])]
            elseif type(i[1])=="table" or type(i[2])=="table" then
                return self[i]
            else
                error("Other calls to dMatrix() not implemented yet")
            end
        elseif type(i)=="number" and (j==nil or type(j)=="number") then
            return self.data[_dMatrix_IJ_index(self,i,j)]
        else
            error("Other calls to dMatrix() not implemented yet")
        end
    end

_dMatrix_ClassMT.__unm=function(self)
        for i=1,self.n_rows*self.n_cols do
            self.data[i]=-self.data[i]
        end
        return self
    end

_dMatrix_ClassMT.__add=function(lo,ro)
        return setmetatable(l__op(lo,ro,0),_dMatrix_ClassMT)
    end

_dMatrix_ClassMT.__sub=function(lo,ro)
        return setmetatable(l__op(lo,ro,1),_dMatrix_ClassMT)
    end

_dMatrix_ClassMT.__mul=function(lo,ro)
        return setmetatable(l__op(lo,ro,2),_dMatrix_ClassMT)
    end

_dMatrix_ClassMT.__div=function(lo,ro)
        return setmetatable(l__op(lo,ro,3),_dMatrix_ClassMT)
    end

_dMatrix_ClassMT.__shl=function(self,v)
        if v==begin_mat then
            self.__insertmode__=1
            self.data={}
            self.n_rows=1
            self.n_cols=0
            self.__cellptr__=0
        elseif v==end_mat then
            self.__insertmode__=0
            if self.n_cols==0 then
                self.n_cols=self.__cellptr__
                self.n_rows=1
            else
                self.n_rows=math.floor((self.__cellptr__-1)/self.n_cols)+1
            end
            local i,j=_dMatrix_index_IJ(self,self.__cellptr__)
            for k=j+1,self.n_cols do
                self.__cellptr__=self.__cellptr__+1
                table.insert(self.data,0.0)
            end
            self.__cellptr__=0
        elseif v==endr then
                if self.__insertmode__==1 then
                    if self.n_cols==0 then
                        if self.__cellptr__==0 then
                            error("using << notation, setting up empty matrix")
                        end
                        self.n_cols=self.__cellptr__
                    end
                end
                local i,j=_dMatrix_index_IJ(self,self.__cellptr__)
                for k=j+1,self.n_cols do
                    self.__cellptr__=self.__cellptr__+1
                    if self.__insertmode__==1 then
                        table.insert(self.data,0.0)
                    else
                        self.data[self.__cellptr__]=0.0
                    end
                end
        elseif type(v)=="table" and #v>0 then
                if self.__insertmode__==0 and self.__cellptr__>=self.n_rows*self.n_cols then
                    self.__cellptr__=0
                end
                for k,o in ipairs(v) do
                    self.__cellptr__=self.__cellptr__+1
                    if self.__insertmode__==0 and self.__cellptr__>=self.n_rows*self.n_cols then
                        self.__cellptr__=1
                    end
                    if self.__insertmode__==1 then
                        table.insert(self.data,o)
                    else
                        self.data[self.__cellptr__]=o
                    end
                end
        else
                if self.__insertmode__==0 and self.__cellptr__>=self.n_rows*self.n_cols then
                    self.__cellptr__=1
                else
                    self.__cellptr__=self.__cellptr__+1
                end
                if self.__insertmode__==1 then
                    table.insert(self.data,v)
                    if self.__cellptr__>self.n_rows*self.n_cols then
                        self.n_rows=self.n_rows+1
                    end
                else
                    self.data[self.__cellptr__]=v
                end
        end
        return self
    end

_dMatrix_ClassMT.__concat=function(a,b)
    local rv={}
    if bIsMatrix(a) then
        local tb=type(b)
        if bIsMatrix(b) then
            rv.n_rows,rv.n_cols=math.min(a.n_rows,b.n_rows),(a.n_cols+b.n_cols)
            _dMatrix_set_size(rv,rv.n_rows,rv.n_cols)
            for i=1,rv.n_rows do
                for j=1,a.n_cols do
                    rv.data[_dMatrix_IJ_index(rv,i,j)]=a{i,j}
                end
                for j=1,b.n_cols do
                    rv.data[_dMatrix_IJ_index(rv,i,a.n_cols+j)]=b{i,j}
                end
            end
        elseif tb=="table" and #b>0 then
            local nb=#b
            rv.n_rows,rv.n_cols=a.n_rows,(a.n_cols+nb)
            _dMatrix_set_size(rv,rv.n_rows,rv.n_cols)
            for i=1,rv.n_rows do
                for j=1,a.n_cols do
                    rv.data[_dMatrix_IJ_index(rv,i,j)]=a{i,j}
                end
                for j=1,nb do
                    rv.data[_dMatrix_IJ_index(rv,i,a.n_cols+j)]=b[j]
                end
            end
        elseif wds.bIn(tb,"string","number") then
            rv.n_rows,rv.n_cols=a.n_rows,(a.n_cols+1)
            _dMatrix_set_size(rv,rv.n_rows,rv.n_cols)
            for i=1,rv.n_rows do
                for j=1,a.n_cols do
                    rv.data[_dMatrix_IJ_index(rv,i,j)]=a{i,j}
                end
                rv.data[_dMatrix_IJ_index(rv,i,a.n_rows+1)]=b
            end
        else
            error('error concatenating a Matrix with '..wds.show(b))
        end
    else
        local ta=type(a)
        if ta=="table" and #a>0 then
            local na=#a
            rv.n_rows,rv.n_cols=b.n_rows,(na+b.n_cols)
            _dMatrix_set_size(rv,rv.n_rows,rv.n_cols)
            for i=1,rv.n_rows do
                for j=1,na do
                    rv.data[_dMatrix_IJ_index(rv,i,j)]=a[j]
                end
                for j=1,b.n_cols do
                    rv.data[_dMatrix_IJ_index(rv,i,na+j)]=b{i,j}
                end
            end
        elseif wds.bIn(tb,"string","number") then
            rv.n_rows,rv.n_cols=a.n_rows,(1+b.n_cols)
            _dMatrix_set_size(rv,rv.n_rows,rv.n_cols)
            for i=1,rv.n_rows do
                rv.data[_dMatrix_IJ_index(rv,i,j)]=a
                for j=1,b.n_cols do
                    rv.data[_dMatrix_IJ_index(rv,i,1+j)]=b{i,j}
                end
            end
        else
            error('error concatenating a Matrix with '..wds.show(a))
        end
    end
    return setmetatable(rv,_dMatrix_ClassMT)
end

_dMatrix_ClassMT.__index=_dMatrix_ClassMTI.__index

_dMatrix_ClassMT.__newindex=function(self,k,v)
        if type(k)=="table" and #k==2 then
            _dMatrix_IJ_set(self,k[1],k[2],v)
        elseif type(k)=="number" then
            if self.n_rows==1 then
                _dMatrix_IJ_set(self,1,k,v)
            elseif self.n_cols==1 then
                _dMatrix_IJ_set(self,k,1,v)
            else
                error("Error, in dMatrix, single index undefined unless n_rows==1 or n_cols==1")
            end
        elseif k=="n_rows" or k=="n_cols" or k=="__cellptr__" or k=="__insertmode__" then
            rawset(self,k,v)
        end
    end

l__op=function(lo,ro,oper)
        local rv={}
        _dMatrix_set_size(rv,0,0)
        if NULL==ro or bIsNULLOrError(ro) then
            rv.n_rows,rv.n_cols=lo.n_rows,lo.n_cols
            for i=1,lo.n_rows*lo.n_cols do table.insert(rv.data,NULL) end
        elseif NULL==lo or bIsNULLOrError(lo) then
            rv.n_rows,rv.n_cols=ro.n_rows,ro.n_cols
            for i=1,ro.n_rows*ro.n_cols do table.insert(rv.data,NULL) end
        elseif type(ro)=="number" then
            rv.n_rows,rv.n_cols=lo.n_rows,lo.n_cols
            for i=1,lo.n_rows*lo.n_cols do 
                if oper==0 then
                    table.insert(rv.data,lo.data[i]+ro) 
                elseif oper==1 then
                    table.insert(rv.data,lo.data[i]-ro) 
                elseif oper==2 then
                    table.insert(rv.data,lo.data[i]*ro) 
                elseif oper==3 then
                    table.insert(rv.data,lo.data[i]/ro) 
                end
            end
        elseif type(lo)=="number" then
            rv.n_rows,rv.n_cols=ro.n_rows,ro.n_cols
            for i=1,ro.n_rows*ro.n_cols do 
                if oper==0 then
                    table.insert(rv.data,lo+ro.data[i]) 
                elseif oper==1 then                
                    table.insert(rv.data,lo-ro.data[i]) 
                elseif oper==2 then                
                    table.insert(rv.data,lo*ro.data[i]) 
                elseif oper==3 then                
                    if ro.data[i]==0 then
                        table.insert(rv.data,NULL) 
                    else
                        table.insert(rv.data,lo/ro.data[i]) 
                    end
                end
            end
        elseif type(ro)=="string" or type(lo)=="string" then
            error("dMatrix __mul not defined for strings")
        elseif type(ro)=="table" then
            if ro.__class__ and ro.__class__==lo.__class__ then
                if oper==3 then
                    error("div not implemented yet for dMatrices")
                elseif oper==2 then
                    if (lo.n_rows*lo.n_cols==1) then
                        rv.n_rows,rv.n_cols=ro.n_rows,ro.n_cols
                        for i=1, ro.n_rows*ro.n_cols do table.insert(rv.data,lo.data[1]*lo.data[i]) end
                    elseif (ro.n_rows*ro.n_cols==1) then
                        rv.n_rows,rv.n_cols=lo.n_rows,lo.n_cols
                        for i=1, lo.n_rows*lo.n_cols do table.insert(rv.data,lo.data[i]*ro.data[1]) end
                    else
                        assert(lo.n_cols==ro.n_rows
                            ,"dMatrix __mul requires matrices where a.n_cols=b.n_rows")
                        rv.n_rows,rv.n_cols=lo.n_rows,ro.n_cols
                        for i=1, lo.n_rows do
                            for j=1, ro.n_cols do
                                local s=0.0
                                for k=1, lo.n_cols do s=s+lo{i,k}*ro{k,j} end
                                table.insert(rv.data,s)
                            end
                        end
                    end
                else
                        assert(lo.n_row==ro.n_rows and lo.n_cols==ro.n_cols
                            ,"dMatrix __add and __sub require matrices where a.n_cols=b.n_rows")
                        for i=1, #lo.data do
                            if oper==0 then
                                table.insert(rv.data,lo.data[i]+ro.data[i])
                            else
                                table.insert(rv.data,lo.data[i]-ro.data[i])
                            end
                        end
                end
            elseif lo.__class__ and lo.__class__==_dMatrix_ClassMT then
                    assert(lo.n_rows*lo.n_cols==#ro
                        ,"dMatrix (element-wise) __add, __sub, __mul, or __div  require a table with the same number of cells")
                    rv.n_rows,rv.n_cols=lo.n_rows,lo.n_cols
                        for i=1, #lo.data do
                            if oper==0 then
                                table.insert(rv.data,lo.data[i]+ro[i])
                            elseif oper==1 then
                                table.insert(rv.data,lo.data[i]-ro[i])
                            elseif oper==2 then
                                table.insert(rv.data,lo.data[i]*ro[i])
                            else
                                if ro[i]==0 then
                                    table.insert(rv.data,NULL)
                                else
                                    table.insert(rv.data,lo.data[i]/ro[i])
                                end
                            end
                        end
            else
                    assert(ro.n_rows*ro.n_cols==#lo
                        ,"dMatrix (element-wise) __add, __sub, __mul, or __div  require a table with the same number of cells")
                    rv.n_rows,rv.n_cols=ro.n_rows,ro.n_cols
                        for i=1, #lo.data do
                            if oper==0 then
                                table.insert(rv.data,lo[i]+ro.data[i])
                            elseif oper==1 then
                                table.insert(rv.data,lo[i]-ro.data[i])
                            elseif oper==2 then
                                table.insert(rv.data,lo[i]*ro.data[i])
                            else
                                if ro[i]==0 then
                                    table.insert(rv.data,NULL)
                                else
                                    table.insert(rv.data,lo[i]/ro.data[i])
                                end
                            end
                        end
            end
        end
        return rv
    end



dMatrix=AddToModuleHelp{
    dMatrix=[==[--[[--
            A constructor for a simple matrix-like class with dMatrix properties/methods.
--]]--]==]
-- @function dMatrix
    } .. 
function(a,...)
    local args=table.pack(...)
    local rv={}
    if a==nil then
        _dMatrix_set_size(rv,0,0)
    elseif #args==0 then
        if type(a)=="number" then
            _dMatrix_set_size(rv,a,a)
        elseif type(a)=="table" then
            if a.__class__ and a.__class__==_dMatrix_ClassMT then
                _dMatrix_set_size(rv,0,0)
                rv.data=wds.simple_copy(a.data)
                rv.n_rows=a.n_rows
                rv.n_cols=a.n_cols
            else 
                if #a==0 then
                    _dMatrix_set_size(rv,0,0)
                else
                    _dMatrix_set_size(rv,1,#a,a)
                end
            end
        end
    elseif type(a)=="number" and type(args[1])=="number" then
        _dMatrix_set_size(rv,a,args[1],args[2])
    end
    return setmetatable(rv,_dMatrix_ClassMT)
end

dZeros=AddToModuleHelp{
    dZeros=[==[--[[--
            A dMatrix call with zeros.
--]]--]==]
-- @function dZeros
} ..  function(a,b) return dMatrix(a,b,0.0) end

dOnes=AddToModuleHelp{
    dOnes=[==[--[[--
            A dMatrix call with ones.
--]]--]==]
-- @function dOnes
} ..  function(a,b) return dMatrix(a,b,1.0) end

dRandom=AddToModuleHelp{
    dRandom=[==[--[[--
            A dMatrix call filled with random().
--]]--]==]
-- @function dRandom
} ..  function(a,b) return dMatrix(a,b,math.random) end

sMatrix=AddToModuleHelp{
    sMatrix=[==[--[[--
            A random letter or word matrix.
--]]--]==]
-- @function sMatrix
} ..  function(a,b,l,fill,mx)
    if l==nil then l=1 end
    if fill==nil then fill=true end
    if mx==nil then mx=52 end
    local randomletter=function()
        local i=math.random(1,mx)
        if i<=26 then
            return string.char(64+i)
        else
            return string.char(70+i)
        end
    end
    local randomword=function()
        if l==1 then
            return randomletter()
        end
        local rv=""
        local ll=l
        if not fill then
            ll=math.random(1,l)
        end
        for i=1,ll do
            rv=rv..randomletter()
        end
        return rv
    end
    return dMatrix(a,b,randomword)
end


bIsdMatrix=AddToModuleHelp{
        bIsdMatrix=[==[--[[--
                A Boolean test for dMatrix.
--]]--]==]
-- @function bIsdMatrix
} ..  function(a)
        if type(a)~="table" then
            return false
        end
        if a.__class__ and a.__class__==_dMatrix_ClassMT then
            return true
        end
        if a.__classname__ and a.__classname__=="dMatrix" then
            return true
        end
        return false
    end

dMatrix_WrapOrRef=AddToModuleHelp{
        dMatrix_WrapOrRef=[==[--[[--
                Returns either a reference to an existing dMatrix or wraps something.
--]]--]==]
-- @function dMatrix_WrapOrRef
} ..  function(a,...)
        if bIsdMatrix(a) then
            return a
        else
            local rv=dMatrix():wrap(a,...)
            return rv
        end
    end

dMatrix_SimpleDiffVector=AddToModuleHelp{
        dMatrix_SimpleDiffVector=[==[--[[--
                Returns a difference sequence.
--]]--]==]
-- @function dMatrix_SimpleDiffVector
} ..  function(a,d)
        assert(bIsdMatrix(a) 
                or (a.n_rows==1 and a.n_cols==1) 
                or (a.n_rows>d and a.n_cols>d)
                ,"dMatrix_SimpleDiffVector requires a one dimensional matrix (single row or column).")
        local rv
        if a.n_rows==1 then
            rv=dZeros(a.n_rows,a.n_cols-d)
            for j in pesc.range(a.n_cols-d) do
                local jPd=j+d
                rv.data[j]=a[jPd]-a[j]
            end
        else
            rv=dZeros(a.n_rows-d,a.n_cols)
            for i in pesc.range(a.n_rows-d) do
                local iPd=j+d
                rv.data[i]=a[iPd]-a[i]
            end
        end
        return rv
    end

bIsNULLOrError=AddToModuleHelp{
        bIsNULLOrError=[==[--[[--
                A Boolean check for a nil, NULL, or Error object.
--]]--]==]
-- @function bIsNULLOrError
} .. function(obj)
    if obj==nil or NULL==obj then
        return true
    end
    local t=type(obj)
    if t=="number" and (obj~=obj or obj==math.huge or obj==-math.huge or obj==math.mininteger or obj==math.maxinteger) then
        return true
    elseif t=="string" and (wds.bIsEmpty(obj) or wds.bIn(obj:lower(),"error","err","na","n/a","nan","nil","null")) then
        return true
    end
    return false
end

bIsNULLOrErrorOrZero=AddToModuleHelp{
        bIsNULLOrErrorOrZero=[==[--[[--
                A Boolean check for nil, NULL, Error, or Zero object.
--]]--]==]
-- @function bIsNULLOrErrorOrZero
} .. function(obj)
    if obj==nil or NULL==obj or obj==0 then
        return true
    end
    local t=type(obj)
    if t=="table" then
        if obj.__classname__ and obj.__classname__=="dMatrix" then
            for i=1,#obj.data do if obj.data[i]~=0 and not(NULL==obj.data[i]) then return false end end
            return true
        elseif #obj>0 then
            for i=1,#obj do if obj[i]~=0 and not(NULL==obj[i]) then return false end end
            return true
        else
            return false
        end
    elseif t=="number" and (math.isnan(obj) or math.isinf(obj) or obj==math.mininteger) then
        return true
    elseif t=="string" and (wds.bIsEmpty(obj) or wds.bIn(obj:lower(),"0","zero","error","err","na","n/a","nan","nil","null")) then
        return true
    end
    return false
end


CDbl=AddToModuleHelp{
    CDbl=[==[--[--
            A safe conversion to a number or NULL.
--]]--]==]
-- @function CDbl
} .. function(obj)
    local rv
    local ok, msg=pcall(function() rv=tonumber(obj) end)
    if not ok then
        return NULL
    end
    return rv
end

bIsNumeric=AddToModuleHelp{
    bIsNumeric=[==[--[[--
            A Boolean check for a non-NULL numeric value.
--]]--]==]
-- @function bIsNumeric
} .. function(obj)
    if NULL==obj then
        return false
    end
    return type(obj)=="number"
end



return wds.EnvLock(_M)



