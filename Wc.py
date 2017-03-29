#!C:\Python34\python.exe
# Location on UCC Windows PC's

######## Location on my pc: C:\Users\Jeff\AppData\Local\Programs\Python\Python35-32\python.exe
######## Location on linux:   /usr/bin/env python3

from sys import argv

try:
    for arg in argv[1:]:

        fileName=arg
        # Displays information about the file 'fileName'.
        # Output will contain the number of lines, the
        # number of words, and the number of characters
        # listed in that order.
        fileHandle=open(fileName).read()
        characterCount=len(fileHandle)
        lineCount = len(fileHandle.splitlines())
        wordCount=0
        for line in fileHandle.splitlines():
            wordCount+=len(line.split())
        print('%5i %5i %5i' % (lineCount, wordCount, characterCount))
except IOError:
    print('***Error in Wc: unable to open file; %s' % arg)
