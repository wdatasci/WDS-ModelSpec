/** 
MIT License

Copyright (c) 2019 Wypasek Data Science, Inc.

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
*/


/// Basic lua Couchbase calls based on lua c-api and Couchbase c-api examples.
// @submodule WDS.Wranglers

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <inttypes.h>
#include <errno.h>

#include <dirent.h>
#include "lua.h"
#include "lauxlib.h"

#include <setjmp.h>
#include <libcouchbase/couchbase.h>

//using setjmp/longjmp in C to handle errors from Couchbase

static jmp_buf bootstrap_callback_env;
static int     bootstrap_callback_env_rc=-1;
static void bootstrap_callback(lcb_INSTANCE *instance, lcb_STATUS err)
{
    if (err == LCB_SUCCESS) {
        printf( "In bootstrap_callback with success");
    } else {
        printf( "In bootstrap_callback with err, %d", err);
        bootstrap_callback_env_rc=-1;
        longjmp(bootstrap_callback_env,-1);
    }
}

static jmp_buf store_callback_env;
static int     store_callback_env_rc=-1;
static void store_callback(lcb_INSTANCE *instance, int cbtype, const lcb_RESPSTORE *resp)
{
    lcb_STATUS rc = lcb_respstore_status(resp);
    //printf("=== %s ===\n", lcb_strcbtype(cbtype));
    if (rc == LCB_SUCCESS) {
        const char *key;
        size_t nkey;
        uint64_t cas;
        lcb_respstore_key(resp, &key, &nkey);
        //printf("KEY: %.*s\n", (int)nkey, key);
        lcb_respstore_cas(resp, &cas);
        //printf("CAS: 0x%" PRIx64 "\n", cas);
    } else {
        //die(instance, lcb_strcbtype(cbtype), rc);
        store_callback_env_rc=rc;
        longjmp(store_callback_env,rc);
    }
}

static jmp_buf get_callback_env;
static int     get_callback_env_rc=-1;


int Couchbase_CAPI_store(lua_State *L)
{
    lcb_STATUS err;
    lcb_INSTANCE *instance;
    lcb_CREATEOPTS *create_options = NULL;
    lcb_CMDSTORE *scmd;

    const char *connection_string = luaL_checkstring(L,1);
    const char *username = luaL_checkstring(L,2);
    const char *password = luaL_checkstring(L,3);
    const char *key = luaL_checkstring(L,4);
    const char *value = luaL_checkstring(L,5);

    lcb_createopts_create(&create_options, LCB_TYPE_BUCKET);
    lcb_createopts_connstr(create_options, connection_string, strlen(connection_string));
    lcb_createopts_credentials(create_options, username, strlen(username), password, strlen(password));

    err = lcb_create(&instance, create_options);
    lcb_createopts_destroy(create_options);
    if (err != LCB_SUCCESS) {
        //die(NULL, "Couldn't create couchbase handle", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't create couchbase handle");
        lua_pushnumber(L,err);
        return 3;
    }

    err = lcb_connect(instance);
    if (err != LCB_SUCCESS) {
        //die(instance, "Couldn't schedule connection", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't schedule connection");
        lua_pushnumber(L,err);
        return 3;
    }

    lcb_set_bootstrap_callback(instance, (lcb_bootstrap_callback)bootstrap_callback);
    if (!setjmp(bootstrap_callback_env)) {
        lcb_wait(instance);
    } else {
        lua_pushnil(L);
        lua_pushstring(L,"Problem with bootstrap status");
        lua_pushnumber(L,store_callback_env_rc);
        return 3;
    }

    //printf("connection_string=%s\n",connection_string);
    //printf("username=%s\n",username);
    //printf("password=%s\n",password);
    //printf("key=%s\n",key);
    //printf("value=%s\n",value);

    err = lcb_get_bootstrap_status(instance);
    if (err != LCB_SUCCESS) {
        //die(instance, "Couldn't bootstrap from cluster", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't bootstrap from cluster");
        lua_pushnumber(L,err);
        return 3;
    }

    lcb_install_callback(instance, LCB_CALLBACK_STORE, (lcb_RESPCALLBACK)store_callback);

    lcb_cmdstore_create(&scmd, LCB_STORE_UPSERT);
    lcb_cmdstore_key(scmd, key, strlen(key));
    lcb_cmdstore_value(scmd, value, strlen(value));
    //lcb_cmdstore_value_iov(scmd, value, strlen(value));

    err = lcb_store(instance, NULL, scmd);
    lcb_cmdstore_destroy(scmd);
    if (err != LCB_SUCCESS) {
        //die(instance, "Couldn't schedule storage operation", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't schedule store operation");
        lua_pushnumber(L,err);
        return 3;
    }

    //The store_callback is invoked from lcb_wait() 
    printf("Will wait for storage operation to complete..\n");
    if (!setjmp(store_callback_env)) {
        lcb_wait(instance);
    } else {
        lua_pushnil(L);
        lua_pushstring(L,"Problem while waiting for storage operation to complete");
        lua_pushnumber(L,store_callback_env_rc);
        return 3;
    }

    lua_pushnumber(L,0);
    lua_pushstring(L,"Success");

    lcb_destroy(instance);
    return 0;
}


int Couchbase_CAPI_get(lua_State *L)
{
    lcb_STATUS err;
    lcb_INSTANCE *instance;
    lcb_CREATEOPTS *create_options = NULL;
    lcb_CMDGET *gcmd;

    const char *connection_string = luaL_checkstring(L,1);
    const char *username = luaL_checkstring(L,2);
    const char *password = luaL_checkstring(L,3);
    const char *key = luaL_checkstring(L,4);
    //const char *value = luaL_checkstring(L,5);

    lcb_createopts_create(&create_options, LCB_TYPE_BUCKET);
    lcb_createopts_connstr(create_options, connection_string, strlen(connection_string));
    lcb_createopts_credentials(create_options, username, strlen(username), password, strlen(password));

    err = lcb_create(&instance, create_options);
    lcb_createopts_destroy(create_options);
    if (err != LCB_SUCCESS) {
        //die(NULL, "Couldn't create couchbase handle", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't create couchbase handle");
        lua_pushnumber(L,err);
        return 3;
    }

    err = lcb_connect(instance);
    if (err != LCB_SUCCESS) {
        //die(instance, "Couldn't schedule connection", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't schedule connection");
        lua_pushnumber(L,err);
        return 3;
    }

    //printf("hey3\n");
    lcb_set_bootstrap_callback(instance, (lcb_bootstrap_callback)bootstrap_callback);
    if (!setjmp(bootstrap_callback_env)) {
        lcb_wait(instance);
    } else {
        lua_pushnil(L);
        lua_pushstring(L,"Problem with bootstrap status");
        lua_pushnumber(L,store_callback_env_rc);
        return 3;
    }

    err = lcb_get_bootstrap_status(instance);
    if (err != LCB_SUCCESS) {
        //die(instance, "Couldn't bootstrap from cluster", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't bootstrap from cluster");
        lua_pushnumber(L,err);
        return 3;
    }

    // Assign the handlers to be called for the operation types 
    size_t nvalue=0;
    const char* value;
    // localizing the callback to return value to this function space
    void get_callback2(lcb_INSTANCE *instance, int cbtype, const lcb_RESPGET *resp)
    {
        printf("=== %s ===\n", lcb_strcbtype(cbtype));
        lcb_STATUS rc = lcb_respget_status(resp);
        printf("=== %s ===\n", lcb_strcbtype(cbtype));
        if (rc == LCB_SUCCESS) {
            const char *key;
            size_t nkey;
            uint64_t cas;
            uint32_t flags;
            lcb_respget_key(resp, &key, &nkey);
            printf("KEY: %.*s\n", (int)nkey, key);
            lcb_respget_cas(resp, &cas);
            printf("CAS: 0x%" PRIx64 "\n", cas);
            lcb_respget_value(resp, &value, &nvalue);
            lcb_respget_flags(resp, &flags);
            printf("VALUE: %.*s\n", (int)nvalue, value);
            printf("FLAGS: 0x%x\n", flags);
        } else {
            printf("Huh?\n");
            //die(instance, lcb_strcbtype(cbtype), rc);
            get_callback_env_rc=rc;
            longjmp(get_callback_env,rc);
        }
    }

    printf("hey 1\n");
    lcb_install_callback(instance, LCB_CALLBACK_GET, (lcb_RESPCALLBACK)get_callback2);
    printf("hey 2\n");

    //Now fetch the item back 
    lcb_cmdget_create(&gcmd);
    printf("hey\n");
    lcb_cmdget_key(gcmd, key, strlen(key));
    printf("hey\n");
    printf("before key VALUE: %.*s\n", (int)strlen(key), key);
    err = lcb_get(instance, NULL, gcmd);
    printf("hey\n");
    if (err != LCB_SUCCESS) {
        //die(instance, "Couldn't schedule retrieval operation", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't schedule retrieval operation");
        lua_pushnumber(L,err);
        return 3;
    }

    printf("Will wait to retrieve item..\n");
    if (!setjmp(get_callback_env)) {
        lcb_wait(instance);
    } else {
        lua_pushnil(L);
        lua_pushstring(L,"Problem while waiting for retreive operation to complete");
        lua_pushnumber(L,get_callback_env_rc);
        return 3;
    }

    lcb_cmdget_destroy(gcmd);

    if (nvalue>0) {
        printf("OUTSIDE VALUE: %.*s\n", (int)nvalue, value);
    }

    lua_pushnumber(L,0);
    lua_pushstring(L,value);

    lcb_destroy(instance);
    return 2;
}



//the registration function
int luaopen_WDS_Wranglers_Couchbase(lua_State *L) {
    lua_register(L,"Couchbase_CAPI_store",Couchbase_CAPI_store);
    lua_register(L,"Couchbase_CAPI_get",Couchbase_CAPI_get);
    return 0;
}


