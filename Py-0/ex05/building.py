import sys
import string

def print_res(s : str) -> None:
    
    digits = sum(c.isdigit() for c in s)
    upper_letters = sum(c.isupper() for c in s)
    lower_letters = sum(c.islower() for c in s)
    punctuation_marks = sum(c in string.punctuation for c in s)
    spaces = sum(c in " \n" for c in s)
    
    print("The text contains", len(s), "characters:")
    print(upper_letters , "upper letters")
    print(lower_letters , "lower letters")
    print(punctuation_marks , "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")

def main() -> int :
    
    if (len(sys.argv) > 2) :
        print("AssertionError: Need one arg")
        return(0)
    elif (len(sys.argv) == 1) :
        s = input("What is the text to count?\n") + "\n"
        print_res(s)
        return (1)
    s = sys.argv[1]
    print_res(s)
    return(1)

if (__name__ == "__main__") :
    sys.exit(main())