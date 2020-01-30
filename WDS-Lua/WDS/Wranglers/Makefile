
LUA=lua5.3

all:	Couchbase.so

Couchbase.so:	Couchbase.c
	gcc -I/usr/include/lua5.3 -llua5.3 -shared -o Couchbase.so -Wall -fPIC Couchbase.c -L/usr/lib -lcouchbase

clean:	
	-rm Couchbase.so



