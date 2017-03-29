#!C:\Users\Jeff\AppData\Local\Programs\Python\Python35-32\python.exe

# Location on UCC Windows PC's - C:\Python34\python.exe

######## Location on my pc: C:\Users\Jeff\AppData\Local\Programs\Python\Python35-32\python.exe
######## Location on linux:   /usr/bin/env python3

from sys import argv

# Processes text line by line and prints any lines
# which match a specified pattern. 2 options are supported:
# '-v' indicates that an inverse matching will take place,
# where non-matching lines are printed. '-n' is the second
# supported command, where each matching line is prefixed
# with its line number.

lineNumber=0
numbering=False
inverse=False
string=''
listOfFiles=[]

if '-n' == argv[1]:
    numbering=True
    if '-v'== argv[2]:
        inverse=True
        string=argv[3]
        for arg in argv[4:]:
            listOfFiles.append(arg)
    else:        
        string=argv[2]
        for arg in argv[3:]:
            listOfFiles.append(arg)
elif '-v'== argv[1]:
    inverse=True
    if '-n' == argv[2]:
        numbering=True
        string=argv[3]
        for arg in argv[4:]:
            listOfFiles.append(arg)
    else:
        string=argv[2]
        for arg in argv[3:]:
            listOfFiles.append(arg)
else:
    string=argv[1]
    for arg in argv[2:]:
        listOfFiles.append(arg)
        
try:
    for file in listOfFiles:
        fileHandle=open(file, 'r')
        for line in fileHandle:
            lineNumber+=1
            if numbering and inverse:
                if string not in line:
                    print(lineNumber,':',line)
            elif numbering and not inverse:
                if string in line:
                    print(lineNumber,':',line)
            elif not numbering and inverse:
                if string not in line:
                    print(line)
            else:
                if string in line:
                    print(line)
except IOError:
    print('***Error in Grep: unable to open file: %s' % file)
