--[[Copyright 2019,2020, Wypasek Data Science, Inc.  (WDataSci, WDS)
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

--- A few date and time utilities.
-- @submodule WDS.Util

-- Require the base module and set free names into the module
-- environment to be returned.
local wds=require("WDS")
local _M={}
local _G=_G
_ENV=wds.EnvExtension(_M,_G)

local wdsu=require("WDS.Util")
NULL=require("WDS.NULL").NULL

local __parent__="Util"
local __name__="DTm"
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

local module_name_dots=( ... or "main-call-without-args" )
-- to hard-code use.......

info={name=module_name
    ,path=module_path
    ,doc=module_name .. " ("..module_path..")"..[==[
    A set of functions for various date and time operations.
    ]==]
    ,docmap={}
    ,_ENV=_M
}
-- localizing AddToModuleHelp to globally assign to this module's info table
local AddToModuleHelp=function(tbl,tbl2) 
    tbl.info=info 
    return wds.__AddToModuleHelp(tbl,tbl2) 
end

local __dateparts__={"year","month","day","hour","min","sec"}
local __dateparts_keys__={year=true,month=true,day=true,hour=true,min=true,sec=true}
local __dateparts_default__={1970,1,1,0,0,0}
local __dateonlyparts__={"year","month","day"}
local __timeonlyparts__={"hour","min","sec"}
local __osdateparts__={"year","month","day","hour","min","sec","wday","yday","isdst"}
local __osdateparts_keys__={year=true,month=true,day=true,hour=true,min=true,sec=true,wday=true,yday=true,isdst=true}

local __DTm_MT__={}

bIsDTm=AddToModuleHelp{
    bIsDTm=[==[--[[--
            A boolean check for the WDS.Util.DTm class.
--]]--]==]
-- @class DTme
} ..
function(arg)
    if type(arg)~="table" then return false end
    if arg.__classname__ and arg.__classname__~="DTm" then return false end
    local mt=getmetatable(arg)
    if mt~=__DTm_MT__ then return false end
    return true;
end

__DTm_MT__.__epoch__=setmetatable({year=1970,month=1,day=1,hour=0,min=0,sec=0},__DTm_MT__)
__DTm_MT__.__classname__="DTm"

__DTm_MT__.__fmt_input_available__={}
__DTm_MT__.__fmt_input_available__["isoZ"]={"(%d+)[/-](%d+)[/-](%d+)[T%s]+(%d+):(%d+):(%d+)([Z+-])(%d+):(%d+)",
            {"year","month","day","hour","min","sec","tzoffset_direction","tzoffset_hour","tzoffset_min"}}

__DTm_MT__.__fmt_input_available__["iso"]={"(%d+)[/-](%d+)[/-](%d+)[T%s]+(%d+):(%d+):(%d+)", {"year","month","day","hour","min","sec"}}
__DTm_MT__.__fmt_input_available__["iso/"]=__DTm_MT__.__fmt_input_available__["iso"]

__DTm_MT__.__fmt_input_available__["YYYY-MM-DD"]={"(%d+)[/-](%d+)[/-](%d+)", {"year","month","day"}}
__DTm_MT__.__fmt_input_available__["YYYY-MM"]={"(%d+)[/-](%d+)[/-](%d+)", {"year","month"}}

__DTm_MT__.__fmt_input_available__["iso-date"]={"(%d+)[/-](%d+)[/-](%d+)",{"year","month","day","hour"}}
__DTm_MT__.__fmt_input_available__["iso/date"]=__DTm_MT__.__fmt_input_available__["iso-date"]

__DTm_MT__.__fmt_input_available__["YYYYMMDDThhmmss"]={"(%d%d%d%d)(%d%d)(%d%d)T(%d%d)(%d%d)(%d%d)",{"year","month","day","hour","min","sec"}}
__DTm_MT__.__fmt_input_available__["YYYYMMDD"]={"(%d%d%d%d)(%d%d)(%d%d)",{"year","month","day"}}
__DTm_MT__.__fmt_input_available__["YYYYMM"]={"(%d%d%d%d)(%d%d)",{"year","month"}}

__DTm_MT__.__fmt_input_default__="iso"

__DTm_MT__.__fmt_output_available__={}

__DTm_MT__.__fmt_output_available__["iso"]={"YYYY-MM-DD hh:mm:ss", function(self) return string.format("%.4d-%.2d-%.2d %.2d:%.2d:%.2d",self.year,self.month,self.day,self.hour,self.min,self.sec) end}
__DTm_MT__.__fmt_output_available__["iso/"]={"YYYY/MM/DD hh:mm:ss", function(self) return string.format("%.4d/%.2d/%.2d %.2d:%.2d:%.2d",self.year,self.month,self.day,self.hour,self.min,self.sec) end}

__DTm_MT__.__fmt_output_available__["iso-date"]={"YYYY-MM-DD", function(self) return string.format("%.4d-%.2d-%.2d",self.year,self.month,self.day) end}
__DTm_MT__.__fmt_output_available__["iso/date"]={"YYYY/MM/DD", function(self) return string.format("%.4d/%.2d/%.2d",self.year,self.month,self.day,self.hour,self.min,self.sec) end}

__DTm_MT__.__fmt_output_available__["YYYY-MM-DD"]={"YYYY-MM-DD", function(self) return string.format("%.4d-%.2d-%.2d",self.year,self.month,self.day) end}
__DTm_MT__.__fmt_output_available__["YYYY/MM/DD"]={"YYYY/MM/DD", function(self) return string.format("%.4d/%.2d/%.2d",self.year,self.month,self.day) end}

__DTm_MT__.__fmt_output_available__["YYYY-MM"]={"YYYY-MM", function(self) return string.format("%.4d-%.2d",self.year,self.month) end}
__DTm_MT__.__fmt_output_available__["YYYY/MM"]={"YYYY/MM", function(self) return string.format("%.4d/%.2d",self.year,self.month) end}

__DTm_MT__.__fmt_output_default__="iso"

__DTm_MT__.__tostring=function(self)
        local fmt=__DTm_MT__.__fmt_output_available__[self.__fmt_output__] or 
            __DTm_MT__.__fmt_output_available__["iso"]
        if rawlen(self)==1 then
            return fmt[2](os.date("*t",rawget(self,1)))
        else
            return fmt[2](self)
        end
end

__DTm_MT__.__as_date__=function(self)
    if rawlen(self)==1 then
        local tmp=os.date("*t",rawget(self,1))
        rawset(self,1,nil)
        wds.AddToEnv_Raw(self,tmp)
    else
        local i,v
        for i,v in ipairs(__dateparts__) do
            if rawget(self,v)==nil then
                rawset(self,v,__dateparts_default__[i])
            end
        end
    end
    return self
end

__DTm_MT__.__as_time__=function(self)
    if rawlen(self)==1 then
        local i,v
        for i,v in ipairs(__osdateparts__) do rawset(self,v,nil) end
    else
        local i,v
        for i,v in ipairs(__dateparts__) do
            if rawget(self,v)==nil then rawset(self,v,__dateparts_default__[i]) end
        end
        rawset(self,1,os.time(self))
        local i,v
        for i,v in ipairs(__osdateparts__) do rawset(self,v,nil) end
    end
    return self
end


__DTm_MT__.__builder__=function(self,...)
        local args=table.pack(...)
        local i
        local fmt
        if self==nil or type(self)~="table" then 
            if args.n==1 and bIsDTm(args[1]) then
                return setmetatable(wds.deeper_copy(args[1]),__DTm_MT__)
            else
                self=setmetatable({},__DTm_MT__) 
            end
        end
        for i=1,6 do rawset(self,__dateparts__[i],nil) end
        if args.n==0 then
            rawset(self,1,os.time())
            if rawget(self,"__fmt_input__")==nil then rawset(self,"__fmt_input__",__DTm_MT__.__fmt_input_default__) end
            if rawget(self,"__fmt_output__")==nil then rawset(self,"__fmt_output__",__DTm_MT__.__fmt_output_default__) end
        elseif args.n==1 then
            local targ=type(args[1])
            if rawget(self,"__fmt_input__")==nil then rawset(self,"__fmt_input__",__DTm_MT__.__fmt_input_default__) end
            if rawget(self,"__fmt_output__")==nil then rawset(self,"__fmt_output__",__DTm_MT__.__fmt_output_default__) end
            if targ=="table" then
                if bIsDTm(args[1]) then
                    rawset(self,1,arts[1]:time())
                    __DTm_MT__.__as_time__(self)
                else
                    local rv=os.date("*t",os.time(args[1]))
                    for i=1,6 do rawset(self,__dateparts__[i],rv[__dateparts__[i]]) end
                end
            elseif type(args[1])=="string" then
                fmt=__DTm_MT__.__fmt_input_available__.iso
                local parts=table.pack(args[1]:match(fmt[1]))
                for i=1,parts.n,1 do rawset(self,fmt[2][i],math.floor(tonumber(parts[i]))) end
                __DTm_MT__.__as_time__(self)
            elseif type(args[1])=="number" then
                local rv=os.date("*t",args[1])
                for i=1,6 do rawset(self,__dateparts__[i],rv[__dateparts__[i]]) end
            else
                error("Error DTm: TODO")
            end
        elseif args.n==2 then
            if type(args[1])=="string" then
                fmt=__DTm_MT__.__fmt_input_available__[args[2]]
                assert(fmt~=nil,"Error DTm: fmt not available use one of:"..wds.show_keys(__DTm_MT__.__fmt_input_available__))
                rawset(self,"__fmt_input__",args[2])
                rawset(self,"__fmt_output__",args[2])
                local parts=table.pack(args[1]:match(fmt[1]))
                print("parts=",wds.show(parts))
                print("args[1]=",wds.show(args[1]))
                print("fmt[1]=",wds.show(fmt[1]))
                for i=1,parts.n,1 do 
                    if parts[i] then
                        rawset(self,fmt[2][i],math.floor(tonumber(parts[i]))) 
                    end
                end
            elseif type(args[1])=="number" and type(args[2])=="number" then
                if rawget(self,"__fmt_input__")==nil then rawset(self,"__fmt_input__","YYYY-MM") end
                if rawget(self,"__fmt_output__")==nil then rawset(self,"__fmt_output__","YYYY-MM") end
                rawset(self,"year",math.floor(tonumber(args[1])))
                rawset(self,"month",math.floor(tonumber(args[2])))
                rawset(self,"day",1)
            else
                error("TODO")
            end
        elseif args.n==3 or args.n==6 then
            if args.n==3 then
                rawset(self,"__fmt_input__","YYYY-MM-DD")
                rawset(self,"__fmt_output__","YYYY-MM-DD")
            else
                rawset(self,"__fmt_input__","iso")
                rawset(self,"__fmt_output__","iso")
            end
            for i=1,args.n,1 do
                rawset(self,__dateparts__[i],math.floor(tonumber(args[i])))
            end
        else
            error("TODO")
        end
        return self
end
__DTm_MT__.__index=function(self,arg)
        if arg=="__classname__" then return __DTm_MT__.__classname__
        elseif arg=="__class__" then return __DTm_MT__
        elseif arg=="time" then return function() __DTm_MT__.__as_time__(self) return self[1] end
        elseif arg=="parse" then return __DTm_MT__.__new__(self,arg)
        elseif arg=="os_date" then return function() return os.date("*t",self:time()) end

        elseif arg=="copy" then return function(self) return wds.deeper_copy(self) end

        elseif arg=="inc_days" then return function (self,arg2)
                __DTm_MT__.__as_date__(self)
                rawset(self,"day",rawget(self,"day")+arg2)
                __DTm_MT__.__as_time__(self)
                return self
            end

        elseif arg=="add_days" then return function (self,arg2) return self:copy():inc_days(arg2) end

        elseif arg=="days_in_month" then return function(self)
                local tmp
                if rawget(self,1) then
                    tmp=os.date("*t",rawget(self,1))
                else
                    tmp=self
                end
                local tmp1=os.time({year=rawget(tmp,"year"),month=rawget(tmp,"month"),day=1})
                local tmp2=os.time({year=rawget(tmp,"year"),month=rawget(tmp,"month")+1,day=1})
                return math.floor((tmp2-tmp1)/86398)  -- to avoid any leap seconds
            end

        elseif arg=="add_months" then return function (self,arg2)
                local dim=self:days_in_month()
                __DTm_MT__.__as_date__(self)
                local day=rawget(self,"day") -- did day roll over?
                rawset(self,"month",rawget(self,"month")+arg2)
                __DTm_MT__.__as_time__(self)
                __DTm_MT__.__as_date__(self)
                if rawget(self,"day")~=day then
                    rawset(self,"month",rawget(self,"month")-1)
                end
                __DTm_MT__.__as_time__(self)
                return self
            end

        elseif arg=="add_years" then return function (self,arg2)
                local dim=self:days_in_month()
                __DTm_MT__.__as_date__(self)
                local day=rawget(self,"day") -- did day roll over?
                print("arg2=",arg2)
                rawset(self,"year",rawget(self,"year")+arg2)
                __DTm_MT__.__as_time__(self)
                __DTm_MT__.__as_date__(self)
                if rawget(self,"day")~=day then
                    rawset(self,"month",rawget(self,"month")-1)
                end
                __DTm_MT__.__as_time__(self)
                return self
            end

        elseif arg=="zap_time" then return function()
                __DTm_MT__.__as_date__(self)
                local i,v
                for i,v in ipairs(__timeonlyparts__) do
                    rawset(self,v,nil)
                end
                return self
                end

        elseif arg=="without_time" then return function()
                __DTm_MT__.__as_date__(self)
                return __DTm_MT__.__builder__(nil,rawget(self,"year"),rawget(self,"month"),rawget(self,"day"))
                end

        elseif arg=="EOM" then return function(self)
                end

        elseif arg=="MonthID" then 
            local y=rawget(self,"year")
            assert(y~=nil,"Error DTm: MonthID requires valid year")
            local m=rawget(self,"mon")
            assert(m~=nil,"Error DTm: MonthID requires valid month")
            return (y-2000)*12+m
        else
            return rawget(self,arg)
        end
end

__DTm_MT__.__cmp__=function(a,b,f)
        local bIsDTm_a=bIsDTm(a)
        local bIsDTm_b=bIsDTm(b)
        if bIsDTm_a and bIsDTm_b then return f(a:time(),b:time())
        elseif bIsDTm_a then return f(a:time(),b)
        elseif bIsDTm_b then return f(a,b:time())
        else error("Error DTm: calling __cmp__(a,b) requires at least one to be a DTm object.")
        end
end

__DTm_MT__.__eq=function(a,b) return __DTm_MT__.__cmp__(a,b,function(x,y) return (x==y) end) end
__DTm_MT__.__lt=function(a,b) return __DTm_MT__.__cmp__(a,b,function(x,y) return (x<y) end) end
__DTm_MT__.__le=function(a,b) return __DTm_MT__.__cmp__(a,b,function(x,y) return (x<=y) end) end
__DTm_MT__.__gt=function(a,b) return __DTm_MT__.__cmp__(a,b,function(x,y) return (x>y) end) end
__DTm_MT__.__ge=function(a,b) return __DTm_MT__.__cmp__(a,b,function(x,y) return (x>=y) end) end

__DTm_MT__.__newindex=function(self,key,value)
    if type(key)=="number" then
        assert(key==1 and type(value)=="number","Error DTm: for DTm[k]=v, if k is a number, it must be 1 and v must be a number.")
        __DTm_MT__.__builder__(self,value)
    elseif key=="time" then
        assert(type(value)=="number","Error DTm: for DTm.time=v, v must be a number.")
        __DTm_MT__.__builder__(self,value)
    elseif key=="date" then
        if bIsDTm(value) then
            __DTm_MT__.__builder__(self,value:time())
        elseif type(value)~="table" then
            __DTm_MT__.__builder__(self,value)
        else
            __DTm_MT__.__builder__(self,os.date("*t",value))
        end
    elseif key=="MonthID" then
        local y=math.floor(value-1)
        local m=value-12*y
        __DTm_MT__.__builder__(self,y,m)
    elseif key=="MonthID_EOM" then
        local y=math.floor(value-1)
        local m=value-12*y
        __DTm_MT__.__builder__(self,y,m)
    elseif __osdateparts_keys__[key] then
        __DTm_MT__.__as_date__(self)
        rawset(self,key,value)
    else
        error("Error DTm: unknown __newindex key, "..key)
    end
end


__DTm_new__=function(...)
    return setmetatable({},__DTm_MT__):__new__(...)
end

Dte=AddToModuleHelp{
    Dte=[==[--[[--
            A simple date(time) class to wrap parsers and string output.  
            The abbreviation Dte is used in common with the WDS-ModelSpec
            and to delineate it from other possible date classes.
--]]--]==]
-- @class Dte
} ..
function(...)
    return setmetatable({},__DTm_MT__):__new__(...)
end

DTm=AddToModuleHelp{
    DTm=[==[--[[--
            A simple date-time class to wrap parsers and string output.  
            The abbreviation DTm is used in common with the WDS-ModelSpec
            and to delineate it from other possible date classes.
--]]--]==]
-- @class DTme
} ..
function(...)
    return __DTm_MT__.__builder__(0,...)
end

datetime_parse=AddToModuleHelp{
    datetime_parse=[==[--[[--
            Parses a string and creates an os.date object.
--]]--]==]
-- @function datetime_parse
} .. 
function(arg,fmt) 
    local d=DTm(arg,fmt)
    return d:os_date()
end


if module_name_dots=="main-call-without-args" or wds.bIsMain(table.pack(...),module_name) then

    print(os.date())
    print('datetime_parse("2000-01-01 12:34:56","iso")=',wds.show(datetime_parse("2000-01-01 12:34:56","iso")))
    x=DTm()
    print(x)
    print(wds.show(x))
    print("bIsDTm(x)=",bIsDTm(x))
    x=DTm(2010,3,31)
    print("x=",x)
    print("bIsDTm(x)=",bIsDTm(x))
    print("os.time(x)=",os.time(x))
    print("x:time()=",x:time())
    y=x:time()
    print("y=",y)
    z=DTm(y)
    print("z=",z)
    zwot=z:without_time()
    print("zwot=",zwot)
    print("zwot < DTm(2015,3,15)=",zwot<DTm(2015,3,15))
    print("zwot < DTm(1992,3,15)=",zwot<DTm(1992,3,15))
    print("zwot:days_in_month()=",zwot:days_in_month())
    print("zwot:add_days(31)=",zwot:add_days(31))
    print("DTm(2020,2,3):days_in_month()=",DTm(2020,2,3):days_in_month())
    print("DTm(2020,2,3):add_years(1):days_in_month()=",DTm(2020,2,3):add_years(1):days_in_month())

end


return _M

