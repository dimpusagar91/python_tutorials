#!/usr/bin/python

#import getopt module

import getopt

args = '-a -b -csample -d example a1 a2'.split()
print("args :", args)

optlist, args = getopt.getopt(args, 'abc:d:')
print("optlist :", optlist)

print("args :", args)

s = '--condition=sample --testing --output-file abc.def -x a1 a2'
args = s.split()
print("args :", args)

optlist, args = getopt.getopt(args , 'x', ['condition=','output-file=','testing'])

print("args  :", args)
