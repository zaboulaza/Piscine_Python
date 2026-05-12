import math

def NULL_not_found(object: any) -> int:
    if (object is None) :
        print("Nothing:",object ,type(object))
    elif (type(object) is (float)) :
        if (math.isnan(object)) :
            print("Cheese:",object ,type(object))
    elif (object == False and type(object) is bool) :
        print("Fake:",object ,type(object))
    elif (object == 0) :
        print("Zero:",object ,type(object))
    elif (object == "") :
        print("Empty:",object ,type(object))
    else :
        print("Type not Found")
        return (1)
    return 0