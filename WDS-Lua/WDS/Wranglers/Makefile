
LUA=lua5.3

all:	Couchbase.so xml_expat_base.so

#note LD_LIBRARY_PATH will need to have /usr/local/lib included

Couchbase.so:	Couchbase.c
	gcc -I/usr/include/lua5.3 -llua5.3 -shared -o Couchbase.so -Wall -fPIC Couchbase.c -L/usr/local/lib -lcouchbase

xml_expat_base.so:	xml_expat_base.c
	gcc -I/usr/include/lua5.3 -llua5.3 -Wall -fPIC -L/usr/local/lib -c xml_expat_base.c -o xml_expat_base.o
	gcc -I/usr/include/lua5.3 -shared -Wall -fPIC -L/usr/local/lib xml_expat_base.o -o xml_expat_base.so  -Wl,--as-needed -llua5.3 -lexpat
	-rm xml_expat_base.o

clean:	
	-rm Couchbase.so
	-rm xml_expat_base.so



