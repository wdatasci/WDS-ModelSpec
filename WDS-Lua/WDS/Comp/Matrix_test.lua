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

--- A test of WDS.Comp.Matrix
-- @within WDS.Comp
-- @script Matrix_test

local wds=require("WDS")
local wdsu=require("WDS.Util")
local pesc=require("WDS.Util.python_esc")
local mat=require("WDS.Comp.Matrix")

local args_opts=require("WDS.Util.args_opts")
options=args_opts.ArgumentParser('usual')
opts_rv1, opts_rv2=options:parse(arg)
if opts_rv1.help then
    options:help()
    print()
    print("Module help()")
    print(wds.help(mat))
    os.exit()
end


x=mat.NULL
y=mat.NULL
print("x=",x)
print("type(x)=",type(x))
print("x()=",x())
print("wds.show(x)=",wds.show(x))
print("tostring(x)=",tostring(x))
print("x==y",x==y)
print(x)
print(y)

--making a few things global
wds.AddToEnv(_G,{NULL=mat.NULL,dMatrix=mat.dMatrix})

z=NULL
print("z==x",z==x)
w=x
print("w=",w)


A=dMatrix(2,3)
print("A.n_rows=",A.n_rows)
print("A.n_cols=",A.n_cols);
print("dMatrix=",wds.show(dMatrix))

--A(1,2)=456.0
A[{1,2}]=456.0
xx=A{1,2}
xx=A(1,2)
xx=A[{1,2}]
A:print("A:")
print("xx=",xx)
xx=73
A:print("A:")
print("xx=",xx)
A:fill(5)
A:print("A:")

    A:reset_cellptr();

    _= A << 0.3
    _= A << 0.3

    A:print("A:")

    A:reset_cellptr()

    _= A << 0.7
    _= (A << 0.7) << .9
    _= A << 0.7 << .9

    A:print("A:")

    A:set_size(5,5)

	_=A << 0.165300 << 0.454037 << 0.995795 << 0.124098 << 0.047084 << mat.endr
		<< 0.688782 << 0.036549 << 0.552848 << 0.937664 << 0.866401 << mat.endr
		<< 0.348740 << 0.479388 << 0.506228 << 0.145673 << 0.491547 << mat.endr
		<< 0.148678 << 0.682258 << 0.571154 << 0.874724 << 0.444632 << mat.endr
		<< 0.245726 << 0.595218 << 0.409327 << 0.367827 << 0.385736 << mat.endr;

    A:print("A:")


    A:fill(111)

	_=A << 0.165300 << 0.454037 << mat.endr << 0.995795 << 0.124098 << 0.047084 << mat.endr
		<< 0.688782 << 0.036549 << 0.552848 << 0.937664 << 0.866401 << mat.endr
		<< 0.348740 << 0.479388 << 0.506228 << 0.145673 << 0.491547 << mat.endr
		<< 0.148678 << mat.endr << 0.682258 << 0.571154 << 0.874724 << 0.444632 << mat.endr
		<< 0.245726 << 0.595218 << 0.409327 << 0.367827 << 0.385736 << mat.endr;

    _=A << mat.begin_mat
        << 1 << 2 << 3 << mat.endr
        << 4
        << mat.end_mat;

    A:print("A:")

    _=A << mat.begin_mat
        << 1 << 2 << 3 << mat.endr
        << mat.end_mat;

    A:print("A:")

    _=
        A << mat.begin_mat << { 1, 3, 7, 103, 88 } << mat.endr << { 34, 99} << mat.end_mat;

    A:print("A:")


    c={1,3,5,8}
    print("c=",wds.show(c))

    B=dMatrix():wrap(c)
    B:print("B:")

    c[2]=345
    print("c=",wds.show(c))
    B:print("B:")
    B[{1,3}]=456
    print("c=",wds.show(c))
    B:print("B:")
    c=nil
    print("c=",wds.show(c))
    B:print("B:")


    _=A << mat.begin_mat
        << 1 << 2 << 3 << mat.endr
        << 4
        << mat.end_mat;

    A:print("A:")

	_=A << mat.begin_mat 
        << 0.165300 << 0.454037 << 0.995795 << 0.124098 << 0.047084 << mat.endr
		<< 0.688782 << 0.036549 << 0.552848 << 0.937664 << 0.866401 << mat.endr
		<< 0.348740 << 0.479388 << 0.506228 << 0.145673 << 0.491547 << mat.endr
		<< 0.245726 << 0.595218 << 0.409327 << 0.367827 << 0.385736 << mat.endr
        << mat.end_mat;

    A:print("A:")

    for j in pesc.range(1,A.n_cols) do
        print("Column ",j)
        for i in A{{},j} do
            print("i=",i)
        end
    end

    for i in pesc.range(A.n_rows) do
        print("row ",i)
        for j in A{i,{}} do
            print("j=",j)
        end
        r=pesc.list(A{i,{}})
        print("r=",wds.show(r))
    end

    A:print("A:")
    print("B=A:t()")
    B=A:t()
    B:print("B:")

    C=mat.dRandom(3,5)
    C:print("C:")

    D=2*C
    D:print("D:")

    D=D*2
    D:print("D:")

    D=D*2+10
    D:print("D:")

    C=-4*mat.dRandom(3,5)+2
    C:print("C:")


    C=mat.dRandom(4,4)
    C:print("C:")

    D=mat.dRandom(4,4)
    D:print("D:")

    E=C*D
    E:print("E:")

    EE=C*D.data
    EE:print("EE:")

    L=mat.sMatrix(4,4)
    L:print("L:")

    L2=L..L
    L2:print("L2:")

    L=mat.sMatrix(4,4,4)
    L:print("L:")

    L=mat.sMatrix(4,4,4,false)
    L:print("L:")

    L=mat.sMatrix(4,4,4,nil,20)
    L:print("L:")




