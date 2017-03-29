#!C:\Users\Jeff\AppData\Local\Programs\Python\Python35-32\python.exe

# Location on UCC Windows PC's - C:\Python34\python.exe

######## Location on my pc: C:\Users\Jeff\AppData\Local\Programs\Python\Python35-32\python.exe
######## Location on linux:   /usr/bin/env python3

from sys import argv

# Reads data from the file 'fileName' and prints the results
# Output will be the printed distinct lines
# The options ‘-E’, ‘-n’, and ‘-s’ are supported, where:
# -E Displays "$" at end of each line.
# -n Numbers all the output lines.
# -s Suppressed all repeated empty output lines.
# It is assumed that one or more filename arguments are supplied.

E=False
n=False
s=False
lineNumber=0
file = argv[1]

for arg in argv[2:]:
    if arg == "-E":
        E=True
    if arg == "-n":
        n=True
    if arg == "-s":
        s=True
try:
    fileHandle=open(file, 'r')
    for line in fileHandle:
        lineNumber+=1
        if s and line=='\n':
            continue
        if n:
            line = str(lineNumber)+': '+line
        if E:
            line=line.strip()+' $'
        print(line)
except IOError:
    print('***Error in Cat: unable to open file: %s' % file)

