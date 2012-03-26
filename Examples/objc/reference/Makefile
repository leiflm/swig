MAKEFILE_NAME = Makefile #necessary for GNUStep Makefiles
include $(OBJC_MAKEFILES)/common.make

TOP          = ../..
SWIG         = $(TOP)/../preinst-swig
INTERFACE    = example.i
LIBRARY_NAME = libexample

LIBRARY_NAME            = libexample
libexample_HEADER_FILES = example.h exampleWrapper.h exampleProxy.h
libexample_CC_FILES     = example.cxx
libexample_OBJCC_FILES  = exampleWrapper.mm
libexample_OBJC_FILES   = exampleProxy.m
libexample_OBJCCFLAGS  += -fobjc-exceptions

TOOL_NAME            = example
example_OBJC_FILES   = runme.m
example_TOOL_LIBS    = -lexample
example_LIB_DIRS     = -L./obj/

include $(OBJC_MAKEFILES)/library.make
include $(OBJC_MAKEFILES)/tool.make

check:: all

before-all:: $(INTERFACE)
	$(SWIG) -objc -c++ $(SWIGOPT) $(INTERFACE)

clean::
	rm -rf *Wrapper* *Proxy*
