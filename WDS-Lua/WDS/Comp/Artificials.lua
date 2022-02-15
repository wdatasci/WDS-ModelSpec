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

--- A pure-lua implementation of the WDS standard Artificial variable handling set.
-- @submodule WDS.Comp


local wds=require("WDS")
local wdsu=require("WDS.Util")

local module_name_dots=( ... or "main-call-without-args" )
local module_name="WDS.Comp.Artificials"

if module_name_dots=="main-call-without-args" or wds.bIsMain(table.pack(...),module_name) then
    print("test with "..string.gsub(module_name,"%.","/").."_test.lua")
    wds.q()
end

local module_path=""
local dbg
if __NO_DEBUG__==nil then
    module_path=debug.getinfo(1,"S").source
    dbg=require("debugger")
    dbg.auto_where=2
else
    dbg=function() end
end

local mat=require("WDS.Comp.Matrix")
local pesc=require("WDS.Util.python_esc")

-- swapping _ENV/_G to restrict everything to this module, but the
-- usual suspects will need to be accessed through _G

local _M={}
local _G=_G
_ENV=wds.EnvExtension(_M,_G)

wds.AddToEnv(_ENV,{NULL=mat.NULL,dMatrix=mat.dMatrix,dMatrix_WrapOrRef=mat.dMatrix_WrapOrRef})

-- A simplified way of providing an info element which the help function

info={name=module_name
    ,path=module_path
    ,doc=module_name .. " ("..module_path..")"..[==[
    A pure-lua implementation of the WDS standard Artificial variable handling set.
    For this module, arguments will either be positional, as in f(a,b,c,d),
    or optional, as in f{a=a,b=b,c=c,d=d}.  Any mixed will treat all non-named
    first, and later optionals as overrides, as in f{a,c=b,d}=f{a=a,b=d,c=b,d=nil).
    ]==]
    ,docmap={}
}

-- for code consistency with VBA
WDSContextID = 40003
WDSModuleName = module_name

-- local decorator for this module
local AddToModuleHelp=function(tbl); tbl.info=info; return wds.AddToModuleHelp(tbl); end


eTreatment=AddToModuleHelp{
        eTreatment=[==[--[[--
                An EnumLike object for artificial treatment types.
--]]--]==]
-- @table eTreatment
} ..
    wds.EnumLike{

      Unknown = -1
    , None = 0
    , Constant = 1
    , CodedMissings = 2
    , DiscreteLC = 3
    , DiscreteRC = 4
    , Hats = 5
    , iHats = 6
    , BSplineOrder2 = 7
    , BSplineOrder3 = 8
    , Categorical = 9
    , CategoricalNumeric = 10

    , __aliases__={
        Straight="None"
        , Numeric="None"
        , Missings="CodedMissings"

        , BucketsLC="DiscreteLC"
        , LevelsLC="DiscreteLC"
        , DiscretizeLC="DiscreteLC"
        , IntervalsLC="DiscreteLC"
        , DiscLC="DiscreteLC"
        , BZ0LC="DiscreteLC"
        , BSO0LC="DiscreteLC"
        , CAGLAD="DiscreteLC"
        , COLLOR="DiscreteLC"
        , LCRL="DiscreteLC"

        , BucketsRC="DiscreteRC"
        , LevelsRC="DiscreteRC"
        , DiscretizeRC="DiscreteRC"
        , IntervalsRC="DiscreteRC"
        , DiscRC="DiscreteRC"
        , BZ0RC="DiscreteRC"
        , BSO0RC="DiscreteRC"
        , CADLAG="DiscreteRC"
        , CORLOL="DiscreteRC"
        , RCLL="DiscreteRC"

        , Buckets="DiscreteRC"
        , Levels="DiscreteRC"
        , Discretize="DiscreteRC"
        , Intervals="DiscreteRC"
        , Disc="DiscreteRC"
        , BZ0="DiscreteRC"
        , BSO0="DiscreteRC"

        , BZ1="Hats"
        , BSO1="Hats"
        , IntegratedHats="iHats"
        , BSplineO2="BSplineOrder2"
        , BZ2="BSplineOrder2"
        , BSO2="BSplineOrder2"
        , BSplineO3="BSplineOrder3"
        , BZ3="BSplineOrder3"
        , BSO3="BSplineOrder3"
        , Cat="Categorical"
        , String="Categorical"
        , NCat="CategoricalNumeric"
        , NCategorical="CategoricalNumeric"
    }
}

tVariableMatter=wds.AddToModuleHelp{
    tVariableMatter=[==[--[[--
            The return type of fVariableMatter.
--]]--]==]
-- @function tVariableMatter
,info=info } ..  wds.nilable_instance_of({

        Name=""
        , Handle=""
        , ArtBaseName=""
    
        , Treatment = eTreatment.Unknown --As eTreatment

        , CleanLimits={__nil__=true}
        , bUseCLLeft =false --As Boolean
        , bUseCLRight =false --As Boolean


        , CritVals={__nil__=true}
        , nCritVals =0 --As Integer
        , nCritValRows =0 --As Integer

        , nArtVars=0
        , iArtVar_First =0 --As Integer
        , iArtVar_Last =0 --As Integer
        , ArtVarLabels={__nil__=true}

        , CoefVals={__nil__=true}
        
        , __classname__ = "tVariableMatter"
    
    },{
        print=function(self,title)

            if title then
                _G.print(title)
            end

            if self.Name and #self.Name>0 then _G.print("   Name: "..self.Name) end
            if self.Handle and #self.Handle>0 then _G.print("   Handle: "..self.Handle) end
            if self.ArtBaseName and #self.ArtBaseName>0 then _G.print("   ArtBaseName: "..self.ArtBaseName) end
            if self.CleanLimits and self.CleanLimits~=NULL then _G.print("   CleanLimits: "..wds.show(self.CleanLimits,{},2)) end
            if self.bUseCLLeft then _G.print("    bUseCLLeft: "..self.bUseCLLeft,"",2) end
            if self.bUseCLRight then _G.print("    bUseCLRight: "..self.bUseCLRight,"",2) end
            if self.CritVals and self.CritVals~=NULL then self.CritVals:print("   CritVals: ","",2) end
            _G.print("    nCritVals: "..self.nCritVals)
            _G.print("    nCritValRows: "..self.nCritValRows)
            _G.print("    nArtVars: "..self.nArtVars)
            _G.print("    iArtVar_First: "..self.iArtVar_First)
            _G.print("    iArtVar_Last: "..self.iArtVar_Last)
            if self.ArtVarLabels and self.ArtVarLabels~=NULL then _G.print("   ArtVarLabels: "..wds.show(self.ArtVarLabels,2)) end
            if self.CoefVals and self.CoefVals~=NULL then self.CoefVals:print("   CoefVals: ","",2) end

            if self.__classname__ and #self.__classname__>0 then _G.print("   __classname__: "..self.__classname__) end

        end
    })

-- fVarArgs is a local helper function to handle positional or optional processing.
local fVarArgs=function(positional_order,...)
        local args=_G.table.pack(...)
        --_G.print("positional_order=",wds.show(positional_order))

        --first, is ... already 'packed', if so, there is only one argument, it 
        --has a count, and it does not have a class
        if #args==1 and _G.type(args[1])=="table" and args[1].__classname__==nil and args[1].__class__==nil then
            args=args[1]
        end
        --_G.print("args=",wds.show(args))
        --_G.print("args=",wds.show(args,2))
        local n=#args
        if n==0 then -- nothing to take as positional
            return args
        end
        local rv={}
        local args_i={}
        if n>0 then
            args_i=pesc.list(pesc.range(1,n))
            for _,i in _G.pairs(args_i) do
                if positional_order[i] and args[positional_order[i]]==nil then
                    rv[positional_order[i]]=args[i]
                end
            end
        end
        -- take any other named arguments
        for k,v in _G.pairs(args) do
            if args_i[k]==nil then
                rv[k]=v
            end
        end
        --_G.print("rv=",wds.show(rv,2))
        return rv
    end



local fVariableMatter_Args={"Treatment","CriticalValues","CleanLimitLeftValue","CleanLimitRightValue","CoefficientsValues"}

fVariableMatter=AddToModuleHelp{
        fVariableMatter=[==[--[[--
                Evaluate all of the usual constants associated with a treatment.
--]]--]==]
-- @function fVariableMatter
} ..  function(...)
        local args=fVarArgs(fVariableMatter_Args,...)
        --_G.print("args=",wds.show(args,2))
        local Treatment=args.Treatment
        local CleanLimitLeftVal=args.CleanLimitLeftVal
        local CleanLimitRightVal=args.CleanLimitRightVal
        local CleanLimits=args.CleanLimits
        if CleanLimits then
            CleanLimitLeftVal=CleanLimitLeftVal or CleanLimits[1]
            CleanLimitRightVal=CleanLimitRightVal or CleanLimits[2]
        end
        if CleanLimitLeftVal and _G.type(CleanLimitLeftVal)=="table" and #CleanLimitLeftVal==2 then
            CleanLimitRightval=CleanLimitRightVal or CleanLimitLeftVal[2]
            CleanLimitLeftVal=CleanLimits[1]
        end

        local rv=tVariableMatter.new



        rv.Treatment=eTreatment(Treatment)

        local tCritVals=_G.type(args.CriticalValues)
        if not(wds.bIn(rv.Treatment, eTreatment.Categorical, eTreatment.CategoricalNumeric)) then
            if tCritVals=="table" then
                rv.CritVals=mat.dMatrix_WrapOrRef(args.CriticalValues,{SingleRow=true})
            elseif tCritVals=="string" then
                rv.CritVals=mat.dMatrix_WrapOrRef(wds.string_split(args.CriticalValues," ",true,true),{SingleRow=true})
                for i=1,#rv.CritVals.data do
                   rv.CritVals.data[i]=_G.tonumber(rv.CritVals.data[i])
                end
            elseif tCritVals=="number" then
                rv.CritVals=mat.dMatrix_WrapOrRef({args.CriticalValues},{SingleRow=true})
            end
        else
            if tCritVals=="table" then
                rv.CritVals=mat.dMatrix_WrapOrRef(args.CriticalValues)
            elseif tCritVals=="string" then
                rv.CritVals=mat.dMatrix_WrapOrRef(wds.string_split(args.CriticalValues," ",true,true),{SingleRow=true})
                for i=1,#rv.CritVals.data do
                    if _G.string.find(rv.CritVals.data[i],"|") then
                        rv.CritVals.data[i]=mat.dMatrix_WrapOrRef(wds.string_split(rv.CritVals.data[i],"|",true,true))
                    end
                end
            elseif tCritVals=="number" then
                if rv.Treatment=="Categorical" then
                    rv.CritVals=mat.dMatrix_WrapOrRef({tostring(args.CriticalValues)},{SingleRow=true})
                else
                    rv.CritVals=mat.dMatrix_WrapOrRef({args.CriticalValues},{SingleRow=true})
                end
            end
        end
        rv.nCritVals = rv.CritVals.n_cols
        rv.bUseCLLeft = CleanLimitLeftVal~=nil and not ( NULL==CleanLimitLeftVal )
        rv.bUseCLRight = CleanLimitRightVal~=nil and not ( NULL==CleanLimitRightVal )

        rv.CleanLimits={CleanLimitLeftVal or mat.NULL, CleanLimitRightVal or mat.NULL}

        rv.nArtVars = 1
        rv.iArtVar_First = 0
        rv.iArtVar_Last = 1


        if rv.Treatment==eTreatment.Hats then
            rv.nCritValRows=1
            rv.nArtVars = rv.nCritVals + 1
            rv.iArtVar_Last=rv.nArtVars-1
        elseif rv.Treatment==eTreatment.DiscreteLC then
            rv.nCritValRows=1
            rv.nArtVars = rv.nCritVals + 2
            rv.iArtVar_Last=rv.nArtVars-1
        elseif rv.Treatment==eTreatment.DiscreteRC then
            rv.nCritValRows=1
            rv.nArtVars = rv.nCritVals + 2
            rv.iArtVar_Last=rv.nArtVars-1
        elseif rv.Treatment==eTreatment.iHats then
            rv.nCritValRows=1
            rv.nArtVars = rv.nCritVals + 1
            rv.iArtVar_Last=rv.nArtVars-1
        elseif rv.Treatment==eTreatment.BSplineOrder2 then
            rv.nCritValRows=1
            rv.nArtVars = rv.nCritVals
            rv.iArtVar_Last=rv.nArtVars-1
        elseif rv.Treatment==eTreatment.BSplineOrder3 then
            rv.nCritValRows=1
            rv.nArtVars = rv.nCritVals - 1
            rv.iArtVar_Last=rv.nArtVars-1
        elseif rv.Treatment==eTreatment.Categorical then
            rv.nCritValRows = rv.CritVals.n_rows
            rv.nArtVars = rv.nCritVals + 1
            rv.iArtVar_Last=rv.nArtVars-1
        elseif rv.Treatment==eTreatment.CategoricalNumeric then
            rv.nCritValRows = rv.CritVals.n_rows
            rv.nArtVars = rv.nCritVals + 1
            rv.iArtVar_Last=rv.nArtVars-1
        elseif rv.Treatment==eTreatment.None then
            rv.nCritValRows=1
            rv.nArtVars = 1
            rv.iArtVar_First = 1
            rv.iArtVar_Last=1
        elseif rv.Treatment==eTreatment.CodedMissings then
            rv.nCritValRows=1
            rv.nArtVars = 2
            rv.iArtVar_Last=1
        elseif rv.Treatment==eTreatment.Constant then
            rv.nCritValRows=1
            rv.nArtVars = 1
            rv.iArtVar_First = 1
            rv.iArtVar_Last=1
        else
            _G.error("Error, Number:="..(WDSContextID + 1)..", "..WDSModuleName..", Unrecognized Treatment!")
        end

        if (rv.Treatment == eTreatment.Hats or rv.Treatment == eTreatment.iHats) and rv.nCritVals == 1 then
            _G.error("Error, Number:="..(WDSContextID + 1)..", "..WDSModuleName..", Invalid Knots")
        elseif (rv.Treatment == eTreatment.BSplineOrder2) and rv.nCritVals <= 3 then
            _G.error("Error, Number:="..(WDSContextID + 1)..", "..WDSModuleName..", Invalid Knots")
        elseif (rv.Treatment == eTreatment.BSplineOrder3) and rv.nCritVals <= 5 then
            _G.error("Error, Number:="..(WDSContextID + 1)..", "..WDSModuleName..", Invalid Knots")
        elseif (rv.Treatment == eTreatment.DiscreteLC or rv.Treatment == eTreatment.DiscreteRC or rv.Treatment == eTreatment.Categorical or rv.Treatment == eTreatment.CategoricalNumeric)
            and rv.nCritVals == 0 then
            _G.error("Error, Number:="..(WDSContextID + 1)..", "..WDSModuleName..", Invalid Knots")
        end

        if not(wds.bIn(rv.Treatment, eTreatment.None, eTreatment.Constant, eTreatment.Categorical, eTreatment.CategoricalNumeric)) then
            for i=2, rv.nCritVals do
                if rv.CritVals{1,i} <= rv.CritVals{1,i-1} then
                    _G.error("Error, Number:="..(WDSContextID + 1)..", "..WDSModuleName..", Invalid Knots")
                end --if
            end -- i
        end --if

        if args.CoefficientValues and args.CoefficientsValues~=NULL then
            if mat.bIsMatrix(args.CoefficientValues) then
                if args.CoefficientValues.n_cols~=rv.nArtVars then
                    _G.error("Error, Number:="..(WDSContextID + 1)..", "..WDSModuleName..", Invalid Coefficients")
                end
                rv.CoefVals=args.CoefficientValues
            elseif type(args.CoefficientValues)=="table" and ( #args.CoefficientValues % rv.nArtVars == 0 ) then
                rv.CoefVals=mat.dMatrix_WrapOrRef(args.CoefficientValues,{n_cols=rv.nArtVars})
            elseif type(args.CoefficientValues)=="double" and #args.CoefficientValues==1 then
                rv.CoefVals=mat.dMatrix_WrapOrRef(args.CoefficientValues,{n_rows=1,n_cols=1})
            else
                    _G.error("Error, Number:="..(WDSContextID + 1)..", "..WDSModuleName..", Invalid Coefficients")
            end
            rv.nScores=args.CoefficientValues.n_rows
        end
            
    


        return rv

    end

local fArtificialsCount_Args={"Treatment","CriticalValues"}

fArtificialsCount=wds.AddToModuleHelp{
    fArtificialsCount=[==[--[[--
            Returns just the expected number of artificials.
--]]--]==]
-- @function fArtificialsCount
, info=info} ..  function(...)
        local args=fVarArgs(fArtificialsCount_Args,...)
        if args.VariableMatter then
            return args.VariableMatter.nArtVars
        end
        local Treatment, CriticalValues, varm
        varm=fVariableMatter{Treatment=args.Treatment, CriticalValues=args.CriticalValues}
        return varm.nArtVars
    end

local fArtificialsLabels_Args={"Treatment","CriticalValues","VariableBaseName"}

fArtificialsLabels=wds.AddToModuleHelp{
    fArtificialsLabels=[==[--[[--
            Returns the labels for artificials for a given treatment and set of critical values.
--]]--]==]
-- @function fArtificialsLabels
, info=info} ..  function(...)
        local args=fVarArgs(fArtificialsLabels_Args,...)
        local Treatment, CriticalValues, varm, VariableBaseName, suffix_sep
        if args.VariableMatter then
            varm=args.VariableMatter
        else
            varm=fVariableMatter(args.Treatment,args.CriticalValues)
        end
        VariableBaseName=args.VariableBaseName or args.Name or varm.ArtBaseName or varm.Name
        suffix_sep=args.Separator or ""
        local rv={}
        for i=varm.iArtVar_First,varm.iArtVar_Last do
            _G.table.insert(rv,VariableBaseName..suffix_sep.._G.tostring(i))
        end
        return rv
    end

local fArtificials_Args={"Treatment","Input","CriticalValues","CleanLimitLeftVal","CleanLimitRightVal"}

fArtificials=AddToModuleHelp{
        fArtificials=[==[--[[--
        Returns a matrix of artificials given treatment parameters and a value or vector of values.
--]]--]==]
-- @function fArtificials
} ..  function(...)
        local args=fVarArgs(fArtificials_Args,...)
        local varm=args.VariableMatter or fVariableMatter(args.Treatment,args.CriticalValues,args.CleanLimitLeftValue,args.CleanLimitRightValue,args.CoefficientValues)
        local Input=dMatrix_WrapOrRef(args.Input)
        local VariableBaseName=args.VariableBaseName or args.Name or varm.ArtBaseName or var.Name
        local suffix_sep=args.Separator or ""
        local rv={}
        local CVs=varm.CritVals
        local Cnstnt
        local CleanLimitLeftVal=varm.CleanLimits[1] or NULL
        local CleanLimitRightVal=varm.CleanLimits[2] or NULL
        local dCVs={} --for sequential differences
        local d2CVs={} --for two-step sequential differences
        local d3CVs={} --for three-step sequential differences

        local eps=0.00000001

        local rv

        if wds.bIn(varm.Treatment, eTreatment.Categorical, eTreatment.CategoricalNumeric) then
            --make sure any imbeds are expanded
            CVs=dMatrix(CVs)
            for i=1,CVs.n_rows do
                for j=1,CVs.n_cols do
                    if _G.type(CVs{i,j})=="table" then
                        CVs[{i,j}]=dMatrix(CVs{i,j})
                    end
                end
            end
        elseif varm.Treatment == eTreatment.Constant then
            Cnstnt = CVs[{1, 1}]
        elseif not (varm.Treatment == eTreatment.None or varm.Treatment == eTreatment.Constant) then
            --wrap already addressed above
            --check the critical values for order
            if not CVs:isOrdered() then
                    error(" Number:="..(WDSContextID + 1)..WDSModuleName..", Description:=Invalid Knots")
            end
            if wds.bIn(varm.Treatment, eTreatment.Hats, eTreatment.iHats, eTreatment.BSplineOrder2, eTreatment.BSplineOrder3) then
                dCVs=mat.dMatrix_SimpleDiffVector(CVs,1)
            end
            if wds.bIn(varm.Treatment, eTreatment.BSplineOrder2, eTreatment.BSplineOrder3, eTreatment.iHats) then
                d2CVs=mat.dMatrix_SimpleDiffVector(CVs,2)
            end
            if varm.Treatment == eTreatment.BSplineOrder3 then
                d3CVs=mat.dMatrix_SimpleDiffVector(CVs,3)
            end
        end
    
        
    local nrows = Input.n_rows

    local rc=dMatrix(nrows, varm.nArtVars)

    local tempval, tempdouble, x
    local r, i, ia, k, found
    local bIsMissing
    
    --[[
    'CodeDoc - CJW :
    '   For consistency, using:
    '       r for row index
    '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
    '       ia for the VBA 'option base 1' artificial index
    '       k for score index
    --]]

    for r = 1, nrows do
        tempval = Input[r]

        if varm.Treatment == eTreatment.None then

            ia = 1
            rc[{r, ia}] = tempval

        elseif varm.Treatment == eTreatment.Constant then

            ia = 1
            rc[{r, ia}] = Cnstnt

        elseif wds.bIn(varm.Treatment, eTreatment.Categorical, eTreatment.CategoricalNumeric) then

            found = false
            if mat.bIsNULLOrError(tempval) then
                found = true
                i = 0
            else
                for _i = 1, varm.nCritVals do
                    for j = 1, varm.nCritValRows do
                        if wds.bIsEmpty(CVs{j, _i}) then
                            break
                        end
                        --Note: CJW, this is not efficient, but in case CVs{j, _i} 
                        --is not expanded into rows.........
                        if mat.bIsMatrix(CVs{j, _i}) then
                            local CVsji=CVs{j, _i}
                            for k=1,#CVsji.data do
                                if varm.Treatment==eTreatment.CategoricalNumeric then
                                    if _G.math.abs(tempval-CVs.data[k])<0.000001 then
                                        i=_i
                                        found = true
                                        break
                                    end
                                else
                                    if tempval == CVsji.data[k] then
                                        i=_i
                                        found = true
                                        break
                                    end
                                end
                            end
                            if found then
                                i=_i
                                break
                            end
                        else
                            if varm.Treatment==eTreatment.CategoricalNumeric then
                                if _G.math.abs(tempval-CVs{j, _i})<0.000001 then
                                    i=_i
                                    found = true
                                    break
                                end
                            else
                                if tempval == CVs{j, _i} then
                                    i=_i
                                    found = true
                                    break
                                end
                            end
                        end
                    end
                    if found then
                        break
                    end
                end
            end

            if found then
                ia = i + 1
            else
                ia = 1
            end

            rc[{r, ia}] = 1

        else
            bIsMissing = not mat.bIsNumeric(tempval)
            if not bIsMissing and varm.bUseCLLeft and not ( NULL==CleanLimitLeftVal ) then
                bIsMissing = tempval < CleanLimitLeftVal
            end
            if not bIsMissing and varm.bUseCLRight and not ( NULL==CleanLimitRightVal ) then
                bIsMissing = tempval > CleanLimitRightVal
            end

            if bIsMissing then
                ia = 1

                    rc[{r, ia}] = 1

            else


            --just to keep things communicable and relatable to usual mathematical discussion

            x = mat.CDbl(tempval)

            if varm.Treatment == eTreatment.CodedMissings then
                --'simple case, missings have already been addressed
                i = 1
                ia = 2

                rc[{r, ia}] = x

            elseif x <= CVs(1) + eps then
                --'all non-missing first artificials are 1 left of the first critical value, except iHats and DiscreteRC
                i = 1
                ia = 2
                if varm.Treatment == eTreatment.iHats then
                    tempdouble = x - CVs(1)

                        rc[{r, ia}] = tempdouble

                else

                        if (varm.Treatment == eTreatment.DiscreteRC) and (x >= CVs(1) - eps) then
                            i = i + 1
                            ia = ia + 1
                        end

                        rc[{r, ia}] = 1

                    end
            elseif x >= CVs(varm.nCritVals) - eps then
                --'all non-missing last artificials are 1 right of the last critical value, except iHats and DiscreteLC
                i = varm.nCritVals
                ia = varm.nArtVars
                if varm.Treatment == eTreatment.iHats then
                    tempdouble = (x - CVs(i) + dCVs(i - 1) / 2)

                        rc[{r, ia}] = tempdouble
                        for j = 2, varm.nCritVals - 1 do
                            ia = j + 1
                            rc[{r, ia}] = rc[{r, ia}] + d2CVs(j - 1) / 2
                        end
                        j = 1
                        ia = 2
                        rc[{r, ia}] = rc[{r, ia}] + dCVs(j) / 2

                else

                        if (varm.Treatment == eTreatment.DiscreteLC) and (x <= CVs(varm.nCritVals) - eps) then
                            i = i + 1
                            ia = ia + 1
                        end

                        rc[{r, ia}] = 1

                    end
            else
                
                
                --'main guts of the function.....
                
                --'find the critical value interval.....
                local i=varm.nCritVals-1
                if varm.Treatment == eTreatment.DiscreteLC then
                    for _i = varm.nCritVals - 1, 1, -1 do
                        if x > CVs(_i) + eps then
                            i=_i
                            break
                        end
                    end
                    i=i+1
                elseif varm.Treatment == eTreatment.DiscreteRC then
                    for _i = varm.nCritVals - 1, 1, -1 do
                        if x > CVs(_i) - eps then
                            i=_i
                            break
                        end
                    end
                    i=i+1
                else
                    for _i = varm.nCritVals - 1, 1, -1 do
                        if x >= CVs(_i) then
                            i=_i
                            break
                        end
                    end
                end
                
                --'usual VBA index
                ia = i + 1

                if varm.Treatment == eTreatment.DiscreteLC or varm.Treatment == eTreatment.DiscreteRC then

                    rc[{r, ia}] = 1

                elseif varm.Treatment == eTreatment.Hats then
                    tempdouble = (x - CVs(i)) / dCVs(i)

                        rc[{r, ia + 1}] = tempdouble
                        rc[{r, ia}] = (1 - tempdouble)

                elseif varm.Treatment == eTreatment.iHats then
                    tempdouble = ((x - CVs(i)) ^ 2 / dCVs(i) / 2)

                        iaP1 = ia + 1
                        
                        rc[{r, iaP1}] = rc[{r, iaP1}] + tempdouble
                        rc[{r, ia}] = rc[{r, ia}] + (x - CVs(i) - tempdouble)
                        
                        for ii = 1, (i - 1) do
                            iia = ii + 1
                            iiaP1 = iia + 1
                            
                            rc[{r, iiaP1}] = rc[{r, iiaP1}] + dCVs(ii) / 2
                            rc[{r, iia}] = rc[{r, iia}] + dCVs(ii) / 2
                        
                        end

                elseif varm.Treatment == eTreatment.BSplineOrder2 then
                    --'the first artificial is a left catch all, necessary through knot3
                    --'k+2 is more akin to the "usual" index, mapped back to "option base 1" with 0 being the missing code variable
                    
                    iM1 = i - 1
                    ia = i + 2
                    iaM1 = ia - 1
                    iaM2 = ia - 2
                    
                    xMci = (x - CVs(i))
                    xMciM1 = 0
                
                    if i > 1 then
                        xMciM1 = (x - CVs(iM1))
                    end
                    
                    -- 'the last artificial is a right catch all
                    -- 'therefore, fo0, [f]unction [o]ffset [0], stops with CVs(varm.nCritVals-2)
                    -- 'and fo1 is a catch all at CVs(varm.nCritVals-1)
                    
                    fo0 = 0
                    fo1 = 0
                    fo2 = 0
                    
                    if i < varm.nCritVals - 1 then
                        --' a+b=1,p+q=1
                        --' a*p
                        fo0 = xMci / d2CVs(i) * xMci / dCVs(i)
                    end
                    if i == 1 then
                        --'fo1 is a catch all where not defined
                        fo1 = 1 - fo0
                    elseif i < varm.nCritVals - 1 then
                        --'the starting interpolation of the preceding basis * corresponding right side of lower order Hat
                        --'+the starting right interpolation of preceding basis * corresponding left side of lower order Hat
                        --' a*q
                        --' +b*p
                        fo1 = xMciM1 / d2CVs(iM1) * (1 - xMci / dCVs(i)) 
                                    + (1 - xMci / d2CVs(i)) * xMci / dCVs(i)
                    end
                    if i == 2 then
                        --'fo2 is a catch all where not defined
                        fo2 = 1 - fo0 - fo1
                    elseif i > 2 then
                        --'the remaining right interpolation of second preceding basis * corresponding right side of lower order Hat
                        --' b*q
                        fo2 = (1 - xMciM1 / d2CVs(iM1)) * (1 - xMci / dCVs(i))
                    end
                    if i == varm.nCritVals - 1 then
                        fo1 = 1 - fo2
                    end
                    

                    if ia < varm.nArtVars then
                        rc[{r, ia}] = fo0
                    else
                        rc[{r, varm.nArtVars}] = fo0
                    end
                    
                    if iaM1 > 1 then
                        if iaM1 < varm.nArtVars then
                            rc[{r, iaM1}] = fo1
                        else
                            rc[{r, varm.nArtVars}] = rc[{r, varm.nArtVars}] + fo1
                        end
                    end
                    
                    if iaM2 > 1 then
                        rc[{r, iaM2}] = rc[{r, iaM2}] + fo2
                    end
                    
                elseif varm.Treatment == eTreatment.BSplineOrder3 then
                    
                    
                    iM1 = i - 1
                    iM2 = i - 2
                    ia = i + 2
                    iaM1 = ia - 1
                    iaM2 = ia - 2
                    iaM3 = ia - 3
                    
                    xMci = (x - CVs(i))
                    xMciM1 = 0
                    xMciM2 = 0
                
                    if i > 1 then
                        xMciM1 = (x - CVs(iM1))
                    end
                    if i > 2 then
                        xMciM2 = (x - CVs(iM2))
                    end
                    
                    fo0 = 0
                    fo1 = 0
                    fo2 = 0
                    fo3 = 0
                    
                    if i < varm.nCritVals - 2 then
                        --' u+v=1,a+b=1,p+q=1
                        --' u[0]*a[0]*p[0]
                        fo0 = xMci / d3CVs(i) * xMci / d2CVs(i) * xMci / dCVs(i)
                    end
                    if i == 1 then --and i<varm.nCritVals-1 then
                        fo1 = 1 - fo0
                    elseif i < varm.nCritVals - 2 then
                        --' u[-1]*(a[-1]*q[0] + b*p[0])
                        --'+v[0]*(a[0]*p[0])
                    
                        fo1 = (xMciM1 / d3CVs(iM1)) * (xMciM1 / d2CVs(iM1) * (1 - xMci / dCVs(i)) 
                                                        + (1 - xMci / d2CVs(i)) * (xMci / dCVs(i))) + 
                                (1 - xMci / d3CVs(i)) * (xMci / d2CVs(i) * xMci / dCVs(i))
                                                                                                                  
                    end
                    if i == 2 then --and i<varm.nCritVals-2 then
                        fo2 = 1 - fo0 - fo1
                    elseif i > 2 and i < varm.nCritVals - 1 then
                        --' u[-2]*(b[-1]*q[0])
                        --'+v[-1]*(a[-1]*q[0]+b[0]*p[0])
                        fo2 = (xMciM2 / d3CVs(iM2)) * ((1 - xMciM1 / d2CVs(iM1)) * (1 - xMci / dCVs(i))) 
                            + (1 - xMciM1 / d3CVs(iM1)) * (xMciM1 / d2CVs(iM1) * (1 - xMci / dCVs(i)) 
                                                         + (1 - xMci / d2CVs(i)) * (xMci / dCVs(i)))
                    end
                    if i == 3 then --and i<varm.nCritVals-3 then
                        fo3 = 1 - fo0 - fo1 - fo2
                    elseif i > 3 and i< varm.nCritVals then
                        --' v[-2]*b[-1]*p[0]
                        fo3 = (1 - xMciM2 / d3CVs(iM2)) * (1 - xMciM1 / d2CVs(iM1)) * (1 - xMci / dCVs(i))
                    end
                    
                    
                    
                    if i == varm.nCritVals - 2 then
                        fo1 = 1 - fo2 - fo3
                    end
                    if i == varm.nCritVals - 1 then
                        fo2 = 1 - fo3
                    end
                    
                    if ia < varm.nArtVars then
                        rc[{r, ia}] = fo0
                    else
                        rc[{r, varm.nArtVars}] = fo0
                    end
                    if iaM1 > 1 then
                        if iaM1 < varm.nArtVars then
                            rc[{r, iaM1}] = fo1
                        else
                            rc[{r, varm.nArtVars}] = rc[{r, varm.nArtVars}] + fo1
                        end
                    end
                    if iaM2 > 1 then
                        if iaM2 < varm.nArtVars then
                            rc[{r, iaM2}] = fo2
                        else
                            rc[{r, varm.nArtVars}] = rc[{r, varm.nArtVars}] + fo2
                        end
                    end
                    if iaM3 > 1 then
                        if iaM3 < varm.nArtVars then
                            rc[{r, iaM3}] = fo3
                        else
                            rc[{r, varm.nArtVars}] = rc[{r, varm.nArtVars}] + fo3
                        end
                    end
                    
                    
                    
                end
            end
            end
            end
    end
        
    
    return rc

end



local fArtificialsScored_Args={"Treatment","Input","CriticalValues","CoefficientValues","CleanLimitLeftVal","CleanLimitRightVal"}

fArtificialsScored=AddToModuleHelp{
        fArtificialsScored=[==[--[[--
            Returns a matrix of scored artificials given treatment parameters and a value or vector of values.
--]]--]==]
-- @function fArtificialsScored
} ..  function(...)
        local args=fVarArgs(fArtificialsScored_Args,...)
        local varm=args.VariableMatter or fVariableMatter(args.Treatment,args.CriticalValues,args.CleanLimitLeftvalue,args.CleanLimitRightValue,args.CoefficientValues)
        local Input=dMatrix_WrapOrRef(args.Input)
        local CoefficientValues=dMatrix_WrapOrRef(args.CoefficientValues)
        local VariableBaseName=args.VariableBaseName or args.Name or varm.ArtBaseName or varm.Name
        local suffix_sep=args.Separator or ""
        local rv={}
        local CVs=varm.CritVals
        local Cnstnt
        local CleanLimitLeftVal=args.CleanLimitLeftVal or (args.CleanLimits and args.CleanLimits[1]) or NULL
        local CleanLimitRightVal=args.CleanLimitRightVal or (args.CleanLimits and args.CleanLimits[2]) or NULL
        local dCVs={} --for sequential differences
        local d2CVs={} --for two-step sequential differences
        local d3CVs={} --for three-step sequential differences

        local eps=0.00000001

        local rv

    
        if CoefficientValues.n_cols ~= varm.nArtVars then
            error("Error, Number:="..(WDSContextID + 1)..", "..WDSModuleName..", Description:=Invalid Coefficients")
        end

        local Coef=dMatrix_WrapOrRef(CoefficientValues)
        local nscores=CoefficientValues.n_rows

        if wds.bIn(varm.Treatment, eTreatment.Categorical, eTreatment.CategoricalNumeric) then
            --make sure any imbeds are expanded
            CVs=dMatrix(CVs)
            for i=1,CVs.n_rows do
                for j=1,CVs.n_cols do
                    if _G.type(CVs{i,j})=="table" then
                        CVs[{i,j}]=dMatrix(CVs{i,j})
                    end
                end
            end
        elseif varm.Treatment == eTreatment.Constant then
            Cnstnt = CVs[{1, 1}]
        elseif not (varm.Treatment == eTreatment.None or varm.Treatment == eTreatment.Constant) then
            --wrap already addressed above
            --check the critical values for order
            if not CVs:isOrdered() then
                    error(" Number:="..(WDSContextID + 1)..WDSModuleName..", Description:=Invalid Knots")
            end
            if wds.bIn(varm.Treatment, eTreatment.Hats, eTreatment.iHats, eTreatment.BSplineOrder2, eTreatment.BSplineOrder3) then
                dCVs=mat.dMatrix_SimpleDiffVector(CVs,1)
            end
            if wds.bIn(varm.Treatment, eTreatment.BSplineOrder2, eTreatment.BSplineOrder3, eTreatment.iHats) then
                d2CVs=mat.dMatrix_SimpleDiffVector(CVs,2)
            end
            if varm.Treatment == eTreatment.BSplineOrder3 then
                d3CVs=mat.dMatrix_SimpleDiffVector(CVs,3)
            end
        end
    
        local nrows = Input.n_rows

        local rc=dMatrix(nrows, nscores)

        local tempval, tempdouble, x
        local r, i, ia, k, found
        local bIsMissing
    
        --[[
        'CodeDoc - CJW :
        '   For consistency, using:
        '       r for row index
        '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
        '       ia for the VBA 'option base 1' artificial index
        '       k for score index
        --]]

        for r = 1, nrows do 

            tempval = Input[r]

            if varm.Treatment == eTreatment.None then

                ia = 1
                for k = 1, nscores do
                    rc[{r, k}] = Coef[{k, ia}] * tempval
                end --k

            elseif varm.Treatment == eTreatment.Constant then

                ia = 1

                for k = 1, nscores do
                    rc[{r, k}] = Coef[{k, ia}] * Cnstnt
                end --k

            elseif wds.bIn(varm.Treatment, eTreatment.Categorical, eTreatment.CategoricalNumeric) then

                found = false
                if mat.bIsNULLOrError(tempval) then
                    found = true
                    i = 0
                else
                    for _i = 1, varm.nCritVals do
                        for j = 1, varm.nCritValRows do
                            if wds.bIsEmpty(CVs{j, _i}) then
                                break
                            end
                            --Note: CJW, this is not efficient, but in case CVs{j, _i} 
                            --is not expanded into rows.........
                            if mat.bIsMatrix(CVs{j, _i}) then
                                local CVsji=CVs{j, _i}
                                for k=1,#CVsji.data do
                                    if varm.Treatment==eTreatment.CategoricalNumeric then
                                        if _G.math.abs(tempval-CVs.data[k])<0.000001 then
                                            i=_i
                                            found = true
                                            break
                                        end
                                    else
                                        if tempval == CVsji.data[k] then
                                            i=_i
                                            found = true
                                            break
                                        end
                                    end
                                end
                                if found then
                                    i=_i
                                    break
                                end
                            else
                                if varm.Treatment==eTreatment.CategoricalNumeric then
                                    if _G.math.abs(tempval-CVs{j, _i})<0.000001 then
                                        i=_i
                                        found = true
                                        break
                                    end
                                else
                                    if tempval == CVs{j, _i} then
                                        i=_i
                                        found = true
                                        break
                                    end
                                end
                            end
                        end
                        if found then
                            break
                        end
                    end
                end

                if found then
                    ia = i + 1
                else
                    ia = 1
                end

                for k = 1, nscores do
                    rc[{r, k}] = Coef{k, ia}
                end --k

            else
                bIsMissing = not mat.bIsNumeric(tempval)
                if not bIsMissing and varm.bUseCLLeft and not ( NULL==CleanLimitLeftVal ) then
                    bIsMissing = tempval < CleanLimitLeftVal
                end
                if not bIsMissing and varm.bUseCLRight and not ( NULL==CleanLimitRightVal ) then
                    bIsMissing = tempval > CleanLimitRightVal
                end

                if bIsMissing then
                    ia = 1
                    for k = 1, nscores do
                        rc[{r, k}] = Coef(k, ia)
                    end --k
                else

                --'just to keep things communicable and relatable to usual mathematical discussion

                x = mat.CDbl(tempval)

                if varm.Treatment == eTreatment.CodedMissings then
                    --'simple case, missings have already been addressed
                    i = 1
                    ia = 2
                    for k = 1, nscores do
                        rc[{r, k}] = Coef{k, 2} * x
                    end --k
                elseif x <= CVs(1) + eps then
                    --'all non-missing first artificials are 1 left of the first critical value, except iHats and DiscreteRC
                    i = 1
                    ia = 2
                    if varm.Treatment == eTreatment.iHats then
                        tempdouble = x - CVs(1)
                        for k = 1, nscores do
                            rc[{r, k}] = Coef{k, 2} * tempdouble
                        end --k
                    else
                        if (varm.Treatment == eTreatment.DiscreteRC) and (x >= CVs(1) - eps) then
                            i = i + 1
                            ia = ia + 1
                        end
                        for k = 1, nscores do
                            rc[{r, k}] = Coef{k, ia}
                        end --k
                    end
                elseif x >= CVs(varm.nCritVals) - eps then
                    --'all non-missing last artificials are 1 right of the last critical value, except iHats and DiscreteLC
                    i = varm.nCritVals
                    ia = varm.nArtVars
                    if varm.Treatment == eTreatment.iHats then
                        tempdouble = (x - CVs(i) + dCVs(i - 1) / 2)
                        for k = 1, nscores do
                            rc[{r, k}] = Coef(k, ia) * tempdouble
                        end --k
                        for k = 1, nscores do
                            for j = 2, varm.nCritVals - 1 do
                                ia = j + 1
                                rc[{r, k}] = rc{r, k} + Coef{k, ia} * d2CVs(j - 1) / 2
                            end --j
                            j = 1
                            ia = 2
                            rc[{r, k}] = rc{r, k} + Coef{k, ia} * dCVs(j) / 2
                        end --k
                    else
                        if (varm.Treatment == eTreatment.DiscreteLC) and (x <= CVs(varm.nCritVals) - eps) then
                            i = i + 1
                            ia = ia + 1
                        end
                        for k = 1, nscores do
                            rc[{r, k}] = Coef{k, ia}
                        end --k
                    end
                else
                    
                    --'main guts of the function.....
                    
                    --'find the critical value interval.....
                    local i=varm.nCritVals-1
                    if varm.Treatment == eTreatment.DiscreteLC then
                        for _i = varm.nCritVals - 1, 1, -1 do
                            if x > CVs(_i) + eps then
                                i=_i
                                break
                            end
                        end
                        i=i+1
                    elseif varm.Treatment == eTreatment.DiscreteRC then
                        for _i = varm.nCritVals - 1, 1, -1 do
                            if x > CVs(_i) - eps then
                                i=_i
                                break
                            end
                        end
                        i=i+1
                    else
                        for _i = varm.nCritVals - 1, 1, -1 do
                            if x >= CVs(_i) then
                                i=_i
                                break
                            end
                        end
                    end
                
                    
                    --'usual VBA index
                    ia = i + 1
                    if varm.Treatment == eTreatment.DiscreteLC or varm.Treatment == eTreatment.DiscreteRC then
                        for k = 1, nscores do
                            rc[{r, k}] = Coef{k, ia}
                        end --k
                    elseif varm.Treatment == eTreatment.Hats then
                        tempdouble = (x - CVs(i)) / dCVs(i)
                        for k = 1, nscores do
                            rc[{r, k}] = rc{r, k} + Coef{k, ia + 1} * tempdouble
                            rc[{r, k}] = rc{r, k} + Coef{k, ia} * (1 - tempdouble)
                        end --k
                    elseif varm.Treatment == eTreatment.iHats then
                        tempdouble = ((x - CVs(i)) ^ 2 / dCVs(i) / 2)

                            iaP1 = ia + 1
                            for k = 1, nscores do
                                rc[{r, k}] = rc[{r, k}] + Coef{k, iaP1} * tempdouble
                                rc[{r, k}] = rc[{r, k}] + Coef{k, ia} * (x - CVs(i) - tempdouble)
                            end --k
                            for ii = 1, (i - 1) do
                                iia = ii + 1
                                iiaP1 = iia + 1
                                for k = 1, nscores do
                                    rc[{r, k}] = rc[{r, k}] + Coef{k, iiaP1} * dCVs(ii) / 2
                                    rc[{r, k}] = rc[{r, k}] + Coef{k, iia} * dCVs(ii) / 2
                                end --k
                            end --ii
                    
                    elseif varm.Treatment == eTreatment.BSplineOrder2 then
                        --'first artificial is a left catch all, necessary through knot3
                        --'i+2 is more akin to the "usual" index, mapped back to "option base 1" with 0 being the missing code variable
                        iM1 = i - 1
                        ia = i + 2
                        iaM1 = ia - 1
                        iaM2 = ia - 2
                        
                        xMci = (x - CVs(i))
                        xMciM1 = 0
                    
                        if i > 1 then
                            xMciM1 = (x - CVs(iM1))
                        end
                                            
                        --'the last artificial is a right catch all
                        --'therefore, fo0, [f]unction [o]ffset [0], stops with CVs(varm.nCritVals-2)
                        --'and fo1 is a catch all at CVs(varm.nCritVals-1)
                        
                        fo0 = 0
                        fo1 = 0
                        fo2 = 0
                        
                        if i < varm.nCritVals - 1 then
                            fo0 = xMci / d2CVs(i) * xMci / dCVs(i)
                        end
                        if i == 1 then
                            --'fo1 is a catch all where not defined
                            fo1 = 1 - fo0
                        elseif i < varm.nCritVals - 1 then
                            fo1 = xMciM1 / d2CVs(iM1) * (1 - xMci / dCVs(i)) 
                                        + (1 - xMci / d2CVs(i)) * xMci / dCVs(i)
                        end
                        if i == 2 then
                            --'fo2 is a catch all where not defined
                            fo2 = 1 - fo0 - fo1
                        elseif i > 2 then
                            fo2 = (1 - xMciM1 / d2CVs(iM1)) * (1 - xMci / dCVs(i))
                        end
                        if i == varm.nCritVals - 1 then
                            fo1 = 1 - fo2
                        end

                        local lrc={}
                        for i=1, varm.nArtVars do
                            lrc[i]=0.0
                        end

                    if ia < varm.nArtVars then
                        lrc[ia] = fo0
                    else
                        lrc[varm.nArtVars] = fo0
                    end
                    
                    if iaM1 > 1 then
                        if iaM1 < varm.nArtVars then
                            lrc[iaM1] = fo1
                        else
                            lrc[varm.nArtVars] = lrc[varm.nArtVars] + fo1
                        end
                    end
                                     
                    if iaM2 > 1 then
                        lrc[iaM2] = lrc[iaM2] + fo2
                    end
                    
                    
                    for k = 1, nscores do
                        
                        for i = 1, varm.nArtVars do
                            rc[{r, k}] = rc[{r, k}] + Coef[{k, i}] * lrc[i]
                        end
                        
                    end
                    
                    elseif varm.Treatment == eTreatment.BSplineOrder3 then
                        
                        
                        iM1 = i - 1
                        iM2 = i - 2
                        ia = i + 2
                        iaM1 = ia - 1
                        iaM2 = ia - 2
                        iaM3 = ia - 3
                        
                        xMci = (x - CVs(i))
                        xMciM1 = 0
                        xMciM2 = 0
                    
                        if i == 3 then
                        x = x
                        end
                        if i > 1 then
                            xMciM1 = (x - CVs(iM1))
                        end
                        if i > 2 then
                            xMciM2 = (x - CVs(iM2))
                        end
                        
                        fo0 = 0
                        fo1 = 0
                        fo2 = 0
                        fo3 = 0
                        
                        if i < varm.nCritVals - 2 then
                            --' u+v=1,a+b=1,p+q=1
                            --' u[0]*a[0]*p[0]
                            fo0 = xMci / d3CVs(i) * xMci / d2CVs(i) * xMci / dCVs(i)
                        end
                        if i == 1 then
                            fo1 = 1 - fo0
                        elseif i < varm.nCritVals - 2 then
                            --' u[-1]*(a[-1]*q[0] + b*p[0])
                            --'+v[0]*(a[0]*p[0])
                        
                            fo1 = (xMciM1 / d3CVs(iM1)) * (xMciM1 / d2CVs(iM1) * (1 - xMci / dCVs(i)) 
                                                            + (1 - xMci / d2CVs(i)) * (xMci / dCVs(i))) + 
                                    (1 - xMci / d3CVs(i)) * (xMci / d2CVs(i) * xMci / dCVs(i))
                                                                                                                      
                        end
                        if i == 2 then
                            fo2 = 1 - fo0 - fo1
                        elseif i > 2 and i < varm.nCritVals - 1 then
                            --' u[-2]*(b[-1]*q[0])
                            --'+v[-1]*(a[-1]*q[0]+b[0]*p[0])
                            fo2 = (xMciM2 / d3CVs(iM2)) * ((1 - xMciM1 / d2CVs(iM1)) * (1 - xMci / dCVs(i)))
                                + (1 - xMciM1 / d3CVs(iM1)) * (xMciM1 / d2CVs(iM1) * (1 - xMci / dCVs(i))
                                                             + (1 - xMci / d2CVs(i)) * (xMci / dCVs(i)))
                        end
                        if i == 3 then
                            fo3 = 1 - fo0 - fo1 - fo2
                        elseif i > 3 then
                            --' v[-2]*b[-1]*p[0]
                            fo3 = (1 - xMciM2 / d3CVs(iM2)) * (1 - xMciM1 / d2CVs(iM1)) * (1 - xMci / dCVs(i))
                        end
                        
                        
                        
                        if i == varm.nCritVals - 2 then
                            fo1 = 1 - fo2 - fo3
                        end
                        if i == varm.nCritVals - 1 then
                            fo2 = 1 - fo3
                        end

                        local lrc={}
                        for i=1, varm.nArtVars do
                            lrc[i]=0.0
                        end

                    if ia < varm.nArtVars then
                        lrc[ia] = fo0
                    else
                        lrc[varm.nArtVars] = fo0
                    end
                    if iaM1 > 1 then
                        if iaM1 < varm.nArtVars then
                            lrc[iaM1] = fo1
                        else
                            lrc[varm.nArtVars] = lrc[varm.nArtVars] + fo1
                        end
                    end
                    if iaM2 > 1 then
                        if iaM2 < varm.nArtVars then
                            lrc[iaM2] = fo2
                        else
                            lrc[varm.nArtVars] = lrc[varm.nArtVars] + fo2
                        end
                    end
                    if iaM3 > 1 then
                        if iaM3 < varm.nArtVars then
                            lrc[iaM3] = fo3
                        else
                            lrc[varm.nArtVars] = lrc[varm.nArtVars] + fo3
                        end
                    end

                    for k = 1, nscores do
                        
                        for i = 1, varm.nArtVars do
                            rc[{r, k}] = rc[{r, k}] + Coef[{k, i}] * lrc[i]
                        end
                        
                    end
                    
                    
                    
                end
            end
        end
        end
    end --r
    
    return rc

end

return wds.EnvLock(_M)



