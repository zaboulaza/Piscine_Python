def give_bmi(height : list[int | float], weight : list[int | float]) -> list[int | float] :
    """Calcule le BMI de chaque individue."""
    
    if (len(height) != len(weight)) :
        raise ValueError("Error: list not the same length")
    for c in height + weight :
        if not isinstance(c, (int, float)):
            raise ValueError("Error: list not good type")
    bmi = []
    for c in range(len(height)) :
        bmi.append(weight[c] / (height[c] ** 2))
    
    return bmi

def apply_limit(bmi : list[int | float], limit: int) -> list[bool]:
    """Return si le BMI depasse la limite."""
    
    res = []
    for c in bmi :
        if not isinstance(c, (int, float)) :
            raise ValueError("Error: list not good type")
    for b in range(len(bmi)) :   
        if (bmi[b] < limit) :
            res.append(False)
        else :
            res.append(True)
    return res




def main() -> int : 
    
    print(give_bmi.__doc__)
    print(apply_limit.__doc__)
    
    return 1

if (__name__ == "__main__") :
    main()
