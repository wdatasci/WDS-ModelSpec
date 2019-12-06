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

local args_opts=require("WDS.Util.args_opts")
local arts=require("WDS.Comp.Artificials")
local pesc=require("WDS.Util.python_esc")
local mat=require("WDS.Comp.Matrix")


math.randomseed(os.time())


local is_main=wds.is_main(arg)
print("is_main=",is_main)
print("arg=",wds.show(arg))

--print("dir()=") dir()

if is_main then

    options=args_opts.ArgumentParser('usual')
    opts_rv1, opts_rv2=options:parse(arg)
    if opts_rv1.help then
        options:help()
        print()
        print("Module help()")
        print(wds.help(arts))
        os.exit()
    end

    wds.AddToEnv(_ENV,{
        fVariableMatter=arts.fVariableMatter
        , fArtificialsCount=arts.fArtificialsCount
        , fArtificials=arts.fArtificials
        , fArtificialsScored=arts.fArtificialsScored
        , fArtificialsLabels=arts.fArtificialsLabels
        , eTreatment=arts.eTreatment
        , dMatrix=mat.dMatrix
        , dRandom=mat.dRandom
    })

    V1=fVariableMatter{
            Treatment="Hats"
            , CriticalValues={ 3, 10, 25, 120 }
            , CleanLimits={ -1, 150 }
        }
    V1_ncols=fArtificialsCount{
            Treatment="Hats"
            , CriticalValues={ 3, 10, 25, 120 }
            , CleanLimits={ -1, 150 }
        }
    print("V1=",wds.show(V1))
    print("V1_ncols=",wds.show(V1_ncols))
    print("V1.ncols=",wds.show(fArtificialsCount{VariableMatter=V1}))
    
    print()
    print("V1 artificial labels=",wds.show(fArtificialsLabels{VariableMatter=V1,VariableBaseName="V1Name"}))
    print("V1 artificial labels=",wds.show(fArtificialsLabels{VariableMatter=V1,Name="V1Name",Separator="_"}))


    print()
    X=pesc.list(pesc.range(-10,10,.5))
    print("X=",wds.show(X))
    XW=dMatrix()
    XW:print("XW:")
    XW:wrap(X,{SingleColumn=true})
    XW[{3,1}]=NULL
    --pesc.list(pesc.range(-10,10,.1)),{Rowwise=True})
    XW:print("XW:")

    print("huh?")

    XA=fArtificials{Input=XW
        , Treatment="Hats"
        , CriticalValues={-6, 2.35, 6, 9}
    }


    XA:print("XA:")

    --q()

local gp = require('gnuplot')

if true then

--for iT,T in pairs({"None","Constant","Hats","Levels","iHats","BZ2","BZ3"}) do
for iT,T in pairs({"Categorical","CategoricalNumeric","Hats","Levels","DiscreteRC","DiscreteLC","iHats","BZ2","BZ3"}) do

    print("T=",T)

    V1=fVariableMatter{
            Treatment=T
            , CriticalValues={ -6, -1, 3, 6, 8, 9 }
            , CleanLimits={ -8, 10.5 }
        }
    print("V1=",wds.show(V1))
    V1.CritVals:print("V1.CritVals:")
    --V1.CleanLimits:print("V1.CleanLimits:")
    --q()
    print("V1=",wds.show(V1))
    V1_n_cols=fArtificialsCount{Treatment=V1.Treatment, CriticalValues=V1.CritVals}
    print("V1_n_cols=",wds.show(V1_n_cols))
    
    XW:print("XW:")
    XA=fArtificials{Input=XW,VariableMatter=V1}
    XA:print("XA:")


    XAFL=fArtificialsLabels{Treatment=V1.Treatment, CriticalValues=V1.CritVals, CleanLimits=V1.CleanLimits, VariableNameBase="X"}
    XAF=function(x,j)
                -- xa=fArtificials{Input={x},VariableMatter=V1}
                if V1.iArtVar_First<=j and j<=V1.iArtVar_Last then
                    xa=fArtificials{Input={x},VariableMatter=V1}
                    --print("x=",x)
                    --xa:print("xa:")
                    if V1.iArtVar_First==0 then
                        return xa.data[j+1]
                    else
                        return xa.data[j]
                    end
                else
                    return nil
                end
            end

    Coef=2-4*dRandom(3,V1_n_cols)
    for i in pesc.range(1,V1_n_cols) do
        print("i=",i)
        Coef[{1,i}]=1.0
    end
    Coef:print("Coef=")
    print("Coef=",wds.show(Coef))
    print("Coef=",wds.show(Coef))
    XAFS=function(x,j)
                -- xa=fArtificials{Input={x},VariableMatter=V1}
                if V1.iArtVar_First<=j and j<=V1.iArtVar_Last then
                    xa=fArtificialsScored{Input={x},VariableMatter=V1,CoefficientValues=Coef}
                        return xa.data[j]
                else
                    return nil
                end
            end

    --XA1=pesc.list(XA{{},1})
    --XA2=pesc.list(XA{{},2})
    --XA3=pesc.list(XA{{},3})
    --XA4=pesc.list(XA{{},4})
    --print(wds.show(XA1))
    --print(wds.show(XA2))
    --print(wds.show(XA3))
    --print(wds.show(XA4))


    --[[
    gp_data={
        gp.array{ {XW.data, AX2} }
    }
    for i in pesc.range(V1.iArtVar_First,V1.iArtVar_Last) do
        print("Adding column ",i)
        table.insert(gp_data,gp.func { function(x) return XAF(x,i) end, range={-10, 10, .2}, with='lines' })
    end
    --]]

yrange="[-5:5]"
if V1.Treatment==arts.eTreatment.iHats then
    yrange="[-5:20]"
elseif V1.Treatment==arts.eTreatment.None then
    yrange="[-12:12]"
end

local g = gp{
    width  = 640,
    height = 480,
    xlabel = "X axis",
    ylabel = "Y axis",
    --key    = "top left",
    key    = "outside nobox opaque center right width 0.5",
    consts = { gamma = 2.5 },
    xrange = "[-11:11]",
    yrange = yrange,
    data = 
    {
        --gp.array { {XW.data, XA1} }
        --, gp.array { {XW.data, XA2} }
        --, gp.array { {XW.data, XA3} }
        --, 
          gp.func { function(x) return XAF(x,0) end, range={-10, 10, .01}, with='lines', title=XAFL[1] }
        , gp.func { function(x) return XAF(x,1) end, range={-10, 10, .01}, with='lines', title=XAFL[2] }
        , gp.func { function(x) return XAF(x,2) end, range={-10, 10, .01}, with='lines', title=XAFL[3] }
        , gp.func { function(x) return XAF(x,3) end, range={-10, 10, .01}, with='lines', title=XAFL[4] }
        , gp.func { function(x) return XAF(x,4) end, range={-10, 10, .01}, with='lines', title=XAFL[5] }
        , gp.func { function(x) return XAF(x,5) end, range={-10, 10, .01}, with='lines', title=XAFL[6] }
        , gp.func { function(x) return XAF(x,6) end, range={-10, 10, .01}, with='lines', title=XAFL[7] }
        , gp.func { function(x) return XAF(x,7) end, range={-10, 10, .01}, with='lines', title=XAFL[8] }
        , gp.func { function(x) return XAF(x,8) end, range={-10, 10, .01}, with='lines', title=XAFL[9] }
        , gp.func { function(x) return XAFS(x,1) end, range={-10, 10, .01}, with='lines', title="Score 1" }
        , gp.func { function(x) return XAFS(x,2) end, range={-10, 10, .01}, with='lines', title="Score 2" }
        , gp.func { function(x) return XAFS(x,3) end, range={-10, 10, .01}, with='lines', title="Score 3" }
    }    
}:plot('output.'..T..'.png')


--q()
    
end

end



sdata=mat.dLetterMatrix(20,1,1,nil,26)

sdata:print("sdata:")


V2=fVariableMatter{Treatment=eTreatment.Categorical
    , CriticalValues={ {"A","Z"}, "C", "D" }
}
V2.CritVals:print("V2.CritVals:")
V2:print("V2:")
XS=fArtificials{Input=sdata,VariableMatter=V2}

tmp=sdata .. XS
tmp:print("sdata .. XS:")


V2=fVariableMatter{Treatment=eTreatment.Categorical
    , CriticalValues="  A|B|C E|F G H"
}
V2.CritVals:print("V2.CritVals:")
V2:print("V2:")
XS=fArtificials{Input=sdata,VariableMatter=V2}

tmp=sdata .. XS
tmp:print("sdata .. XS:")




    

end
    

