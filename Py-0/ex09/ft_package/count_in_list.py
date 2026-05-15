def count_in_list(lst : list, obj) -> int :
    return (sum(1 for c in lst if c == obj))    
    # count = 0
    # for c in lst :
    #     if (c == obj) :
    #         count += 1
    
    # return (count)
