
LUA=lua5.3

#the newer library uses lcb_wait with 2 arguments (lcb_wait3 in older library)
COUCHBASE_FLAGS=-DUSE_NEW_LCB_WAIT=1
COUCHBASE_FLAGS=-DUSE_NEW_LCB_WAIT=0

all:	Couchbase.so

Couchbase.so:	Couchbase.c
	gcc -I/usr/include/lua5.3 -llua5.3 -shared -o Couchbase.so -Wall -fPIC Couchbase.c -L/usr/lib -lcouchbase

clean:	
	-rm Couchbase.so



