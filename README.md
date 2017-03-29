# Unix-Scripts-in-Python

This is my attempt to implement Python versions of a few Linux commands.
The output format of the Python version matches that of the Linux version. If a file does not exist or has incorrect permissions, then the Python version behaves just like the Linux version; apart from that, no further error-checking was done.

1. Wc.py
  Assumed that at least one filename argument is supplied, and output each number in a field of width 5.
2. Uniq.py
  Assumed that either one or two filename arguments are supplied.
3. Cat.py
  The options ‘-E’, ‘-n’, and ‘-s’ are be supported. Assumed that one or more filename arguments are supplied.
4. Tail.py
  The option ‘-n’ is be supported. Assumed that exactly one filename argument is supplied. 
5. Grep.py
  The options ‘-n’ and ‘-v’ are both be supported. Assumed that one or more filename arguments are supplied.
6. Factor.py
  Assumed that all the command-line arguments or terminal inputs are non-negative integers
