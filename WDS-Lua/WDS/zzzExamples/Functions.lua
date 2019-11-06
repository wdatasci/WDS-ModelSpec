--[[
    1: basic function examples
    2: passing functions
    3: lambdas
    4: decorators
--]]


local arg 
arg=table.pack(...)

local module_name_dots=( ... or "main-call-without-args" )
-- to hard-code use.......
local module_name="examples.Functions"

wds=require("WDSUtil.WDS")
wdspylike=require("WDSUtil.python_esc")




--[[
def NPV( discount_rate  #constant
        ,arg1  # array of values
        ):
    ''' 
        simple npv calc,
        discount_rate is per-period
        arg1 is an iterable array of values where discount_rate is applied at the end of each period
        '''
    s=0
    for i,v in enumerate(arg1):
        s+=(0.0+v)/(1.0+discount_rate)**(i+1.0)
    return s
--]]

NPV=function(...)
    local arg_=table.pack(...)
    if #arg_==1 and type(arg_[1])=="string" and arg_[1]=="info.doc" then
        return [[
        simple npv calc,
        discount_rate is per-period
        arg1 is an iterable array of values where discount_rate is applied at the end of each period
        ]]
    end
    if #arg_==1 then
        if type(arg_[1])=="table" then
            arg_=arg_[1]
        else 
            error("Hey, expecting either a 'info.doc' input or {discount_rate, data}")
        end
    end
    local s=0.0
    local discount_rate=tonumber(arg_.discount_rate or arg_[1])
    for i,v in ipairs(arg_.data or arg_[2]) do
        s=s+(0.0+tonumber(v))/(1.0+discount_rate)^((i-1)+1.0)
    end
    return s
end


NPV2=function(...)
    local arg_=table.pack(...)
    if #arg_==1 and type(arg_[1])=="string" and arg_[1]=="info.doc" then
        return [[ 
            simple npv calc, without iterator
            ]]
    end
    if #arg_==1 and type(arg_[1])=="table" then
        arg_=arg_[1]
    end
    -- print("wds.show(arg_)")
    -- print(wds.show(arg_))
    local discount_rate=arg_.discount_rate or arg_[1]
    local arg1=arg_.data or arg_[2]
    local verbose=arg_.verbose or false
    local l=0
    if arg1 ~= nill then
        l=#arg1
    end
    --x=list(range(l))
    local x=wdspylike.list_range(l)
    if verbose then
        print(x)
    end
    local y
    --if verbose then
        --y=np.array(list(range(l)),dtype=np.double)
        y=wdspylike.list_range(l)
    --end
    if verbose then
        print(y)
    end
    --if verbose then
        --y=(1.0+np.array(list(range(l)),dtype=np.double))
        -- lua is not automatically vector based
        for i,v in ipairs(y) do
            y[i]=(1.0+y[i])
        end
    --end
    if verbose then
        print(y)
    end
    --if verbose then
        -- lua is not automatically vector based
        --y=(1.0+discount_rate)**(1.0+np.array(list(range(l)),dtype=np.double))
        for i,v in ipairs(y) do
            y[i]=(1.0+discount_rate)^(y[i])
        end
    --end
    if verbose then
        print(y)
    end
    --y=np.array(arg1,dtype=np.double)/((1.0+discount_rate)**(1.0+np.array(list(range(l)),dtype=np.double)))
    for i,v in ipairs(y) do
        y[i]=arg1[i]/y[i]
    end
    if verbose then
        print(y)
    end
    --y=sum(y)
    local ys=0.0
    for i,v in ipairs(y) do
        ys=ys+v
    end
    if verbose then
        print(ys)
    end
    return ys
end

NPV_FirstDerivative=function(...)
    local arg_=table.pack(...)
    if #arg_==1 then
        if arg_[1]=="info.doc" then
            return [[ 
            simple npv calc, without iterator
            ]]
        end
    end
    if #arg_==1 and type(arg_[1])=="table" then arg_=arg_[1] end
    local discount_rate=arg_.discount_rate or arg_[1]
    local arg1=arg_.data or arg_[2]
    local l=#arg1
    --x=list(range(l))
    local x=wdspylike.list_range(l)
    local y={}
    local ys=0.0
    for i=1,l do
        local yi=arg1[i]*(-i)/( (1.0+discount_rate)^(1.0+i) )
        table.insert(y,yi)
        ys=ys+y[i]
    end
    return ys
end

-- this is not generalized, this is just for a code example

InvF=function(...)
    local arg_=table.pack(...)
    if #arg_==1 and type(arg_[1])=="table" then arg_=arg_[1] end
    if type(arg_)=="string" and arg_=="info.doc" then
        return [[InvF( target    #goal value to find to find
            ,initial_guess  #starting point
            ,arg1           #array of values
            ,fnc            #function to use
            ,fnc_deriv=None #function inverse to use if available
            ,eps=1.0e-6     #acceptible target difference
            )
        returns the discount rate which solves target=fnc(result,arg1)
        ]]
    end
    local target=arg_.target or arg_[1]  -- target    #goal value to find to find
    local initial_guess=arg_.initial_guess or arg_[2] --  #starting point
    local arg1=arg_.arg1 or arg_[3] --           #array of values
    local fnc=arg_.fnc or arg_[4] --            #function to use
    local fnc_deriv=arg_.fnc_deriv or arg_[5] -- =None #function inverse to use if available
    local eps=arg_.eps or arg_[6] or 1.0e-6  --     #acceptible target difference
    local verbose=arg_.verbose or arg_[7] or false   -- False  #to turn on prints

    local xnp1=initial_guess
    local fxnp1=fnc(xnp1,arg1)
    local diff=target-fxnp1

    --if math.fabs(diff)<eps:
        --return xnp1
    if math.abs(diff)<eps then
        return xnp1
    end

    use_deriv=(fnc_deriv ~= nil) --is not None

    if use_deriv then
        xn=initial_guess/2.0
        fxn=fnc(xn,arg1)
    end

    i=-1
    while math.abs(diff) > eps do
        i=i+1
        xn=xnp1
        --don't forget that "if i then" for "i==0" evaluates as true
        --"if i then" evaluates as false only for i==false or i==nil
        if i>0 then
            fxn=fxnp1
        else
            fxn=fnc(xn,arg1)
        end
        if use_deriv then
            fpxn=fnc_deriv(xn,arg1)
            if math.abs(fpxn)<=eps then
                error('near-zero derivative encountered at '..xn)
            end
        else
            huh=1
        end
        --since we are finding the root, the target function is actually fnc-target
        --which does not contribute to derivative
        xnp1=xn-(fxn-target)/fpxn
        fxnp1=fnc(xnp1,arg1)
        diff=target-fxnp1
        if verbose then
            print("xn=",xn)
        end
        if verbose then
            print("fxn=",fxn)
        end
        if verbose then
            print("fpxn=",fpxn)
        end
        if verbose then
            print("xnp1=",xnp1)
        end
        if verbose then
            print("fxnp1=",xnp1)
        end
        if verbose then
            print("diff=",diff)
        end
    end


    return (xnp1)
end



--for a closure example
--here, I am thinking of a closure as the result of something like 
--a builder programming pattern

local WhatBuilder
WhatBuilder=function (arg1, arg2)
    local s=0
    return function(arg_) s=s+arg_ print("internal s=",s) return arg_*arg1+s+arg2 end
end



if module_name_dots=="main-call-without-args" or wds.is_main(table.pack(arg)) then
    print("testing in "..module_name)
    a={10,11,12,13,14}
    print("a="..wds.show(a))
    r=0.01
    print("r=",r)
    print("npv=NPV(r,a)=",NPV{r,a})
    print("using verbose setting in NPV2")
    --y=NPV2(r,a,verbose=True)
    y=NPV2{discount_rate=r,arg1=a,verbose=true}
    print("npv=NPV2(r,a)=",NPV2{discount_rate=r,arg1=a,verbos=true})
    target_value=50.0
    initial_guess=-0.01
    print("target_value=",target_value)
    print("initial_guess=",initial_guess)
    y=InvF{target=target_value,initial_guess=initial_guess,arg1=a,fnc=NPV2,fnc_deriv=NPV_FirstDerivative}
    print("target=",type(target_value))
    print("initial_guess=",type(initial_guess))
    print("arg1",type(a))
    print("fnc=",type(NPV2))
    print("fnc_deriv=",type(NPV_FirstDerivative))
    y=InvF{target=target_value,initial_guess=initial_guess,arg1=a,fnc=NPV2,fnc_deriv=NPV_FirstDerivative}
    print("y=InvF(target_value,initial_guess,a,NPV2,NPV_FirstDerivative)=",y)

    print("using a lambda as the function:")

    --f=lambda discount_rate, arg1: sum(np.array(arg1,dtype=np.double)/((1.0+discount_rate)**(1.0+np.array(list(range(len(arg1))),dtype=np.double))))
    f=function(discount_rate, arg1) 
        local s=0.0
        for i,v in ipairs(arg1) do
            s=s+arg1[i]/(1.0+discount_rate)^(i)
        end
        return s
    end
    --fderiv=lambda discount_rate, arg1: sum(np.array(arg1,dtype=np.double)*(-(1.0+np.array(list(range(len(arg1))),dtype=np.double)))
    --                                          /((1.0+discount_rate)**(2.0+np.array(list(range(len(arg1))),dtype=np.double))))
    fderiv=function(discount_rate, arg1)
        local s=0.0
        --for i,v in ipairs(arg1) do
        for i=1,#arg1 do
            s=s+arg1[i]*(-i)/( (1.0+discount_rate)^(1.0+i) )
        end
        return s
    end
    print("f=",f)
    print("npv=f(r,a)=",f(r,a))
    y=InvF{target=target_value,initial_guess=initial_guess,arg1=a,fnc=f,fnc_deriv=fderiv}
    print("y=InvF(target_value,initial_guess,a,f,fderiv)=",y)

    print()

    print("closure example")
    print("f1=WhatBuilder(3,4)")
    f1=WhatBuilder(3,4)
    print("f2=WhatBuilder(1,2)")
    f2=WhatBuilder(1,2)
    print("f1 - runs")
    print("f1(1,3)=",f1(1,3))
    print("f1(1,3)=",f1(1,3))
    print("f1(1,3)=",f1(1,3))
    print("f2 - runs")
    print("f2(1.1,3)=",f2(1.1,3))
    print("f2(1.1,3)=",f2(1.1,3))
    print("f2(1.1,3)=",f2(1.1,3))
    print("f1 - runs")
    print("f1(1,3)=",f1(1,3))
    print("f1(1,3)=",f1(1,3))
    print("f1(1,3)=",f1(1,3))
    print("f2 - runs")
    print("f2(1,3)=",f2(1,3))
    print("f2(1.1,3)=",f2(1.1,3))
    print("f2(1.1,3)=",f2(1.1,3))


    print()


    print('fin')
        
end





