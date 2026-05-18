import numpy as np

def rotate(array: np.ndarray) -> np.ndarray :
    
    res = np.zeros((400, 400), dtype=array.dtype)
    array = array[:,:,0] 
        
    for i in range(400):
        for j in range(400):
            res[j][i] = array[i][j]   
    # i = 0
    # j = 0
    # while i < 400 :
    #     j = 0
    #     while j < 400 :
    #         res[j][i] = array[i][j]
    #         j += 1
    #     i += 1    
        
    res = res[::-1]
    return res