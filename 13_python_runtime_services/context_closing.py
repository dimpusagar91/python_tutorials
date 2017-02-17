#!/usr/bin/pyton

# import contextlib module - Utilities for with-statement contexts
from contextlib import closing

# import urllib.request module - Extensible library for opening URLS
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)

# returns a context manager that supresses any of the specified exceptions
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('somefile.tmp')
