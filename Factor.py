#!C:\Users\Jeff\AppData\Local\Programs\Python\Python35-32\python.exe

# Location on UCC Windows PC's - C:\Python34\python.exe

######## Location on my pc: C:\Users\Jeff\AppData\Local\Programs\Python\Python35-32\python.exe
######## Location on linux:   /usr/bin/env python3

import sys

# Print the prime factors of all specified integer numbers.
# arguments can be file names containing numbers as well. 
# If no arguments are specified on the command line, a prompt
# will open for numbers or file names to be entered. if 'exit'
# in the windows command prompt or 'Ctrl-D' is entered, the
# program will end

number=0

for arg in sys.argv[1:]:
    try:
        file=arg
        fileHandle=open(file, 'r')
        for line in fileHandle:
            for num in line.split():
                try:
                    number=int(num)
                    if number<=0 or number==1:
                        print(number,': no prime factors.')
                    else:
                        factor=3
                        primFactors = []
                        while number % 2==0:
                            primFactors.append(2)
                            number/=2
                        while factor*factor<=number:
                            while number%factor==0:
                                primFactors.append(int(factor))
                                number/=factor
                            factor+=2
                        if number>1:
                            primFactors.append(int(number))
                        print(num,': Prime Factors=',primFactors)
                    sys.exit(0)
                except:
                    continue
    except:
        try:
            number=int(arg)
            if number<=0 or number==1:
                print(number,': no prime factors.')
            else:
                factor=3
                primFactors = []
                while number % 2==0:
                    primFactors.append(2)
                    number/=2
                while factor*factor<=number:
                    while number%factor==0:
                        primFactors.append(int(factor))
                        number/=factor
                    factor+=2
                if number>1:
                    primFactors.append(int(number))
                print(arg,': Prime Factors=',primFactors)
            sys.exit(0) 
        except ValueError:
            print('***Error in Factor: unable to open file: %s' % file)

if len(sys.argv)==1:
    while True:
        try:
            commands = input()
            # i had used sys.stdin.readline() here, but not sure if it is meant for shell or cmd line
            # this works in shell, where you can stop with a control-D, but not in cmd line.
            # input only looks for one line of input, not sure what david wants...
            #if commands:
            for arg in commands.split():
                try:
                    if arg=='exit' or arg=='^D':
                        sys.exit(0)
                    file=arg
                    fileHandle=open(file, 'r')
                    for line in fileHandle:
                        for num in line.split():
                            try:
                                number=int(num)
                                if number<=0 or number==1:
                                    print(number,': no prime factors.')
                                else:
                                    factor=3
                                    primFactors = []
                                    while number % 2==0:
                                        primFactors.append(2)
                                        number/=2
                                    while factor*factor<=number:
                                        while number%factor==0:
                                            primFactors.append(int(factor))
                                            number/=factor
                                        factor+=2
                                    if number>1:
                                        primFactors.append(int(number))
                                    print(num,': Prime Factors =',primFactors)
                            except:
                                continue
                except:
                    try:
                        if arg=='exit' or arg=='^D':
                            sys.exit(0)
                        number=int(arg)
                        if number<=0 or number==1:
                            print(number,': no prime factors.')
                        else:
                            factor=3
                            primFactors = []
                            while number % 2==0:
                                primFactors.append(2)
                                number/=2
                            while factor*factor<=number:
                                while number%factor==0:
                                    primFactors.append(int(factor))
                                    number/=factor
                                factor+=2
                            if number>1:
                                primFactors.append(int(number))
                            print(arg,': Prime Factors=',primFactors)
                    except ValueError:
                        print('***Error in Factor: unable to open file: %s' % file)
        except EOFError:
            sys.exit(0)
