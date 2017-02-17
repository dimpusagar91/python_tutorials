#!/usr/bin/python

from url.lib.request import urlopen

print("US Naval observatory Master Clock time :")
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    #Decoding the binary data to text
    line = line.decode('utf-8')
    #look for Eastern time
    if 'EST' in line or 'EDT' in line:
        print(line)

 

