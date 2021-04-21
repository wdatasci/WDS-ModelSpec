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

## The WDS-Vertica location
WDS_VERTICA:=$(PWD)/../..

BUILD_FINAL_SOURCES = $(BUILD)/tmp/$(lUDTF).cpp

all:	$(BUILD) $(BUILD_TMPDIR) $(lUDTF)


dirs:	$(BUILD) $(BUILD_TMPDIR)

$(BUILD) $(BUILD_TMPDIR):	
	-- mkdir -p $@

$(lUDTF): $(BUILD) $(BUILD)/$(lUDTF).so

$(BUILD)/tmp/$(lUDTF).cpp:	$(BUILD)/tmp src/$(lUDTF)_spec.xml src/$(lUDTF)_guts.cpp $(WDS_VERTICA)/XSLT/UDTFSpec2Cpp.xsl
	xsltproc -o $(BUILD)/tmp/$(lUDTF).cpp $(WDS_VERTICA)/XSLT/UDTFSpec2Cpp.xsl src/$(lUDTF)_spec.xml

$(BUILD)/$(lUDTF).so: src/*.cpp $(BUILD_FINAL_SOURCES) $(SDK_HOME)/include/Vertica.cpp $(SDK_HOME)/include/BuildInfo.h 
	$(CXX) $(CXXFLAGS) -o $@ $(BUILD_FINAL_SOURCES) $(SDK_HOME)/include/Vertica.cpp 


$(BUILD)/uninstall_ddl.sql:	$(BUILD) FORCE
	-- /bin/rm $(BUILD)/uninstall_ddl.sql
	echo "comment on transform function $(lUDTF)() is null;" > $(BUILD)/uninstall_ddl.sql
	echo "drop library if exists $(lUDTF) cascade;" >> $(BUILD)/uninstall_ddl.sql

$(BUILD)/install_ddl.sql:	$(BUILD) $(BUILD)/$(lUDTF).so src/comment.sql FORCE
	-- /bin/rm $(BUILD)/install_ddl.sql
	echo "comment on transform function $(lUDTF)() is null;" > $(BUILD)/uninstall_ddl.sql
	echo "drop library if exists $(lUDTF) cascade;" >> $(BUILD)/install_ddl.sql
	echo "\\set libfile '\\'$(BUILD)/$(lUDTF).so\\'';" >> $(BUILD)/install_ddl.sql
	echo "create library $(lUDTF) as :libfile;" >> $(BUILD)/install_ddl.sql
	echo "grant all on library $(lUDTF) to dbadmin;" >> $(BUILD)/install_ddl.sql
	echo "grant usage on library $(lUDTF) to public;" >> $(BUILD)/install_ddl.sql
	echo "create transform function $(lUDTF) as language 'C++' name '$(lUDTF)_Factory' library $(lUDTF) fenced;" >> $(BUILD)/install_ddl.sql
	echo "grant all extend on all functions in schema public to dbadmin;" >> $(BUILD)/install_ddl.sql
	echo "grant execute on all functions in schema public to public;" >> $(BUILD)/install_ddl.sql
	cat src/comment.sql >> $(BUILD)/install_ddl.sql


install:	$(BUILD)/install_ddl.sql
	. $(VERTICA_USER_CREDENTIALS_SH); $(VSQL) -h $${VServerName} -U $${VUID} -w $${VPassWD} -p $${VPort} -d $${VDatabase} -v ON_ERROR_STOP=on -f $(BUILD)/install_ddl.sql

uninstall:	$(BUILD)/uninstall_ddl.sql
	. $(VERTICA_USER_CREDENTIALS_SH); $(VSQL) -h $${VServerName} -U $${VUID} -w $${VPassWD} -p $${VPort} -d $${VDatabase} -v ON_ERROR_STOP=on -f $(BUILD)/uninstall_ddl.sql

test:	
	for q in src/*test*.sql; \
		do \
		. $(VERTICA_USER_CREDENTIALS_SH); $(VSQL) -e -h $${VServerName} -U $${VUID} -w $${VPassWD} -p $${VPort} -d $${VDatabase} -v ON_ERROR_STOP=on -f $$q ; \
		done

clean:
	rm -rf $(BUILD)


FORCE:	



