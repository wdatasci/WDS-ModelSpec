
LUA=lua5.3


all:	lua_swig_example1.so lua_capi_example1.so


lua_swig_example1.so:	lua_swig_example1.c lua_swig_example1.i
	swig -Wall -lua -o build/lua_swig_example1_wrap.c lua_swig_example1.i
	gcc -I/usr/include/lua5.3 -llua5.3 -shared -o lua_swig_example1.so -Wall -fPIC lua_swig_example1.c build/lua_swig_example1_wrap.c

lua_capi_example1.so:	lua_capi_example1.c
	gcc -I/usr/include/lua5.3 -llua5.3 -shared -o lua_capi_example1.so -Wall -fPIC lua_capi_example1.c

test:	
	for x in *.lua; do ($(LUA) $${x}); done

clean:	
	-rm build/lua_swig_example1_wrap.c
	-rm lua_swig_example1.so
	-rm lua_capi_example1.so



