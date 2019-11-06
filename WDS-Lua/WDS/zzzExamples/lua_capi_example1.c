//a standard lua example
//gcc -I/usr/include/lua5.3 -llua5.3 -shared -o AAA.so -Wall -fPIC AAA.c

#include <dirent.h>
#include <errno.h>
#include <string.h>

#include "lua.h"
#include "lauxlib.h"


int l_dir (lua_State *L) {
    DIR *dir;
    struct dirent *entry;
    int i;
    const char *path = luaL_checkstring(L,1);
    /* open directory */
    dir=opendir(path);
    if (dir==NULL) {
        lua_pushnil(L);
        lua_pushstring(L, strerror(errno));
        return 2;
    }

    /* create result table */
    lua_newtable(L);
    i=1;
    while ((entry = readdir(dir)) != NULL) {
        lua_pushinteger(L, i++);
        lua_pushstring(L, entry->d_name);
        lua_settable(L, -3);
    }

    closedir(dir);
    return 1;

}


//the registration function
int luaopen_WDS_zzzExamples_lua_capi_example1(lua_State *L) {
    lua_register(L,"l_dir",l_dir);
    return 0;
}


