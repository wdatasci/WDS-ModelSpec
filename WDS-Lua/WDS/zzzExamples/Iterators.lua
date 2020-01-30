--- Test script of iterator structures.
-- @within ExamplesHuh
-- @script Iterators_test



--[[ mirroring ../Python/examples/Iterators.py
    1: basic iterator examples
    2: filter examples
    3: creating an iterator class
    4: traversing a directory
    5: coroutine example in a recursive iterator
--]]

wds=require("WDS")
wdsu=require("WDS.Util")

local arg=arg or table.pack(...)
local is_main=wds.is_main(arg)
print("is_main=",is_main)
print("arg=",wds.show(arg))

local args_opts=require("WDSUtil.args_opts")

    arguments=args_opts.ArgumentParser('usual')

    arguments:add_argument{name="path_of_target_directory"
            , short="p"
            , hasArgument=true
            , help="first argument, path of target directory"
            , default=""
    }

    arguments:add_argument{name="glob_pattern"
            , hasArgument=true
            , help="optional argument for unix-like glob pattern (watch escaping when using p_m)"
            , default="" --{__nil__=true}
    }

    arguments:add_argument{name="CaseInsensitive"
            , short="i"
            , short_negatible="I"
            , aliases={"case-insensitive"}
            , aliases_negatible={"CaseSensitive","case-sensitive"}
            , help="optional argument, for case insensitive"
            , negatible=true
            , default=true
    }
   
    arguments:add_argument{name="recursive"
            , short="r"
            , help="optional argument, for recursive flag for glob"
            , negatible=true
            , default=true 
    }
    
    arguments:add_argument{name="log"
            , short="l"
            , aliases={"verbose"}
            , help="optional argument, for logging"
            , negatible=true
            , default=false 
    }
    
    options_env, options_rem=arguments:parse(arg)
    if options_env.help then
        options_envhelp()
        os.exit()
    end
    -- print("options=",options:show())
    -- print("arg=",wds.show(arg))
    -- print("wds.show(opts_rv1)=",wds.show(opts_rv1))
    -- print("wds.show(opts_rv2)=",wds.show(opts_rv2))








--
--
--
--
--
--


--CodeDoc -CJW - simple logging decorator
--A "decorator" (as I understand it) consumes a object and adds stuff to something
--So, in the python decorator, the __call__ method is a builder


--The example at http://lua-users.org/wiki/DecoratorsAndDocstrings
--is a bit hard to understand, so to walk through it.....
-- -- in order to get the simplified operator look like
-- -- fnc = Decorator{details} .. 
-- --         function () stuff end
--
-- -- Decorator{details} much return something that has the .. or __concat operator
-- -- defined.  
--
-- -- In Python, one can think of the @ operator like a TeX-ish gobble of two arguments things
-- -- and space in between can be ignored, it takes
-- -- @F1 F2 and returns another function which is built up via F1(F2).
--
-- -- With multiple decorators, the convention is that the closest to the final 
-- -- function is operated first, for example, @F1 @F2 @F3 F4 is F1(F2(F3(F4))).
-- -- This is right associative (multiple equivalent binary operations are evaluated
-- -- rightmost first).  
--
-- -- In Lua, ".." is right associative and also gets over multiple spaces in between.
--
-- -- In Lua, one challenge is the space between F1 and F2, although you can 
-- -- call a function like F(1,2,3) (with 3 arguments) or F{1,2,3} (with 1 argument, 
-- -- a table with 3 elements) and you can use F (1,2,3), you cannot use F G(1,2,3)
-- -- to call F(G(1,2,3)).  
--
-- So from the example site, the __concat just spits out the print line operation before the function call
-- Even though the final call looks like a ".." between a decorator and a function, it really is 
-- just returning the final function after the additional interior is performed.  And in the final
-- "random" call below, both typecheck and docstring are equivalent
-- mt = {__concat =
--   function(a,f)
--       return function(...)
--             print("decorator", table.concat(a, ","), ...)
--             return f(...)
--             end
--   end
-- }
-- 
-- function typecheck(...)
--   return setmetatable({...}, mt)
-- end
--
-- function docstring(...)
--   return setmetatable({...}, mt)
-- end
--
-- final form in the example site:
-- random =
--   docstring[[Compute random number.]] ..
--   typecheck("number", '->', "number") ..
--   function(n)
--     return math.random(n)
--   end

--For this simple logging decorator, let's try...


--[[ in Python
#CodeDoc - CJW - simple logging decorator:
__module_log__=''
class LogIt(object):
    def __init__(self,arg):
        global __module_log__
        __module_log__+=str.format('decorating call {} at time.monotonic()={}\n',arg,time.monotonic())
    def __call__(self,fnc):
        global __module_log__
        __module_log__+=str.format('decorating {} at time.monotonic()={}\n',fnc.__name__,time.monotonic())
        def _LogItWrap(*args,**kwargs):
            global __module_log__
            __module_log__+=str.format('Entered into {} at time.monotonic()={}\n',fnc.__name__,time.monotonic())
            fnc(*args,**kwargs)
            __module_log__+=str.format('Exited from {} at time.monotonic()={}\n',fnc.__name__,time.monotonic())
        return _LogItWrap
--]]

bUseLogging=options_env.log

__module_log__=""
-- usage will be:
-- obj=LogIt{MsgTag=[[Object Tag]], MsgAtInit=[[At instantiation]], MsgAtCall=[[At each call]]} ..
--          object

LogIt=function(messages)
    if bUseLogging then
        return setmetatable(messages,{__concat=
                function(messages_w_metatable,fnc)
                    if bUseLogging then
                        local msg=  
                                    messages_w_metatable.MsgTag .. 
                                    ", At Init:" .. 
                                    messages_w_metatable.MsgAtInit .. 
                                    "\n"
                        print(msg)
                        __module_log__=__module_log__ .. msg
                        --print(__module_log__)
                    end
                    return function(...)
                        if bUseLogging then
                            local msg=  
                                     messages_w_metatable.MsgTag .. 
                                     ", At Call:" .. 
                                     messages_w_metatable.MsgAtCall .. 
                                     "("..wds.show({...})..")"..
                                     "\n"
                            print(msg)
                            __module_log__=__module_log__ .. msg
                            --print(__module_log__)
                        end
                        return fnc(...)
                    end
                end
            })
    else 
        return setmetatable({},{__concat=function(jnk,fnc) return fnc end})
    end
end


-- quick test of LogIt
x=LogIt{MsgTag=[[x]]
        ,MsgAtInit=[[First log message]]
        ,MsgAtCall=[[about to run]]
    } ..
    function(a,b)
        return a*b
    end


print("x(2,3)=",x(2,3))

--nilable_instance_of has been moved into WDSUtil/WDS.lua

--[[

#A simple example with a  file descriptor for an example

class OSObject(object):
    '''A simple class as an example with a  file descriptor for an example
    '''
    def __init__(self):
        self._fd=None
        self._local_path=None
--]]


OSObject= {_fd={__nil__=true}
        ,_local_path={__nil__=true}
    }

OSTYPE=os.getenv("OSTYPE") or (function() local h=io.popen("uname") local s=h:read() h:close() return string.lower(string.gsub(s,"[^%w]","")) end )()

assert(OSTYPE=="linux", "this only works when called from a OSTYPE==linux environment")

osp_isdir=function(local_path)
    if os.execute("test -d "..local_path) then
        return true
    else
        return false
    end
end

osp_exists=function(local_path)
    if os.execute("test -e "..local_path) then
        return true
    else
        return false
    end
end

osp_isfile=function(local_path)
    if os.execute("test -f "..local_path) then
        return true
    else
        return false
    end
end

LocalFile=function(local_path)
    local rv=wds.nilable_instance_of(OSObject)
    --assert(os.getenv("OSTYPE")=="linux", "this only works when called from a OSTYPE==linux environment")
    if local_path then
        if osp_isfile(local_path) then
            rv._fd=io.open(local_path,"r")
            rv._local_path=local_path
        else
            error("invalid path for LocalFile, "..local_path)
        end
    end
    return rv
end

--[[

class LocalFile(OSObject):
    def __init__(self
                ,local_path=None
                ):
        super().__init__()
        if not local_path:
            pass
        if (    osp.exists(local_path)
            and osp.isfile(local_path)
            ):
            self._fd=open(local_path,'r')
            self._local_path=local_path
        else:
            raise Exception('invalid path for LocalFile, '+local_path)

--]]

--a python3-ish range iterator, but lua-ish in that end-points are inclusive
range=function(a,b,c) 
    if b==nil then a,b=1,a end 
    if c==nil then c=1 end 
    local _t={a,b,c,0,a-c} 
    return function(t, j) 
                print("incoming _t=",wds.show(_t))
                print("incoming j=",j)
                _t[5]=_t[5]+_t[3]
                if _t[5]<=_t[2] then 
                    -- print("outgoing _t=",wds.show(_t))
                    -- print("outgoing value=",_t[5])
                    return _t[5] 
                end 
            end,_t,0 
end

list=function(f) local rv={} for v in (function () return f, {}, 0 end)()  do i=i+1 table.insert(rv,v) end return rv end

print("for i in range(-3,10,2) do")
for i in range(-3,10,2) do print("i=",i) end


print("for i in range(-3,10) do")
for i in range(-3,10) do print("i=",i) end

print("for i in range(10) do")
for i in range(10) do print("i=",i) end

print("x=list(range(-3,10,2))=")
x=list(range(-3,10,2))
print("x=",wds.show(x))

print("x=list(ipairs(list(range(-3,10,2))))=")
x=list(ipairs(list(range(-3,10,2))))
print("x=",wds.show(x))

-- a decorator to extend a class by wrapping it's metatable __index
AddMethods=function(methods)
        return setmetatable(methods,{__concat=
                function (methods_w_metatable,aClass)
                    --print("adding ",wds.show(methods_w_metatable))
                    --print("to ",wds.show(aClass))
                    local aClass_MT=getmetatable(aClass)
                    local aClass_MTI=aClass_MT.__index
                    aClass_MT.__index=function(t,k)
                        --print("calling updated __index function with t=",wds.show(t)," k=",wds.show(k))
                        if methods[k] then
                            --print("found target in updated __index function with t=",wds.show(t)," k=",wds.show(k))
                            return methods[k]
                        else
                            --print("did not find target in updated __index function with t=",wds.show(t)," k=",wds.show(k))
                            return aClass_MTI(t,k)
                        end
                    end
                    return aClass
                end
            })
end

_os_walk=function(self,options,overrides)
    --print("_os_walk.self=",wds.show(self))
    --print("_os_walk.options=",wds.show(options))
    --print("_os_walk.overrides=",wds.show(overrides))
            local cmd="find "
            if options==nil then
                options={}
            end
            if overrides==nil then
                overrides={}
            end

            if overrides.local_path then
                cmd=cmd..overrides.local_path
            elseif options.local_path then
                cmd=cmd..options.local_path
            else
                cmd=cmd..self._local_path
            end

            if overrides.mindepth then
                cmd=cmd.." -mindepth "..tostring(overrides.mindepth)
            elseif options.mindepth then
                cmd=cmd.." -mindepth "..tostring(options.mindepth)
            end

            if overrides.maxdepth then
                cmd=cmd.." -maxdepth "..tostring(overrides.maxdepth)
            elseif options.maxdepth then
                cmd=cmd.." -maxdepth "..tostring(options.maxdepth)
            end

            if overrides.depth_first or overrides.depth then
                cmd=cmd.." -depth"
            elseif options.depth_first or options.depth then
                cmd=cmd.." -depth"
            end

            if overrides.type then
                if overrides.type~="a" then
                    if string.sub(overrides.type,1,1)=="~" then
                        cmd=cmd .." -not -type "..string.sub(overrides.type,-1,-1)
                    else
                        cmd=cmd .." -type "..overrides.type
                    end
                end
            elseif options.type then
                if options.type~="a" then
                    if string.sub(options.type,1,1)=="~" then
                        cmd=cmd .." -not -type "..string.sub(options.type,-1,-1)
                    else
                        cmd=cmd .." -type "..options.type
                    end
                end
            else
                cmd=cmd .." -type d"
            end
            --print("cmd=",cmd)
            local _h={io.popen(cmd),0,""}
            return function(t,j)
                --print("t=",wds.show(t))
                --print("j=",j)
                local rv=_h[1]:read("l")
                if rv then
                    _h[2]=_h[2]+1
                    _h[3]=rv
                else
                    _h[1].close()
                end
                return rv
            end
        end


local _generator_subdirectories
_generator_subdirectories=function(self,options,overrides)
        --print("options=",wds.show(options))
        --print("overrides=",wds.show(overrides))
            local _hco={{},0,""}
            _hco[1]={mindepth=0,maxdepth=0,type="d",local_path=self._local_path,gglob="*",fileglob="*",dirglob="*",visited={}}
            if options~=nil then
                for k,v in pairs(options) do
                    _hco[1][k]=v
                end
            end
            if overrides~=nil then
                for k,v in pairs(overrides) do
                    _hco[1][k]=v
                end
            end
        --print("_hco[1]=",wds.show(_hco[1]))
            local _co=coroutine.create(function() 
                        --local _lhco={{},0,""}
                        --for k,v in pairs(_hco) do
                            --_lhco[1][k]=v
                        --end
                        --print("before _co body")
                        for s in _os_walk(self,_hco[1]) do
                            --print('s=',s)
                            --if _hco[1][s] then goto continue_s end
                            if _hco[1].dirglob~="*" and string.match(s,_hco[1].dirglob)==nil then goto continue_s end
                            _hco[2]=_hco[2]+1
                            _hco[3]=s
                            _hco[1].visited[s]=true
                            --print('_hco[2]=',wds.show(_hco[2]))
                            --print('_hco[1]=',wds.show(_hco[1]))
                            coroutine.yield(s)
                            if options.type and (options.type=="f" or options.type=="a") then
                                    -- print("s...=",s)
                                for s2 in _os_walk(self,_hco[1],{mindepth=0,maxdepth=1,type="~d",local_path=s}) do
                                    -- print("s2...=",s2)
                                    --print("fileglob...=",_hco[1].fileglob)
                                    if _hco[1].fileglob~="*" and string.match(s2,_hco[1].fileglob)==nil then goto continue_allcontents end
                                    _hco[2]=_hco[2]+1
                                    _hco[3]=s2
                                    _hco[1].visited[s2]=true
                                    coroutine.yield(s2)
                                    ::continue_allcontents::
                                end
                            end
                            local i=0
                            for s2 in _generator_subdirectories(self,options,{mindepth=1,maxdepth=1,type="d",local_path=s}) do
                                i=i+1
                                --print("s2=",s2,i)
                                if _hco[1][s2] then goto continue_s2 end
                                --if _hco[1]._dirglob~="*" and string.match(s2,_olptions._dirglob)==nil then goto continue_s2 end
                                _hco[2]=_hco[2]+1
                                _hco[3]=s2
                                _hco[1].visited[s2]=true
                                coroutine.yield(s2)
                                ::continue_s2::
                            end
                            --]]
                            ::continue_s::
                        end
                        _hco[3]=nil
                        return nil
                    end)
            return function(t,j)
                --just to get the initial calling directory
                --[[
                if options.mindepth and options.mindepth==0 and _hco[1][self._local_path]==nil then
                    if _dirglob~="*" and string.match(self._local_path,_dirglob)==nil then return nil end
                    _hco[1][self._local_path]=true
                    _hco[2]=_hco[2]+1
                    _hco[3]=self._local_path
                    return _hco[3]
                end
                --]]
                --print("t=",wds.show(t))
                --print("j=",wds.show(j))
                --print("_hco=",wds.show(_hco))
                --print("_hco=",wds.show(_hco[1]))
                local status, rv=coroutine.resume(_co)
                --print("rv=",rv)
                return rv
                --j=_hco[2]
                --return _hco[3]
            end, _co, 0
            end



LocalDirectory=function(local_path)
    local rv=AddMethods{
        show=function(self)
            return "LocalDirectory OSObject="..wds.show(self)
        end

        , os_walk_dir=function(self,options,overrides)
            return _os_walk(self,options,overrides)
        end

        , iterator_directory_contents=function(self,options)
            local loptions={mindepth=1,maxdepth=1,type="a"}
            if options and (options.depth_first or options.depth) then
                loptions.depth=true
            end
            return _os_walk(self,loptions)
        end

        , iterator_non_subdirectory_contents=function(self,options)
            local loptions={mindepth=1,maxdepth=1,type="~d"}
            if options and (options.depth_first or options.depth) then
                loptions.depth=true
            end
            return _os_walk(self,loptions)
        end

        , iterator_subdirectories=function(self,options)
            local loptions={mindepth=1,maxdepth=1,type="d"}
            if options and (options.depth_first or options.depth) then
                loptions.depth=true
            end
            return _os_walk(self,loptions)
        end

        , iterator_chained_subdirectories=function(self,options)
            local _h={{},{},{},0,""} -- visited, dir-iterator, non-dir-iterator, initial, value
            return function(t,j)
                -- print("t=",wds.show(t))
                -- print("j=",wds.show(j))
                -- print("_h=",wds.show(_h))
                local rv=""
                while #_h[3]>0 do
                    local srv=_h[3][#_h[3]]({},0)
                    if srv then
                        _h[4]=_h[4]+1
                        _h[5]=srv
                        return srv
                    else
                        _h[3][#_h[3]]=nil
                    end
                end
                if _h[4]==0 or j==0 then
                    table.insert(_h[2],_os_walk(self,{mindepth=0,maxdepth=0,type="d",local_path=self._local_path}))
                end
                while #_h[2]>0 do
                    local rv=_h[2][#_h[2]]({},0)
                    if rv and _h[1][rv]==nil then
                        _h[1][rv]=true
                        if options and options.type~="~d" then
                            table.insert(_h[3],_os_walk(self,{mindepth=1,maxdepth=1,type="~d",local_path=rv}))
                        end
                        table.insert(_h[2],_os_walk(self,{mindepth=1,maxdepth=1,type="d",local_path=rv}))
                        _h[4]=_h[4]+1
                        _h[5]=rv
                        return rv
                    else
                        _h[2][#_h[2]]=nil
                    end
                end
            end
        end


        , generator_subdirectories=_generator_subdirectories

    } .. wds.nilable_instance_of(OSObject).new
    --print(wds.show(rv))
    --assert(os.getenv("OSTYPE")=="linux", "this only works when called from a OSTYPE==linux environment")
    if local_path then
        if osp_isdir(local_path) then
            rv._local_path=local_path
        else
            error("invalid path for LocalDirectory, "..local_path)
        end
    end
    return rv
end



--[[
class LocalDirectory(OSObject):
    def __init__(self
                ,local_path=None
                ):
        super().__init__()
        if not local_path:
            pass
        if (    osp.exists(local_path)
            and osp.isdir(local_path)
            ):
            self._local_path=local_path
        else:
            raise Exception('invalid path for LocalDirectory, '+local_path)

    @LogIt('ClassMethod')
    def os_walk_list(self):
        ''' uses a list-wrap to realize the generator
        '''
        if self._local_path:
            return list(os.walk(self._local_path,))
        else:
            raise Exception('local_path not set for LocalDirectory')
        

    @LogIt('ClassMethod')
    def os_walk(self):
        ''' a printing example to use the "generator" aspect of os.walk
        '''
        if self._local_path:
            i=0
            for v in os.walk(self._local_path):
                i+=1
                print(str.format('element {} of os.walk({}): ',i,self._local_path),v)
            return list(os.walk(self._local_path,))
        else:
            raise Exception('local_path not set for LocalDirectory')
        
    
    

    @LogIt('ClassMethod')
    def glob_list(self
                ,arg                        #glob pattern
                ,case_insensitive=True
                ,recursive=False
                ):
        if self._local_path:
            if arg:
                larg=(arg)
                if case_insensitive:
                    #RefDoc - CJW - hint from https://stackoverflow.com/questions/500864/case-insensitive-python-regular-expression-without-re-compile
                    rv=[]
                    bSubDirInSearch=(arg.find(osp.sep)>=0)
                    regex=fnmatch.translate(arg)
                    regexobj=re.compile('(?i)'+regex)
                    for d,sd,f in os.walk(self._local_path):
                        for v in f:
                            vv=osp.join(d,v)
                            #print(vv)
                            if regexobj.match(vv):
                                rv.append(vv)
                    return rv
                else:
                    return glob.glob(osp.join(self._local_path
                                            ,larg
                                            )
                                        ,recursive=recursive
                                )
            else:
                raise Exception('glob argument not passed')
        else:
            raise Exception('local_path not set for LocalDirectory')
        
    #a class within a class, restricting it's use, at least symbolically, in this class namespace
    class iterator_example(object):
        def __init__(self):
            self._local_data=3

        def __iter__(self):
            self._local_i=-1
            return self

        def __next__(self):
            self._local_i+=1
            #exit criterion
            if self._local_i>=self._local_data: 
                raise StopIteration
            #next value (including the first) yielded
            return self._local_i
            

    #CodeDoc - CJW - until I can figure out how to get the class within a class to access the outside class's namespace
    def iterator_directory_contents(self): return self._iterator_directory_contents(self._local_path)

    def iterator_subdirectories(self): return self._iterator_subdirectories(self._local_path)

    #a class within a class, restricting it's use, at least symbolically, in this class namespace
    class _iterator_directory_contents(object):
        ''' a simple iterator exploiting the glob.iglob iterator
        '''
        def __init__(self
                , local_path
                ):
            self._local_data=glob.iglob(osp.join(local_path,'*'),recursive=False)

        def __iter__(self):
            return self

        def __next__(self):
            return self._local_data.__next__()
            #CodeDoc - CJW - this does not need the exit throw since the glob.iglob iterator raise of StopIteration is not caught
            #But, if the value is stored first, it can be checked against other criterion before returning, such as in the next example.
            #This will be done in the WDS library.

    class _iterator_subdirectories(object):
        ''' a simple iterator exploiting the glob.iglob iterator
        '''
        def __init__(self
                , local_path
                ):
            self._local_data=glob.iglob(osp.join(local_path,'*'),recursive=False)

        def __iter__(self):
            return self

        def __next__(self):
            rv=self._local_data.__next__()
            #print(rv,osp.isdir(rv))
            while not osp.isdir(rv):
                rv=self._local_data.__next__()
            return rv

    #@LogIt('ClassMethod')
    def generator_subdirectories(self):
        for sd in self._iterator_subdirectories(self._local_path):
            yield sd
            sdd=LocalDirectory(sd)
            for ssdd in sdd.generator_subdirectories():
                yield ssdd






#CodeDoc - CJW - see examples/HelloWorld.py
if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        _parser.add_argument("path_of_target_directory"
                            , help="first argument, path of target directory")
        #optional switches
        _parser.add_argument("--glob_pattern"
                            , help="optional argument for unix-like glob pattern (watch escaping when using p_m)"
                            , default=None
                            )
        _parser.add_argument("-i", "--case-insensitive", "--CaseInsensitive"
                            , help="optional argument, for case insensitive"
                            , dest="case_insensitive"
                            , action='store_true'
                            , default=True )
        _parser.add_argument("-I", "--case-sensitive", "--CaseSensitive"
                            , help="optional argument, for case sensitive"
                            , action='store_false'
                            , dest='case_insensitive'
                            , default=None )
        _parser.add_argument("-r", "--recursive"
                            , help="optional argument, for recursive flag for glob"
                            , action='store_true'
                            #, dest='recursive_flag'
                            , default=True )
        _parser.add_argument("--no-recursive"
                            , help="optional argument, for recursive flag set to False for glob"
                            , action='store_false'
                            , dest='recursive'
                            , default=None )
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser


    def main(args=None):
        if not args:
            raise('nothing passed into main')

        for i in range(10): print()

        path_of_target_directory=args.path_of_target_directory
        print("path_of_target_directory=",path_of_target_directory)
        dd=LocalDirectory(path_of_target_directory)

        print()
        print('os_walk_list method:')
        print(dd.os_walk_list())
       
        print()
        print('os_walk method:')
        print(dd.os_walk())

        print()
        if args.glob_pattern:
            if args.case_insensitive:
                print('glob.iglob method:')
            else:
                print('glob.glob method:')
            print(dd.glob_list(args.glob_pattern
                    ,recursive=args.recursive
                    ,case_insensitive=args.case_insensitive
                    ))
        else:
            print('no glob pattern provided')

        print()
        print('iterator examples')

        print()
        print('directory contents')
        for i in dd.iterator_directory_contents(): print(i)

        print()
        print('directory subdirectories')
        for i in dd.iterator_subdirectories(): print(i)

        print()
        print('directory subdirectories via generator recursively')
        for i in dd.generator_subdirectories(): print(i)


        print('Log message')
        global __module_log__
        print(__module_log__)

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


if is_main then
        print("test in "..arg[0])

        if options_env.path_of_target_directory==nil then
            error("nothing passed into main")
        end

        print("path of target directory=",options_env.path_of_target_directory)
        dd=LocalDirectory(options_env.path_of_target_directory)
        -- print(wds.show(getmetatable(dd).__index))
        print("dd:show()=",dd:show())
        f=LocalFile(options_env.path_of_target_directory.."./README.md")
        -- this will fail since f is not a LocalDirectory object with :show extension
        -- print("f:show()=",f:show())
        for s in dd:os_walk_dir() do
            print("subdir=",s)
        end


        --lsR=list(dd:generator_subdirectories({type="f"}))
        -- lsR=list(dd:os_walk_dir())
        -- lsR=list(dd:os_walk_dir({mindepth=0,type="a"}))
        -- lsR=list(dd:generator_subdirectories({mindepth=0,type="a"}))
        --lsR=list(dd:generator_subdirectories({mindepth=0,type="a",glob="Python.examples"}))
        lsR=list(dd:generator_subdirectories({type="a"})) --,fileglob="A",maxdepth=3}))
        print("lsR=",wds.show_values(lsR))

        --os.exit()

        print()
        print('directory contents')

        print()
        print('iterator examples')

        print()
        print('directory contents')
        --for i in dd.iterator_directory_contents(): print(i)
        for i in dd:iterator_directory_contents() do
            print(i)
        end

        print()
        print('directory contents (non-subdirs)')
        --for i in dd.iterator_directory_contents(): print(i)
        for i in dd:iterator_non_subdirectory_contents() do
            print(i)
        end


        print()
        print('directory subdirectories')
        for i in dd:iterator_subdirectories() do
            print(i)
        end

        print()
        print('directory subdirectories chained (one iterator, multi-level)')
        for i in dd:iterator_chained_subdirectories() do
            print(i)
        end

        print()
        print('directory subdirectories chained (one iterator, no maxdepth)')
        for i in dd:os_walk_dir({maxdepth=false}) do
            print(i)
        end

        print()
        print('directory subdirectories via generator recursively (in lua, using coroutines)')
        for i in dd:generator_subdirectories({type="a"}) do
            print(i)
        end

        print()
        print('directory subdirectories via generator recursively (in lua, using coroutines), with fileglob="__init__.py"')
        for i in dd:generator_subdirectories({type="a",fileglob="__init__.py"}) do
            print(i)
        end

        print()

        print('Log message')
        --global __module_log__
        print(__module_log__)

        print()
        print('fin')
        

end

