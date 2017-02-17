import os, sys

# Assuming /tmp/foo.txt exists and has read/write permissions.

ret = os.access("C://python33", os.F_OK)
print ("F_OK - return value %s"% ret)

ret = os.access("C://python33", os.R_OK)
print ("R_OK - return value %s"% ret)

ret = os.access("C://python3", os.W_OK)
print ("W_OK - return value %s"% ret)

ret = os.access("C:\\python33", os.X_OK)
print ("X_OK - return value %s"% ret)
