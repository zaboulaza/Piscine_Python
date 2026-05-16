
def slice_me(family: list, start: int, end: int) -> list :
    """slice decoupe une liste"""
    if(not isinstance(family, (list))) :
        raise ValueError("Error: wrong argument")
    if not isinstance(start, int) or not isinstance(end, int) :
        raise ValueError("Error: wrong argument")
    
    lenght = len(family)
    widght = len(family[0])
    
    if (start > lenght or end > lenght) :
        raise ValueError("Error: argument not good")
    for c in range(len(family)) :
        if (widght != len(family[c])) :
            raise ValueError("Error: list not the same size")\

    res = family[start:end]
        
    print(f"My shape is : ({lenght}, {widght})")
    print(f"My new shape is : ({len(res)}, {len(res[0])})")
    return res

def main() -> int :
    
    
    return 1

if (__name__ == "__main__") :
    main()
