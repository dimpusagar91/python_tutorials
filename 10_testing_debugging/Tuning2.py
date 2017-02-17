#!/usr/bin/python

# Use Exceptions to handle uncommon cases
# Approach 2 :
# An alternative way to handle errors is to simply let the  program
# generate an exception and catch it

def parse_header(line):
    fields = line.split(":")
    try:
        header,value = fields
        return header.lower(), value.strip()
    except ValueError:
        raise RuntimeError("Malformed header")


# The second approach of code runs about 1 percent faster. Setting up a try catch block
# for code that normally doesn't raise an exceptions runs more quickly
# than executing an if statement    
        
