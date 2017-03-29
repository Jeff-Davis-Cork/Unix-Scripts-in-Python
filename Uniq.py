#!C:\Python34\python.exe

# Location on UCC Windows PC's

######## Location on my pc: C:\Users\Jeff\AppData\Local\Programs\Python\Python35-32\python.exe
######## Location on linux:   /usr/bin/env python3

from sys import argv

# Filters out repeated lines in the file 'fileName'.
# Output will be the printed distinct lines
try:
    for arg in argv[1:]:
        fileName=arg
        fileHandle=open(fileName).read()
        previousLine=None
        for line in fileHandle.splitlines():
            if line != previousLine:
                print(line)
            line = previousLine
except IOError:
    print('***Error in Wc: unable to open file; %s' % arg)
