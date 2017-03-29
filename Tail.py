#!C:\Users\Jeff\AppData\Local\Programs\Python\Python35-32\python.exe

# Location on UCC Windows PC's - C:\Python34\python.exe

######## Location on my pc: C:\Users\Jeff\AppData\Local\Programs\Python\Python35-32\python.exe
######## Location on linux:   /usr/bin/env python3

from sys import argv

# Prints the last 10 lines of each file to standard output.
# If the argument -n is supplied, will print out the last k
# lines, where k is the number following -n. For example:
# 'Tail.py myfile.txt -n 100' will print the last 100 lines
# of the file myfile.txt. If "-n +K" is supplied, it will
# print out the lines starting with with the Kth.

kStart=False
kLegnth=0
kLines=0
diffNumLines=False
lineNumber=0
file = argv[1]
lineCount=0

for arg in argv[2:]:
    if '+' in arg:
        kStart=True
        kLegnth=int(arg.replace('+',''))
    if arg == "-n":
        diffNumLines=True
    if arg !="-n" and not '+' in arg:
        kLines=int(arg)
        
if len(argv)==2:
    try:
        fileHandle=open(file, 'r')
        lineCount = sum(1 for line in fileHandle)
        fileHandle=open(file, 'r')
        for line in fileHandle:
            lineNumber+=1
            if lineNumber>=lineCount-10:
                print(line)
    except IOError:
        print('***Error in Tail: unable to open file: %s' % file)
else:
    try:
        fileHandle=open(file, 'r')
        lineCount = sum(1 for line in fileHandle)
        fileHandle=open(file, 'r')
        for line in fileHandle:
            lineNumber+=1
            if not kStart and diffNumLines:
                if lineNumber>=lineCount-kLines:
                    print(line)
            if diffNumLines and kStart:
                if lineNumber>=kLegnth:
                    print(line)
    except IOError:
        print('***Error in Tail: unable to open file: %s' % file)





