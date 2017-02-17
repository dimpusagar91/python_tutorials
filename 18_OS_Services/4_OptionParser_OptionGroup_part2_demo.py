#!/usr/bin/python

from optparse import OptionParser, OptionGroup

#usually, a help option is added automaticaly, but that can
#be suppressed using the add_help_option argument

parser = OptionParser(add_help_option=False)

parser.add_option("-h","--help",action="help")
parser.add_option("-v",action="store_true", dest="verbose",
                  help="Be moderately verbose")
parser.add_option("--file",dest="filename",
                  help="Input file to read data from")
#parser.add_option("--secret", help=SUPPRESS_HELP)
parser.print_help()





 
