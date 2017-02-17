#!/usr/bin/python

# Use Exceptions to handle uncommon cases
# Approach 1 :
# To avoid errors, you might be inclined to add extra checks to a program

def parse_header(line):
    fields = line.split(":")
    if len(fields) != 2:
        raise RuntimeError("Malformed header")
      header,value = fields
      return header.lower(), value.strip()
