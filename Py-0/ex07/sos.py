import sys

NESTED_MORSE = {' ': ' ',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ',': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'}

def main() -> int :
    
    if (len(sys.argv) != 2) : 
        print("AssertionError: the arguments are bad")
    elif (not sys.argv[1].isalnum()) :
        print("AssertionError: the arguments are bad")
    sys.argv[1] = sys.argv[1].upper()
    print("".join([NESTED_MORSE[c] for c in sys.argv[1]]))
    return 1


if (__name__ == "__main__") :
    sys.exit(main())

