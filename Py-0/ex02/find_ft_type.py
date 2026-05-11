def all_thing_is_obj(object: any) -> int:

    if (type(object) not in (str, int)) :
        print(type(object).__name__.capitalize(), ':', type(object))
    elif (type(object) == str) :
        print(object, "is in the kitchen :", type(object))
    else :
        print("Type not found")
    return 42
