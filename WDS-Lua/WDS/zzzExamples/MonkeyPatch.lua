--[[ super basic example of  (mirroring MonkeyPatch.py)
    1: a lua class
        -- in lua, using this as an example of metadata
    2: a subclass
    3: "MonkeyPatching" the subclass
        -- not quite the same thing in lua, but something
        -- kind-of parallel, re-defining "member" functions
    4: (Not applicable in Lua) a basic numpy array

    Other objectives not mirroring Python
    5: closures
--]]

--[[compare objects to ../Python/examples/MonkeyPatch.py
--]]

local printtostring=function(arg) print(tostring(arg)) end

print("pcall(printtostring,...)")
local ok, msg=pcall(printtostring,...)
print("pcall(printtostring,...), ok? ",tostring(ok)," msg=",msg)
if not ok then
    printtostring(msg)
end
print(tostring(arg))

wds=require("WDSUtil.WDS")

-- just for this example, something to mirror np.zeros
zeros=function(dims, dtype)
    nrows=dims[1]
    ncols=dims[2]
    --for dtype everything is a double
    local rv={}
    for i=1,nrows do
        local row={}
        for j=1,ncols do
            table.insert(row,0.0)
        end
        table.insert(rv,row)
    end
    return rv
end
    


--creating an ``object'' in lua is a table with a metatable
--first, without a prototype

--class will be called ``A'' with metatable _AMT (class _ (for hidden), qualifier A (for the object name), representation MT (for metatable))

--here we are using the metatable.__index for the methods only
_AMT={}

_AMT.info={doc="hey, this is a doc string..."}

--see note below on @classmethod, a base constructor has this same behavior
_AMT.new = function(datatype
                    ,nrows
                    ,ncols
                    ,data
                    )
            local rv={}
            rv._datatype=datatype
            rv._nrows=nrows
            rv._ncols=ncols
            rv._data=data
            --note, _AMT has to be declared to use it here, but the function
            --tostring is not defined yet.....
            rv._AMT=_AMT
            return setmetatable(rv,{__index=_AMT,__tostring=_AMT.tostring})
            --return setmetatable(rv,{__index=_AMT}) --,__tostring=_AMT.tostring})
        end

--the "class variables" that are avaiable to all instances of this class
--are just elements of the metatable, getting them to have a nil value is 
--harder, here we are using an empty table
_AMT._class_variable_A={}
_AMT._class_variable_B={}

--to get the Python equivalent of decorating a method as @classmethod, 
--a metatable function just does not have a self
--it should have access to all local variables of the class-like table
_AMT.zeros = function(
                nrows
                ,ncols
                )
            --an example of a tail call which intepreter can do without adding any stack space
            --the interpreter returns directly to the calling point of the wrapping function
            return _AMT.new("double",nrows,ncols,zeros({nrows,ncols},"double"))
    end
            
--note, called as A:tostring() will still pass self as the first argument
_AMT.tostring = function(obj)
    local rv=""
    for i=1,obj._nrows do
        if i>1 then
            rv=rv.."\n"
        end
        for j=1,obj._ncols do
            if j>1 then
                rv=rv..","
            end
            rv=rv..obj._data[i][j]
        end
    end
    return rv
end

_AMT.__tostring=_AMT.tostring

A={}
setmetatable(A,{__index=_AMT,__tostring=_AMT.tostring})

--to set up class B as below, we set up an index that prioritizes 
--the new constructor and then defaults to _AMT

--here we are changing the metatable on _BMT, so that if a call
--(an index lookup) does not exist (has not been overridden)
--it looks it up in AMT

local _BMT={_AMT=_AMT}

_BMT.info={doc="A different doc string"}

_BMT__index=function(t,k)
    if k and rawget(_BMT,k) then
        return rawget(_BMT,k)
    elseif k and _BMT._AMT and rawget(_BMT._AMT,k) then
        return rawget(_BMT._AMT,k)
    end
end

setmetatable(_BMT,{__index=_BMT__index})

_BMT.__tostring=_BMT._AMT.__tostring

_BMT.new = function(datatype
                    ,nrows
                    ,ncols
                    ,data
                    )
            local rv={}
            rv._datatype=datatype
            rv._nrows=nrows
            rv._ncols=ncols
            rv._data=data
            rv._data[1][1]=rv._data[1][1]+123
            rv._BMT=_BMT
            return setmetatable(rv,{__index=_BMT,__tostring=_BMT.tostring})
        end

_BMT.zeros = function(
                nrows
                ,ncols
                )
            --an example of a tail call which intepreter can do without adding any stack space
            --the interpreter returns directly to the calling point of the wrapping function
            return _BMT.new("double",nrows,ncols,zeros({nrows,ncols},"double"))
    end
            

B={}
setmetatable(B,{__index=_BMT,__tostring=_BMT.tostring})


local main = function(args)
    print(wds.show(args))
    print("Test of "..args[0])
    print("help(A)")
    help(A)
    _AMT._class_variable_A=3
    print(wds.show_keys(A))
    print(wds.show_keys(getmetatable(A)))
    print(wds.show_keys(getmetatable(A).__index))
    local aA=A.zeros(3,4)
    aA._AMT._class_variable_B=5
    print("aA="..aA:tostring())
    print("aA=")
    print(aA)
    print("aA._class_variable_A=")
    print(type(aA._class_variable_A))
    show(aA._class_variable_A)
    print("aA._class_variable_B=")
    print(type(aA._class_variable_B))
    show(aA._class_variable_B)

    local aB=B.zeros(2,10)
    print("aB=")
    print(aB)
    print("aB._class_variable_A=")
    print(type(aB._class_variable_A))
    show(aB._class_variable_A)
    print("aB._class_variable_B=")
    print(type(aB._class_variable_B))
    show(aB._class_variable_B)

    --here is the MonkeyPatch, adding something to the methods of B

    aB._BMT.hey=function(a) print("What "..a) end

    print("Monkey patch on B")
    aB.hey("huh")

    print("Did it Monkey patch A? (ok, msg)")
    --aA.hey("huh")
    ok, msg=pcall(aA.hey,"huh")
    print(ok, msg)

end

if wds.is_main(arg) then
    print("if wds.is_main......")
    main(arg)
end



--[[

class A(object):
    #StyleDoc - CJW - class comments are read directly from the first un-named string
    '''Class A is a small wrapper around a numpy array
    '''
    '''Additional doc strings will not show up when calling help(A)
    '''
    #StyleDoc - CJW - using leading _ to denote what in other languages is private or not generally to be used directly

    #CodeDoc - CJW - variables in this scope are available to all instances of this class
    _class_variable_A=None
    _class_variable_B=None

    #CodeDoc - CJW - default constructor
    #There can only be one __init__ constructor in Python (overloading is not possible)
    def __init__(self
                ,datatype=None
                ,rows=None
                ,cols=None
                ,data=None):
        self._datatype=datatype
        self._rows=rows
        self._cols=cols
        self._data=data

    #CodeDoc - CJW - a constructor class method which sets some parameters
    #This enables a constructor of the form:  a=A.zeros(nrows,ncols)
    @classmethod
    def zeros(cls,nrows,ncols):
        return cls(datatype=np.double
            ,rows=nrows
            ,cols=ncols
            ,data=np.zeros([nrows,ncols],dtype=np.double)
            )

    def __repr__(self):
        return str(self._data)


class B(A):
    '''A sub-class of A, an example of using the sub-class to set up a different constructor
    '''
    def __init__(self,nrows,ncols):
        super().__init__(
            datatype=np.double
            ,rows=nrows
            ,cols=ncols
            ,data=np.zeros([nrows,ncols],dtype=np.double)
            )
        self._data+=123.45




#CodeDoc - CJW - see examples/HelloWorld.py
if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        #_parser.add_argument("arg1", help="first argument")
        #_parser.add_argument("arg2", help="second argument")
        #optional switches
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser


    def main(args=None):
        print()
        print("Test of " + __file__)
        a=A
        print()
        print('a default is an instance of A, print(type(a)):')
        print(type(a))
        print('print(a):')
        print(a)
        print()
        print('resetting a using zeros constructor')
        a=A.zeros(10,5)
        print('a=A.zeros(10,5);help(a)')
        help(a)
        print("a=",a)
        print('dir(a)')
        print(dir(a))

    
        print()
        #Forcing a monkeypatch, just by adding a field
        B._hey=8
        print('Forcing a monkeypatch, just by adding a field to the class (definition), B._hey=8')
        print()
        print('print(dir(B)):')
        print(dir(B))

        #adding a method to a class
        print('MonkeyPatch, via adding an attribute:')
        print('def hmm(slf, arg1): slf._data-=arg1')
        print('setattr(B,"hmm",hmm)')
        def hmm(slf, arg1): slf._data-=arg1
        setattr(B,'hmm',hmm)
        print()
        print('now create an instance of B, b=B(3,7)')
        b=B(3,7)
        print("b=",b)
        print('now run the new monkey-patched method, b.hmm(12.345)')
        b.hmm(12.345)
        print("b=",b)
        print('print(dir(b))')
        print(dir(b))


        print()
        print('fin')
        

    l_argparser = main_argparser()
    try:
        args=l_argparser.parse_args()
        if args.pudb:
            pudb.set_trace()
        main(args=args)
    except Exception as e:
        print("Hey")
        print(e)
        print(traceback.format_tb(e.__traceback__))


--]]
