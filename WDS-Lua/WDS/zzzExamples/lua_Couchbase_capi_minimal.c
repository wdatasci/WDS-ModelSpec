//This example wraps the Couchbase c-api example minimal.c with the lua c-api.

/* -*- Mode: C; tab-width: 4; c-basic-offset: 4; indent-tabs-mode: nil -*- */
/*
 *     Copyright 2012-2019 Couchbase, Inc.
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 */

/**
 * @file
 *
 * This is a minimal example file showing how to connect to a cluster and
 * set and retrieve a single item.

#include <stdio.h>
#include <libcouchbase/couchbase.h>
#include <stdlib.h>
#include <string.h> // strlen 
#ifdef _WIN32
#define PRIx64 "I64x"
#else
#include <inttypes.h>
#endif

static void die(lcb_INSTANCE *instance, const char *msg, lcb_STATUS err)
{
    fprintf(stderr, "%s. Received code 0x%X (%s)\n", msg, err, lcb_strerror_short(err));
    exit(EXIT_FAILURE);
}

static void store_callback(lcb_INSTANCE *instance, int cbtype, const lcb_RESPSTORE *resp)
{
    lcb_STATUS rc = lcb_respstore_status(resp);
    fprintf(stderr, "=== %s ===\n", lcb_strcbtype(cbtype));
    if (rc == LCB_SUCCESS) {
        const char *key;
        size_t nkey;
        uint64_t cas;
        lcb_respstore_key(resp, &key, &nkey);
        fprintf(stderr, "KEY: %.*s\n", (int)nkey, key);
        lcb_respstore_cas(resp, &cas);
        fprintf(stderr, "CAS: 0x%" PRIx64 "\n", cas);
    } else {
        die(instance, lcb_strcbtype(cbtype), rc);
    }
}

static void get_callback(lcb_INSTANCE *instance, int cbtype, const lcb_RESPGET *resp)
{
    lcb_STATUS rc = lcb_respget_status(resp);
    fprintf(stderr, "=== %s ===\n", lcb_strcbtype(cbtype));
    if (rc == LCB_SUCCESS) {
        const char *key, *value;
        size_t nkey, nvalue;
        uint64_t cas;
        uint32_t flags;
        lcb_respget_key(resp, &key, &nkey);
        fprintf(stderr, "KEY: %.*s\n", (int)nkey, key);
        lcb_respget_cas(resp, &cas);
        fprintf(stderr, "CAS: 0x%" PRIx64 "\n", cas);
        lcb_respget_value(resp, &value, &nvalue);
        lcb_respget_flags(resp, &flags);
        fprintf(stderr, "VALUE: %.*s\n", (int)nvalue, value);
        fprintf(stderr, "FLAGS: 0x%x\n", flags);
    } else {
        die(instance, lcb_strcbtype(cbtype), rc);
    }
}

int main(int argc, char *argv[])
{
    lcb_STATUS err;
    lcb_INSTANCE *instance;
    lcb_CREATEOPTS *create_options = NULL;
    lcb_CMDSTORE *scmd;
    lcb_CMDGET *gcmd;

    if (argc < 2) {
        fprintf(stderr, "Usage: %s couchbase://host/bucket [ password [ username ] ]\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    lcb_createopts_create(&create_options, LCB_TYPE_BUCKET);
    lcb_createopts_connstr(create_options, argv[1], strlen(argv[1]));
    if (argc > 3) {
        lcb_createopts_credentials(create_options, argv[2], strlen(argv[2]), argv[3], strlen(argv[3]));
    }

    err = lcb_create(&instance, create_options);
    lcb_createopts_destroy(create_options);
    if (err != LCB_SUCCESS) {
        die(NULL, "Couldn't create couchbase handle", err);
    }

    err = lcb_connect(instance);
    if (err != LCB_SUCCESS) {
        die(instance, "Couldn't schedule connection", err);
    }

    lcb_wait(instance);

    err = lcb_get_bootstrap_status(instance);
    if (err != LCB_SUCCESS) {
        die(instance, "Couldn't bootstrap from cluster", err);
    }

    // Assign the handlers to be called for the operation types 
    lcb_install_callback(instance, LCB_CALLBACK_GET, (lcb_RESPCALLBACK)get_callback);
    lcb_install_callback(instance, LCB_CALLBACK_STORE, (lcb_RESPCALLBACK)store_callback);

    lcb_cmdstore_create(&scmd, LCB_STORE_UPSERT);
    lcb_cmdstore_key(scmd, "key", strlen("key"));
    lcb_cmdstore_value(scmd, "value", strlen("value"));

    err = lcb_store(instance, NULL, scmd);
    lcb_cmdstore_destroy(scmd);
    if (err != LCB_SUCCESS) {
        die(instance, "Couldn't schedule storage operation", err);
    }

    // The store_callback is invoked from lcb_wait() 
    fprintf(stderr, "Will wait for storage operation to complete..\n");
    lcb_wait(instance);

    // Now fetch the item back 
    lcb_cmdget_create(&gcmd);
    lcb_cmdget_key(gcmd, "key", strlen("key"));
    err = lcb_get(instance, NULL, gcmd);
    if (err != LCB_SUCCESS) {
        die(instance, "Couldn't schedule retrieval operation", err);
    }
    lcb_cmdget_destroy(gcmd);

    // Likewise, the get_callback is invoked from here 
    fprintf(stderr, "Will wait to retrieve item..\n");
    lcb_wait(instance);

    // Now that we're all done, close down the connection handle 
    lcb_destroy(instance);
    return 0;
}
*/

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

//usring setjmp/longjmp in C to handle errors from Couchbase


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
    printf("=== %s ===\n", lcb_strcbtype(cbtype));
    if (rc == LCB_SUCCESS) {
        const char *key;
        size_t nkey;
        uint64_t cas;
        lcb_respstore_key(resp, &key, &nkey);
        printf("KEY: %.*s\n", (int)nkey, key);
        lcb_respstore_cas(resp, &cas);
        printf("CAS: 0x%" PRIx64 "\n", cas);
    } else {
        //die(instance, lcb_strcbtype(cbtype), rc);
        store_callback_env_rc=rc;
        longjmp(store_callback_env,rc);
    }
}

static jmp_buf get_callback_env;
static int     get_callback_env_rc=-1;
static void get_callback(lcb_INSTANCE *instance, int cbtype, const lcb_RESPGET *resp)
{
    lcb_STATUS rc = lcb_respget_status(resp);
    printf("=== %s ===\n", lcb_strcbtype(cbtype));
    if (rc == LCB_SUCCESS) {
        const char *key, *value;
        size_t nkey, nvalue;
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
        //die(instance, lcb_strcbtype(cbtype), rc);
        get_callback_env_rc=rc;
        longjmp(get_callback_env,rc);
    }
}

int l_Couchbase_capi_minimal(lua_State *L)
{
    lcb_STATUS err;
    lcb_INSTANCE *instance;
    lcb_CREATEOPTS *create_options = NULL;
    lcb_CMDSTORE *scmd;
    lcb_CMDGET *gcmd;

    //printf("hey0\n");

    //if (argc < 2) {
    //    fprintf(stderr, "Usage: %s couchbase://host/bucket [ password [ username ] ]\n", argv[0]);
    //    exit(EXIT_FAILURE);
    //}
    //
    //CJW:note, this doc should look like     fprintf(stderr, "Usage: %s couchbase://host/bucket [ username [ password ] ]\n", argv[0]);
    const char *connection_string = luaL_checkstring(L,1);
    const char *username = luaL_checkstring(L,2);
    const char *password = luaL_checkstring(L,3);
    const char *key = luaL_checkstring(L,4);
    const char *value = luaL_checkstring(L,5);

    lcb_createopts_create(&create_options, LCB_TYPE_BUCKET);
    //lcb_createopts_connstr(create_options, argv[1], strlen(argv[1]));
    lcb_createopts_connstr(create_options, connection_string, strlen(connection_string));
    //if (argc > 3) {
        //lcb_createopts_credentials(create_options, argv[2], strlen(argv[2]), argv[3], strlen(argv[3]));
    //}
        lcb_createopts_credentials(create_options, username, strlen(username), password, strlen(password));

    //printf("hey1\n");
    err = lcb_create(&instance, create_options);
    lcb_createopts_destroy(create_options);
    if (err != LCB_SUCCESS) {
        //die(NULL, "Couldn't create couchbase handle", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't create couchbase handle");
        lua_pushnumber(L,err);
        return 3;
    }

    //printf("hey2\n");
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
        //printf("hey3.0.1\n");
        lcb_wait(instance);
        //printf("hey3.0.2\n");
    } else {
        lua_pushnil(L);
        lua_pushstring(L,"Problem with bootstrap status");
        lua_pushnumber(L,store_callback_env_rc);
        return 3;
    }


    //printf("hey4\n");
    

    //printf("connection_string=%s\n",connection_string);
    //printf("username=%s\n",username);
    //printf("password=%s\n",password);
    //printf("key=%s\n",key);
    //printf("value=%s\n",value);



    //printf("hey4.0.1\n");
    err = lcb_get_bootstrap_status(instance);
    //printf("hey4.0.2\n");
    if (err != LCB_SUCCESS) {
        //die(instance, "Couldn't bootstrap from cluster", err);
        //printf("hey4.0.3\n");
        lua_pushnil(L);
        //printf("hey4.0.4\n");
        lua_pushstring(L,"Couldn't bootstrap from cluster");
        //printf("hey4.0.5\n");
        lua_pushnumber(L,err);
        //printf("hey4.0.6\n");
        return 3;
    }

    //printf("hey4.1\n");

    // Assign the handlers to be called for the operation types 
    lcb_install_callback(instance, LCB_CALLBACK_GET, (lcb_RESPCALLBACK)get_callback);
    lcb_install_callback(instance, LCB_CALLBACK_STORE, (lcb_RESPCALLBACK)store_callback);

    //printf("hey4.2\n");

    lcb_cmdstore_create(&scmd, LCB_STORE_UPSERT);
    lcb_cmdstore_key(scmd, key, strlen(key));
    lcb_cmdstore_value(scmd, value, strlen(value));
    //lcb_cmdstore_value_iov(scmd, value, strlen(value));

    //printf("hey5\n");
    err = lcb_store(instance, NULL, scmd);
    lcb_cmdstore_destroy(scmd);
    if (err != LCB_SUCCESS) {
        //die(instance, "Couldn't schedule storage operation", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't schedule store operation");
        lua_pushnumber(L,err);
        return 3;
    }

    //printf("hey6\n");
    // The store_callback is invoked from lcb_wait() 
    //fprintf(stderr, "Will wait for storage operation to complete..\n");
    printf("Will wait for storage operation to complete..\n");
    if (!setjmp(store_callback_env)) {
        lcb_wait(instance);
    } else {
        lua_pushnil(L);
        lua_pushstring(L,"Problem while waiting for storage operation to complete");
        lua_pushnumber(L,store_callback_env_rc);
        return 3;
    }

    // Now fetch the item back 
    lcb_cmdget_create(&gcmd);
    lcb_cmdget_key(gcmd, key, strlen(key));
    err = lcb_get(instance, NULL, gcmd);
    if (err != LCB_SUCCESS) {
        //die(instance, "Couldn't schedule retrieval operation", err);
        lua_pushnil(L);
        lua_pushstring(L,"Couldn't schedule retrieval operation");
        lua_pushnumber(L,err);
        return 3;
    }
    lcb_cmdget_destroy(gcmd);

    // Likewise, the get_callback is invoked from here 
    //fprintf(stderr, "Will wait to retrieve item..\n");
    printf("Will wait to retrieve item..\n");
    if (!setjmp(get_callback_env)) {
        lcb_wait(instance);
    } else {
        lua_pushnil(L);
        lua_pushstring(L,"Problem while waiting for retreive operation to complete");
        lua_pushnumber(L,get_callback_env_rc);
        return 3;
    }


    // Now that we're all done, close down the connection handle 
    lcb_destroy(instance);
    return 0;
}




//the registration function
int luaopen_WDS_zzzExamples_lua_Couchbase_capi_minimal(lua_State *L) {
    lua_register(L,"lua_Couchbase_capi_minimal",l_Couchbase_capi_minimal);
    return 0;
}


