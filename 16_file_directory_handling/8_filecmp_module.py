#!/usr/bin/python

print("\nExample program using filecmp module\n")

from filecmp import dircmp

# Construct a new directory comparision object
# to compare the directories left and right

dcmp = dircmp(r"C:\Python33",r"C:\Python27")

# This directory from left side of dircmp method
print("\nleft:",dcmp.left)



#Files and subdirectories in a directory from left side of dircmp method
print("\nleft list:", dcmp.left_list)

#The directory from right side of dircmp method
print("\nright:",dcmp.right)

 
#Files and subdirectories in a directory from right side of dircmp method
print("\right list:", dcmp.right_list)

#Files and subdirectories in both left and right
print("\nCommon:",dcmp.common)

#Files in both left and right
print("\nCommon files:", dcmp.common_files)

#files which are identical in both left and right, using the class's
# file comparision operator
print("\nsame_files", dcmp.same_files)

'''
#files which are in both lef and right, whose contents according
# to the class's file comparision operator
print("\ndiff_files", dcmp.diff_files)


def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print("diff_file %s found in %s and %s" %(name,dcmp.left,dcmp.right))

    for sub_dcmp in dmp.subdirs.values():
        print_diff_files(sub_dcmp)

print("\ndiff : ", print_diff_files(dcmp))

'''


