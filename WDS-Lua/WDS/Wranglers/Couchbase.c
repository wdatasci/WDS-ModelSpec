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
#include <stdbool.h>
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
        //printf( "In bootstrap_callback with success");
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
    if (rc == LCB_SUCCESS) {
        //const char *key;
        //size_t nkey;
        //uint64_t cas;
        //lcb_respstore_key(resp, &key, &nkey);
        ////printf("KEY: %.*s\n", (int)nkey, key);
        //lcb_respstore_cas(resp, &cas);
        ////printf("CAS: 0x%" PRIx64 "\n", cas);
    } else {
        //die(instance, lcb_strcbtype(cbtype), rc);
        store_callback_env_rc=rc;
        longjmp(store_callback_env,rc);
    }
}

static jmp_buf get_callback_env;
static int     get_callback_env_rc=-1;
//get_callback assigned in localized space

//static jmp_buf query_callback_env;
//static int     query_callback_env_rc=-1;
//query_callback assigned in localized space

static jmp_buf row_callback_env;
static int     row_callback_env_rc=-1;
//row_callback assigned in localized space

static lcb_STATUS Couchbase_CAPI_createopts(lcb_INSTANCE** dptr_instance
        , lcb_CREATEOPTS** dptr_create_options
        , const char* connection_string
        , const char* username
        , const char* password
        ){
    lcb_STATUS err;
    lcb_createopts_create(dptr_create_options, LCB_TYPE_BUCKET);
    lcb_createopts_connstr(*dptr_create_options, connection_string, strlen(connection_string));
    lcb_createopts_credentials(*dptr_create_options, username, strlen(username), password, strlen(password));
    err = lcb_create(dptr_instance, *dptr_create_options);
    lcb_createopts_destroy(*dptr_create_options);
    return err;
}

int lua_return_Couchbase_code(lua_State* L, lcb_INSTANCE** dptr_instance, int rc, const char* msg) {
    lua_pushnumber(L,rc);
    lua_pushstring(L,msg);
    lcb_destroy(*dptr_instance);
    return 2;
}

int lua_return_Couchbase_error(lua_State* L, lcb_INSTANCE** dptr_instance, lcb_STATUS err, const char* msg) {
    char message[512]="Error Couchbase_CAPI: ";
    lua_pushnil(L);
    lua_pushnumber(L,err);
    lua_pushstring(L,strcat(message,msg));
    lcb_destroy(*dptr_instance);
    return 3;
}

// from libcouchbase examples
//static void ln2space(const void *buf, size_t nbuf){
//    size_t i;
//    char *str=(char*)buf;
//    for (i=0;i<nbuf;i++){
//        if (str[i]=='\n') str[i]=' ';
//    }
//}

int err2color(lcb_STATUS err){
    switch (err) {
        case LCB_SUCCESS:
            return 32;
        case LCB_ERR_DOCUMENT_EXISTS:
            return 33;
        default:
            return 31;
    }
}

/***
Store a key-value in a Couchbase bucket.
@function Couchbase_CAPI_store
@param connection_string in the style of couchbase://<<host>>
@param bucket (appended to connection string for the host, i.e., couchbase://localhost/BucketName)
@param username
@param password
@param key (document name to be placed in the corresponding bucket)
@param value (document to be stored)
*/


int Couchbase_CAPI_store(lua_State *L){
    lcb_STATUS err;
    lcb_INSTANCE *instance;
    lcb_CREATEOPTS *create_options = NULL;
    lcb_CMDSTORE *scmd;

    const char *connection_string = luaL_checkstring(L,1);
    const char *bucket = luaL_checkstring(L,2);
    const char *username = luaL_checkstring(L,3);
    const char *password = luaL_checkstring(L,4);
    const char *key = luaL_checkstring(L,5);
    const char *value = luaL_checkstring(L,6);

    char conn[1024]={0};
    strcpy(conn,connection_string);
    strcat(conn,"/");
    strcat(conn,bucket);

    err = Couchbase_CAPI_createopts(&instance, &create_options, conn, username, password);
    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not create couchbase handle");

    err = lcb_connect(instance);
    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not schedule connection");

    lcb_set_bootstrap_callback(instance, (lcb_bootstrap_callback)bootstrap_callback);
    if (!setjmp(bootstrap_callback_env)) lcb_wait(instance);
    else return lua_return_Couchbase_error(L,&instance,bootstrap_callback_env_rc,"Problem with bootstrap status");

    err = lcb_get_bootstrap_status(instance);
    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not bootstrap from cluster");

    lcb_install_callback(instance, LCB_CALLBACK_STORE, (lcb_RESPCALLBACK)store_callback);

    lcb_cmdstore_create(&scmd, LCB_STORE_UPSERT);
    lcb_cmdstore_key(scmd, key, strlen(key));
    lcb_cmdstore_value(scmd, value, strlen(value));
    //lcb_cmdstore_value_iov(scmd, value, strlen(value));

    err = lcb_store(instance, NULL, scmd);
    lcb_cmdstore_destroy(scmd);

    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not schedule store operation");
    if (!setjmp(store_callback_env)) lcb_wait(instance);
    else return lua_return_Couchbase_error(L,&instance,store_callback_env_rc,"Problem while waiting for storage operation to complete");

    return lua_return_Couchbase_code(L,&instance,0,"Success");
}

/***
Get the value associated with a key in a Couchbase bucket.
@function Couchbase_CAPI_get
@param connection_string in the style of couchbase://<<host>>
@param bucket (appended to connection string for the host, i.e., couchbase://localhost/BucketName)
@param username
@param password
@param key (document name to be placed in the corresponding bucket)
*/

int Couchbase_CAPI_get(lua_State *L){
    lcb_STATUS err;
    lcb_INSTANCE *instance;
    lcb_CREATEOPTS *create_options = NULL;
    lcb_CMDGET *gcmd;

    const char *connection_string = luaL_checkstring(L,1);
    const char *bucket = luaL_checkstring(L,2);
    const char *username = luaL_checkstring(L,3);
    const char *password = luaL_checkstring(L,4);
    const char *key = luaL_checkstring(L,5);

    char conn[1024]={0};
    strcpy(conn,connection_string);
    strcat(conn,"/");
    strcat(conn,bucket);

    err = Couchbase_CAPI_createopts(&instance, &create_options, conn, username, password);
    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not create couchbase handle");

    err = lcb_connect(instance);
    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not schedule connection");

    lcb_set_bootstrap_callback(instance, (lcb_bootstrap_callback)bootstrap_callback);
    if (!setjmp(bootstrap_callback_env)) lcb_wait(instance);
    else return lua_return_Couchbase_error(L,&instance,bootstrap_callback_env_rc,"Problem with bootstrap status");

    err = lcb_get_bootstrap_status(instance);
    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not bootstrap from cluster");

    size_t nvalue=0;
    const char* value;
    uint64_t cas=0;
    uint32_t flags=0;

    // localizing the callback to return value to this function space
    void get_callback2(lcb_INSTANCE *instance, int cbtype, const lcb_RESPGET *resp)
    {
        lcb_STATUS rc = lcb_respget_status(resp);
        if (rc == LCB_SUCCESS) {
            lcb_respget_cas(resp, &cas);
            lcb_respget_value(resp, &value, &nvalue);
            lcb_respget_flags(resp, &flags);
        } else {
            get_callback_env_rc=rc;
            longjmp(get_callback_env,rc);
        }
    }

    lcb_install_callback(instance, LCB_CALLBACK_GET, (lcb_RESPCALLBACK)get_callback2);

    //Now fetch the item back 
    lcb_cmdget_create(&gcmd);
    lcb_cmdget_key(gcmd, key, strlen(key));
    err = lcb_get(instance, NULL, gcmd);
    lcb_cmdget_destroy(gcmd);

    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not schedule retrieval operation");

    if (!setjmp(get_callback_env)) lcb_wait(instance);
    else return lua_return_Couchbase_error(L,&instance,get_callback_env_rc,"Problem while waiting for retreive operation to complete");

    lua_pushnumber(L,0);
    lua_pushstring(L,value);
    lua_pushinteger(L,(int)cas);
    lua_pushinteger(L,(int)flags);
    lcb_destroy(instance);
    return 4;
}

/***
Get the result of a N1QL query of a key in a Couchbase bucket.
@function Couchbase_CAPI_query
@param connection_string in the style of couchbase://<<host>>
@param bucket (appended to connection string for the host, i.e., couchbase://localhost/BucketName)
@param username
@param password
@param query in N1QL syntax, possibly with optional positional replacement
@param optional value 1, replacement value for placeholder $1 in the query
*/

int Couchbase_CAPI_query(lua_State *L){
    lcb_STATUS err;
    lcb_INSTANCE *instance;
    lcb_CREATEOPTS *create_options = NULL;
    lcb_CMDN1QL *gcmd;

    const char *connection_string = luaL_checkstring(L,1);
    const char *bucket = luaL_checkstring(L,2);
    const char *username = luaL_checkstring(L,3);
    const char *password = luaL_checkstring(L,4);
    const char *query = luaL_checkstring(L,5);
    const char *param1 = ( (lua_absindex(L,-1)>5) ? luaL_checkstring(L,6) : "\"\"" );

    //in the current library, there is only one positional parameter $1
    //const char *param2 = ( (lua_absindex(L,-1)>6) ? luaL_checkstring(L,7) : "\"\"" );

    char conn[1024]={0};
    strcpy(conn,connection_string);
    strcat(conn,"/");
    strcat(conn,bucket);

    err = Couchbase_CAPI_createopts(&instance, &create_options, conn, username, password);
    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not create couchbase handle");

    err = lcb_connect(instance);
    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not schedule connection");

    lcb_set_bootstrap_callback(instance, (lcb_bootstrap_callback)bootstrap_callback);
    if (!setjmp(bootstrap_callback_env)) lcb_wait(instance);
    else return lua_return_Couchbase_error(L,&instance,bootstrap_callback_env_rc,"Problem with bootstrap status");

    err = lcb_get_bootstrap_status(instance);
    if (err != LCB_SUCCESS) return lua_return_Couchbase_error(L,&instance,err,"Could not bootstrap from cluster");

    size_t nvalue=0;
    const char* value;
    uint64_t cas=0;
    uint32_t flags=0;
    const char *row1="";
    size_t nrow1=0;
    size_t nrows=0;
    bool bHasInitialRVs=false;
    bool bHasSummaryRV=false;

    // localizing error return case if nrows>0
    int local_lua_return_Couchbase_error(lua_State* L, lcb_INSTANCE** dptr_instance, lcb_STATUS err, const char* msg) {
        if (bHasSummaryRV) lua_pop(L,1);
        if (bHasInitialRVs) lua_pop(L,2);
        char message[1024]="Error Couchbase_CAPI: ";
        lua_pushnil(L);
        lua_pushnumber(L,err);
        lua_pushstring(L,strcat(message,msg));
        lcb_destroy(*dptr_instance);
        return 3;
    }

    // localizing the callback to return value to this function space
    void get_callback2(lcb_INSTANCE *instance, int cbtype, const lcb_RESPGET *resp)
    {
        lcb_STATUS rc = lcb_respget_status(resp);
        if (rc == LCB_SUCCESS) {
            lcb_respget_cas(resp, &cas);
            lcb_respget_value(resp, &value, &nvalue);
            lcb_respget_flags(resp, &flags);
        } else {
            get_callback_env_rc=rc;
            longjmp(get_callback_env,rc);
        }
    }
    lcb_install_callback(instance, LCB_CALLBACK_GET, (lcb_RESPCALLBACK)get_callback2);

    //int rc_index=0;
    int rv_index=0;
    //int rs_index=0;

    // localizing the callback to return value to this function space
    void row_callback2(lcb_INSTANCE *instance, int cbtype, const lcb_RESPN1QL *resp)
    {
        lcb_STATUS rc = lcb_respn1ql_status(resp);
        //ln2space(row,nrow);
        if (rc == LCB_SUCCESS) {
            rc=lcb_respn1ql_row(resp, &row1, &nrow1);
            //printf("h=[\x1b[%dmQUERY\x1b[0m] %s, (%d) >>>>>%.*s<<<<<\n"
            //      , err2color(rc), lcb_strerror_short(rc), (int)nrow1, (int)nrow1, row1);
            if (!bHasInitialRVs) {
                lua_pushnumber(L,0);
                //rc_index=lua_absindex(L,-1); //top
                lua_newtable(L);
                rv_index=lua_absindex(L,-1); //top
                bHasInitialRVs=true;
            }
            if (lcb_respn1ql_is_final(resp)) {
                if (!bHasSummaryRV) {
                    bHasSummaryRV=true;
                    lua_pushstring(L,row1);
                    //rs_index=lua_absindex(L,-1); //top
                }
            } else {
                nrows+=1;
                //Note, through testing, the couchbase pull may not 0-terminate.
                //Here, strncpy'ing to buffer to enable a 0-terminal.
                char buf[16384]={0};
                strncpy(buf,row1,nrow1);
                lua_pushfstring(L,"%s",buf);
                lua_seti(L,rv_index,nrows);
            }
        } else {
            row_callback_env_rc=rc;
            longjmp(row_callback_env,rc);
        }
    }

    //Now fetch the item back 
    //int i=0;printf("hey %d\n",++i);
    lcb_cmdn1ql_create(&gcmd);
    err = lcb_cmdn1ql_statement(gcmd, query, strlen(query));
    if (err != LCB_SUCCESS) return local_lua_return_Couchbase_error(L,&instance,err,"set query statement");

    //printf("hey %d\n",++i);
    if (strcmp(param1,"\"\"")!=0) {
        err = lcb_cmdn1ql_positional_param(gcmd, param1, strlen(param1));
        if (err != LCB_SUCCESS) return local_lua_return_Couchbase_error(L,&instance,err,"set query positional parameters");
    }

    //if (strcmp(param2,"\"\"")!=0) {
    //    err = lcb_cmdn1ql_positional_param(gcmd, param2, strlen(param2));
    //    if (err != LCB_SUCCESS) return local_lua_return_Couchbase_error(L,&instance,err,"set query positional parameters");
    //}


    //printf("hey %d\n",++i);
    err = lcb_cmdn1ql_option(gcmd,"pretty",strlen("pretty"),"false",strlen("false"));
    if (err != LCB_SUCCESS) return local_lua_return_Couchbase_error(L,&instance,err,"set query 'pretty' option");

    //printf("hey %d\n",++i);
    lcb_cmdn1ql_callback(gcmd, row_callback2);
    err = lcb_n1ql(instance, NULL, gcmd);
    if (err != LCB_SUCCESS) return local_lua_return_Couchbase_error(L,&instance,err,"schedule query operation");

    //printf("hey %d\n",++i);
    lcb_cmdn1ql_destroy(gcmd);

    //printf("hey %d\n",++i);
    if (!setjmp(row_callback_env)) lcb_wait(instance);
    else return local_lua_return_Couchbase_error(L,&instance,row_callback_env_rc,"Problem while waiting for query operation to complete");

    //printf("hey %d\n",++i);
    //outputs are initialized in row_callback
    lcb_destroy(instance);
    return 3;
}




//the registration function
int luaopen_WDS_Wranglers_Couchbase(lua_State *L) {
    lua_register(L,"Couchbase_CAPI_store",Couchbase_CAPI_store);
    lua_register(L,"Couchbase_CAPI_get",Couchbase_CAPI_get);
    lua_register(L,"Couchbase_CAPI_query",Couchbase_CAPI_query);
    return 0;
}


