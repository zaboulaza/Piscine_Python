def ft_filter(func, elem) :
    if (type(elem) is not list) :
        return []
    elif (func == None ) :
      return [c for c in elem if c]  
    return [c for c in elem if func(c)]

# def is_pair(n) -> bool :
#     return (n % 2 == 0)

# def main() -> int :
    
#     nb = [0, 1, 2, 3, 4, 5, 6]
#     print(ft_filter(is_pair, nb))
#     # print(ft_filter(None, nb))
#     return 1

# if (__name__ == "__main__") :
#     sys.exit(main())
    
