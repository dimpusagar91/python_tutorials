#!/usr/bin/python

print("\nExample program\n")

#importing the path module
import pathlib

print("\nPure paths:\n")
#A generic class that represents the system's path flavour
print("Pure Path: ", pathlib.PurePath())

#However, in a Windows path, changing the local root doesn't discard the
#previous drive setting
print("\nPure Windows Path: ", pathlib.PureWindowsPath('C:/Windows','/Program Files'))

print("\nConcrete paths:\n")
#A subclass of PurePath, this class represents concrete paths of the system's path flavour
print("A subclass of PurePath: ", pathlib.Path('c:/Python33/Demo'))

#A subclass of Path and purewindowspath, this class represents
#concrete windows filesystem paths
print("A subclass of Path and PureWindowsPath: ", pathlib.WindowsPath('c:/Program files'))

      
      
