#!/usr/bin/python
# import sysconfig module
#provide access to python's configuration information
import sysconfig

#returns an installation path corresponding to the path name
print("Path Name : ", sysconfig.get_path("stdlib"))
print()

#returns a string that identifies the current platform
print("Current Platform : ", sysconfig.get_platform())
print()

# returns the MAJOR.MINOR Python version number as a string
print("Python Version Number : ", sysconfig.get_python_version())
print()

#returns a tuple containing all schemes
print("Scheme Names : ", sysconfig.get_scheme_names())
print()


