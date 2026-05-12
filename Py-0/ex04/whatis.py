import sys

if (len(sys.argv) > 2) :
    print("AssertionError: more than one argument is provided")
    sys.exit(1)
elif (len(sys.argv) < 2):
    print("AssertionError: less than one argument is provided")
    sys.exit(1)
s = sys.argv[1]
if (s[0] in "-+") :
    s = s[1:]
if (s.isdigit() is False) :
    print("AssertionError: argument is not an integer")
elif (int(s) % 2 == 0) :
    print("I'm Even.")
else :
    print("I'm Odd.")
