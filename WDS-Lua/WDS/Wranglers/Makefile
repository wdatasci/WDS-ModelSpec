
LUA=lua5.3

all:	Couchbase.so

#note LD_LIBRARY_PATH will need to have /usr/local/lib included

Couchbase.so:	Couchbase.c
	gcc -I/usr/include/lua5.3 -llua5.3 -shared -o Couchbase.so -Wall -fPIC Couchbase.c -L/usr/local/lib -lcouchbase

clean:	
	-rm Couchbase.so



