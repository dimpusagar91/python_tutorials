#!/usr/bin/python

#import sys module - system specific parameters and functions
import sys

#displays a list of strings that specifies the search path for modules
print("Sys path : ", sys.path)
print()

#displays string contains a platform identifier that can be used to append
#platform-specific components to sys.path for instance
print("Sys platform : ", sys.platform)
print()

#a tuple containing the five components of the versionnumber
print("Version number : ", sys.version_info)


#the C API version for this interpreter
print("Sys API Version : ", sys.api_version )

# displays a struct sequence giving parametres of the numeric hash implementation
print("Sys Hash Info : ", sys.hash_info)


#returns the name of the encoding used to convert Unicode filenames into
# system filenames

print("Get file system Encoding : ", sys.getfilesystemencoding())
print()
