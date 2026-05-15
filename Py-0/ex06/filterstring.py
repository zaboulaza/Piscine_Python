from ft_filter import ft_filter
import sys

def main() -> int :
    
    if (len(sys.argv) != 3) :
        print("AssertionError: the arguments are bad")
        return (0)
    elif (type(sys.argv[1]) is not (str) or not sys.argv[2].isdigit()) :
        print("AssertionError: the arguments are bad")
        return (0)
            
    str_list = sys.argv[1].split()
    print(ft_filter(lambda word: len(word) > int(sys.argv[2]), str_list))
    
    return 1


if (__name__ == "__main__") :
    sys.exit(main())

