MAKEFILE_NAME = ../ObjC.mk #necessary for GNUStep Makefiles
include $(OBJC_MAKEFILES)/common.make

TOOL_NAME              = $(TARGET)
$(TARGET)_HEADER_FILES = *.h
$(TARGET)_C_FILES      = $(wildcard *.c)
$(TARGET)_CC_FILES     = $(wildcard *.cxx *.cpp)
$(TARGET)_OBJC_FILES   = ../$(TARGET)_runme.m $(wildcard *.m)
$(TARGET)_OBJCC_FILES  = $(wildcard *.mm)

include $(OBJC_MAKEFILES)/tool.make
