# WDS-Lua
Supporting Lua module(s).

The main module is WDS.lua, which after requiring, one can use WDS.SUB or WDS.SUB.SUB.

Wrapping of Couchbase's C API (libcouchbase) is contained in WDS/Wranglers and a build is required.  
The build has been tested on WSL-ubuntu, AWS/AWS-linux, and AWS/AWS-ubuntu.

Luarocks prerequisites: alt-getopt, argparse, debugger, ldoc, lua-curl, lua-gnuplot 

Other prerequisites: libcouchbase, readline


A wrap of expat is contained in WDS/Wranglers and also requires a build.  This is currently under
construction, but differs from some xml handlers in that comment objects and order are preserved.

Prerequisities:  libexpat-dev



For additional detail and comments, please build Lua doc directory via ldoc.  
In addition to the WDS.help CLI functionality, ldoc style comments are partially available. 
Construct with "ldoc -B ./config.ld".



