#modified from the Vertica SDK examples

## Set to the location of the SDK installation
SDK_HOME?=/opt/vertica/sdk
SDK_JAR?=/opt/vertica/

CXX?=g++
CXXFLAGS:=$(CXXFLAGS) -I $(SDK_HOME)/include -I HelperLibraries -g -Wall -Wno-unused-value -shared -fPIC -std=gnu++11
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


lUDTF ?= $(notdir $(PWD))

all:	$(BUILD) $(BUILD_TMPDIR) $(lUDTF)


dirs:	$(BUILD) $(BUILD_TMPDIR)

$(BUILD) $(BUILD_TMPDIR):	
	-- mkdir -p $@


$(lUDTF): $(BUILD) $(BUILD)/$(lUDTF).so

$(BUILD)/$(lUDTF).so: src/*.cpp $(SDK_HOME)/include/Vertica.cpp $(SDK_HOME)/include/BuildInfo.h 
	$(CXX) $(CXXFLAGS) -o $@ src/*.cpp $(SDK_HOME)/include/Vertica.cpp 


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
	echo "create transform function $(lUDTF) as language 'C++' name 'lUDTFFactory' library $(lUDTF) fenced;" >> $(BUILD)/install_ddl.sql
	cat src/comment.sql >> $(BUILD)/install_ddl.sql


install:	$(BUILD)/install_ddl.sql
	vsql -v ON_ERROR_STOP=on -w $(VPASSWORD) -f $(BUILD)/install_ddl.sql

uninstall:	$(BUILD)/uninstall_ddl.sql
	vsql -v ON_ERROR_STOP=on -w $(VPASSWORD) -f $(BUILD)/uninstall_ddl.sql

test:	
	for q in src/*test*.sql; \
		do \
		vsql -v ON_ERROR_STOP=on -w $(VPASSWORD) -f $$q ; \
		done

clean:
	rm -rf $(BUILD)


FORCE:	



