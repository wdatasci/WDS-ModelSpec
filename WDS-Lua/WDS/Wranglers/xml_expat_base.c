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


/// A basic lua api wrap of expat to produce lua structures that maintain xml 
// parsing order and comments.  Based on reference examples of libexpat.
// @submodule WDS.Wranglers
//

#include <stdio.h>
#include <expat.h>
#include <stdbool.h>
#include <string.h>

#include "lua.h"
#include "lauxlib.h"

#include <setjmp.h>

#ifdef XML_LARGE_SIZE
#  define XML_FMT_INT_MOD "ll"
#else
#  define XML_FMT_INT_MOD "l"
#endif

#ifdef XML_UNICODE_WCHAR_T
#  define XML_FMT_STR "ls"
#else
#  define XML_FMT_STR "s"
#endif

//#define BUFFSIZE 8192
//char Buff[BUFFSIZE];
//char* indent="  ";

int __XML_class__index = 0;

int StartingTop;

bool bHasAnyReturnValue=false;

static jmp_buf callback_env;
static int     callback_env_rc=-1;


static void XMLCALL aElementStartCallback(void *userData, const XML_Char *name, const XML_Char **attr_list) {
    int i;
    void** luserData=(void**) userData;
    lua_State* lL=(lua_State*) luserData[0];
    bHasAnyReturnValue=true;

    lua_newtable(lL);
    lua_pushstring(lL,"__QName__");
    lua_pushstring(lL,name);
    lua_settable(lL,-3);
    lua_pushstring(lL,"__XML__");
    lua_pushboolean(lL,1);
    lua_settable(lL,-3);

    if (__XML_class__index>0) {
        lua_pushnil(lL);
        lua_copy(lL,__XML_class__index,lua_gettop(lL));
        lua_setmetatable(lL,-2);
    }


    if (attr_list[0]) {
        lua_pushstring(lL,"__AttrList__");
        lua_newtable(lL);
        for (i=0; attr_list[i]!=NULL; i += 2) {
            lua_pushstring(lL,attr_list[i]);
            lua_pushstring(lL,attr_list[i+1]);
            lua_settable(lL,-3);
        }
        lua_settable(lL,-3);
    }

    //for (i = 0; i < StartingTop; i++) printf("%s",indent);
    //printf("E=%" XML_FMT_STR, name);
    //for (i = 0; attr_list[i]; i += 2) printf(" A=%" XML_FMT_STR "='%" XML_FMT_STR "'", attr_list[i], attr_list[i + 1]);
    //printf("\n");
}

static void XMLCALL aElementEndCallBack(void *userData, const XML_Char *name) {
    void** luserData=(void**) userData;
    lua_State* lL=(lua_State*) luserData[0];

    (void)name;

    if (lua_gettop(lL)>StartingTop+1) {
        int top=lua_gettop(lL)-1;
        int toprawlen=lua_rawlen(lL,top);
        lua_rawseti(lL,top,toprawlen+1);
    }

}

static void aCharacterDataCallBack(void *userData, const char *s, int l){ 
    void** luserData=(void**) userData;
    lua_State* lL=(lua_State*) luserData[0];
    lua_Alloc __lua_Alloc=(lua_Alloc) luserData[1];

    int i=0;
    bool found=((int)s[i])>32;
    if ( !found ) {
        for (i=0;!found && i<l;i++) found=((int)s[i])>32;
        if (found) i-=1;
    }
    if (found) {
        char* buf=NULL;
        buf=__lua_Alloc(NULL,buf,0,l-i+1);
        if (buf==NULL) longjmp(callback_env,-100);
        strncpy(buf,&s[i],l-i);
        buf[l-i]='\0';
        //if (found) printf("              DH%s\n",buf); 
        int top=lua_gettop(lL);
        int toprawlen=lua_rawlen(lL,top);
        lua_pushfstring(lL,"%s",buf);
        lua_rawseti(lL,top,toprawlen+1);
        buf=__lua_Alloc(NULL,buf,0,0);
        if (buf!=NULL) longjmp(callback_env,-101);
    }

}


static void aCommentCallBack(void *userData, const char *s){ 
    void** luserData=(void**) userData;
    lua_State* lL=(lua_State*) luserData[0];
    //lua_Alloc __lua_Alloc=(lua_Alloc) luserData[1];

    int i=0;
    int l=strlen(s);
    bool found=((int)s[i])>32;
    if ( !found ) {
        for (i=0;!found && i<l;i++) found=((int)s[i])>32;
        if (found) i-=1;
    }
    if (found) {
        //char* buf=NULL;
        //buf=__lua_Alloc(NULL,buf,0,l-i+1);
        //if (buf==NULL) longjmp(callback_env,-100);
        //strncpy(buf,&s[i],l-i);
        //buf[l-i+1]='\0';
        int top=lua_gettop(lL);
        int toprawlen=lua_rawlen(lL,top);
        lua_newtable(lL);
        lua_pushstring(lL,"__Comment__");
        lua_pushstring(lL,&s[i]);
        //lua_pushfstring(lL,"%s",buf);
        lua_settable(lL,-3);
        lua_rawseti(lL,top,toprawlen+1);
        //buf=__lua_Alloc(NULL,buf,0,0);
        //if (buf!=NULL) longjmp(callback_env,-101);
    }
    //if (found) printf("              CH%.*s\n",l,s); 
}


/***
  Use the expat library to parse an xml string, returning a lua object.
  @function xml_expat_parse
  @param the xml string to parse
  @param optional encoding string
  */


int xml_expat_parse(lua_State *L){

    const char *xml_string = luaL_checkstring(L,1);
    const int xml_string_len = strlen(xml_string);
    const char *enc = ( (lua_gettop(L)>2) ? luaL_checkstring(L,3) : "UTF-8" );
    if ( (lua_gettop(L)>1) && lua_istable(L,2) ) {
        if (lua_getfield(L,2,"__classname__")==LUA_TSTRING) {
            size_t bufl=0;
            const char* buf=lua_tolstring(L,-1,&bufl);
            if (bufl==3 && strncmp(buf,"XML",3)==0) {
                __XML_class__index=2;
            }
        }
    } 

    int lua_return_error_code(lua_State* lL, XML_Parser lParser, int lrc, const char* lmsg) {
        XML_ParserFree(lParser);
        lua_pushnil(lL);
        lua_pushnumber(lL,lrc);
        lua_pushstring(lL,lmsg);
        return 3;
    }

    int lua_return_code(lua_State* lL, XML_Parser lParser, int lrc, const char* lmsg) {
        XML_ParserFree(lParser);
        if (bHasAnyReturnValue) {
            //return value is already prepared, rotate rc below it
            lua_pushnumber(lL,lrc);
            lua_rotate(lL,-2,1);
            //lua_rotate(lL,lua_gettop(L)-1,1);
            lua_pushstring(lL,lmsg);
        } else {
            lua_newtable(lL);
            lua_pushnumber(lL,lrc);
            lua_pushstring(lL,lmsg);
        }
        return 3;
    }

    XML_Parser p = XML_ParserCreate(NULL);
    if (!p) return lua_return_error_code(L,p,-1,"Error xml_parse: could not allocate parser.");

    XML_SetEncoding(p,enc);

    void* userData[2]={(void*) L,(void*) lua_getallocf(L,NULL)};

    XML_SetUserData(p,userData);

    XML_SetElementHandler(p, aElementStartCallback, aElementEndCallBack);
    XML_SetCharacterDataHandler(p,(XML_CharacterDataHandler) aCharacterDataCallBack);
    XML_SetCommentHandler(p,(XML_CommentHandler) aCommentCallBack);

    /** from the expat looping example, not this case...
      for (;;) {
      int done;
      int len;

      len = (int)fread(Buff, 1, BUFFSIZE, stdin);
      if (ferror(stdin)) {
      fprintf(stderr, "Read error\n");
      exit(-1);
      }
      done = feof(stdin);

      if (XML_Parse(p, Buff, len, done) == XML_STATUS_ERROR) {
      fprintf(stderr,
      "Parse error at line %" XML_FMT_INT_MOD "u:\n%" XML_FMT_STR "\n",
      XML_GetCurrentLineNumber(p),
      XML_ErrorString(XML_GetErrorCode(p)));
      exit(-1);
      }

      if (done)
      break;
      }
      XML_ParserFree(p);
      */

    int done=0;

    StartingTop=lua_gettop(L);

    const XML_Char* tmp_attr_list[2]={NULL,NULL};
    //setting a document containing element
    aElementStartCallback(userData,"root",(const XML_Char**)(&tmp_attr_list));

    //lua_newtable(L);
    //lua_pushstring(L,"__QName__");
    //lua_pushstring(L,"root");
    //lua_settable(L,-3);
    //if (__XML_class__index>0) {
    //    lua_pushnil(lL);
    //    lua_copy(lL,__XML_class__index,lua_gettop(lL));
    //    lua_setmetatable(lL,-2);
    //}

    if (!setjmp(callback_env)) {
        if (XML_Parse(p, xml_string, xml_string_len, done) == XML_STATUS_ERROR) 
            return lua_return_error_code(L,p
                    ,(XML_GetCurrentLineNumber(p)*100+1)
                    ,XML_ErrorString(XML_GetErrorCode(p)));
    } else
        return lua_return_error_code(L, p, callback_env_rc, "Error xml_expat: longjmp error");

    return lua_return_code(L, p, 0, "Success");

}


int bIsTable(lua_State *L){
    bool rv=((lua_gettop(L)==1) && lua_istable(L,1));
    lua_pushboolean(L,rv ? 1 : 0);
    return 1;
}



//the registration function
int luaopen_WDS_Wranglers_xml_expat_base(lua_State *L) {
    //This pushes into the global space
    //lua_register(L,"xml_expat_base.parse",xml_expat_parse);
    //return 0;
    //This will return a table with named function elements
    lua_newtable(L);

    //Add one three line block for each cfunction to be returned
    lua_pushstring(L,"parse");
    lua_pushcfunction(L,xml_expat_parse);
    lua_settable(L,-3);

    lua_pushstring(L,"bIsTable");
    lua_pushcfunction(L,bIsTable);
    lua_settable(L,-3);

    return 1;
}


