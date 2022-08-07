#modified from the Vertica SDK examples

## Set an external credentials script (with permissions 0700)
VERTICA_USER_CREDENTIALS_SH?=~/vertica_user_credentials.sh

#example credentials file
# export VDSN=XXXXXX
# export VDatabase=XXXXXX
# export VServerName=XXXXXX
# export VBackupServerNode=XXXXXX
# export VUID=XXXXXX
# export VPassWD=XXXXXX
# export VPort=5433



## Path to vsql to avoid use of aliased versions
VSQL=/opt/vertica/bin/vsql

## Set to the location of the SDK installation
SDK_HOME?=/opt/vertica/sdk
SDK_JAR?=/opt/vertica/

LANGUAGE?=C++

CXX?=g++
CXXFLAGS:=$(CXXFLAGS) -I $(SDK_HOME)/include -I HelperLibraries -g -Wall -Wno-unused-value -shared -fPIC -std=gnu++11 -D_GLIBCXX_USE_CXX11_ABI=0
CXXFLAGS:=$(CXXFLAGS) -O3

## Set to the desired destination directory for .so output files
BUILD?=$(abspath build)

## Set to a valid temporary directory
BUILD_TMPDIR?=$(BUILD)/tmp

JAVA_HOME ?= /usr

JAVA_PATH := bin/java
JAVAC_PATH := bin/javac
JAR_PATH := bin/jar

JAVA ?= $(JAVA_HOME)/$(JAVA_PATH)
JAVAC ?= $(JAVA_HOME)/$(JAVAC_PATH)
JAR ?= $(JAVA_HOME)/$(JAR_PATH)


## this build is for a UDTF, parallel constructs will be used for other UDxs before a generalized format is ready.

lUDTF ?= $(notdir $(PWD))
lSchema ?= `grep Schema src/$(lUDTF)_spec.xml | sed -e 's/^.\+="//;s/".\+//'`

## The WDS-Vertica location
WDS_LOC:=../../..
WDS_CPP:=$(WDS_LOC)/WDS-Cpp
WDS_VERTICA:=$(WDS_LOC)/WDS-Vertica

CXXFLAGS:=$(CXXFLAGS) -I $(WDS_CPP)/include


BUILD_FINAL_SOURCES = $(BUILD)/tmp/$(lUDTF).cpp

all:	$(BUILD) $(BUILD_TMPDIR) $(BUILD)/$(lUDTF).so

dirs:	$(BUILD) $(BUILD_TMPDIR)

$(BUILD) $(BUILD_TMPDIR):	
	-- mkdir -p $@


$(lUDTF): $(BUILD) $(BUILD)/$(lUDTF).so

$(BUILD)/tmp/$(lUDTF).cpp:	$(BUILD)/tmp src/$(lUDTF)_spec.xml src/$(lUDTF)_guts.cpp $(WDS_VERTICA)/XSLT/UDTFSpec2Cpp.xsl
	xsltproc -o $(BUILD)/tmp/$(lUDTF).cpp $(WDS_VERTICA)/XSLT/UDTFSpec2Cpp.xsl src/$(lUDTF)_spec.xml

$(BUILD)/$(lUDTF).so: src/*.cpp $(BUILD_FINAL_SOURCES) $(SDK_HOME)/include/Vertica.cpp $(SDK_HOME)/include/BuildInfo.h 
	$(CXX) $(CXXFLAGS) -o $@ $(BUILD_FINAL_SOURCES) $(SDK_HOME)/include/Vertica.cpp 

$(BUILD)/uninstall_ddl.sql uninstall_ddl.sql:	$(BUILD) $(WDS_VERTICA)/XSLT/UDTFSpec2SQLCall.xsl FORCE
	xsltproc --stringparam language $(LANGUAGE) --stringparam runtemplate UDTF_SQLUnInstall --stringparam pathtobuild "$(BUILD)" -o $(BUILD)/uninstall_ddl.sql $(WDS_VERTICA)/XSLT/UDTFSpec2SQLCall.xsl src/$(lUDTF)_spec.xml

$(BUILD)/install_ddl.sql install_ddl.sql:	$(BUILD) $(WDS_VERTICA)/XSLT/UDTFSpec2SQLCall.xsl FORCE
	xsltproc --stringparam language $(LANGUAGE) --stringparam runtemplate UDTF_SQLInstall --stringparam pathtobuild "$(BUILD)" -o $(BUILD)/install_ddl.sql $(WDS_VERTICA)/XSLT/UDTFSpec2SQLCall.xsl src/$(lUDTF)_spec.xml

install:	$(BUILD)/uninstall_ddl.sql $(BUILD)/install_ddl.sql $(WDS_VERTICA)/XSLT/UDTFSpec2SQLCall.xsl
	. $(VERTICA_USER_CREDENTIALS_SH); $(VSQL) -h $${VServerName} -U $${VUID} -w $${VPassWD} -p $${VPort} -d $${VDatabase} -v ON_ERROR_STOP=on -f $(BUILD)/uninstall_ddl.sql
	. $(VERTICA_USER_CREDENTIALS_SH); $(VSQL) -h $${VServerName} -U $${VUID} -w $${VPassWD} -p $${VPort} -d $${VDatabase} -v ON_ERROR_STOP=on -f $(BUILD)/install_ddl.sql

uninstall:	$(BUILD)/uninstall_ddl.sql $(WDS_VERTICA)/XSLT/UDTFSpec2SQLCall.xsl
	. $(VERTICA_USER_CREDENTIALS_SH); $(VSQL) -h $${VServerName} -U $${VUID} -w $${VPassWD} -p $${VPort} -d $${VDatabase} -v ON_ERROR_STOP=on -f $(BUILD)/uninstall_ddl.sql

$(BUILD)/call.sql call.sql:	$(WDS_VERTICA)/XSLT/UDTFSpec2SQLCall.xsl src/$(lUDTF)_spec.xml FORCE
	xsltproc --stringparam runtemplate UDTF_SQLCall -o $(BUILD)/call.sql $(WDS_VERTICA)/XSLT/UDTFSpec2SQLCall.xsl src/$(lUDTF)_spec.xml

test:	$(BUILD)/call.sql
	for q in src/*test*.sql; \
		do \
		. $(VERTICA_USER_CREDENTIALS_SH); $(VSQL) -e -h $${VServerName} -U $${VUID} -w $${VPassWD} -p $${VPort} -d $${VDatabase} -v ON_ERROR_STOP=on -f $$q ; \
		done

clean:
	rm -rf $(BUILD)


FORCE:	



