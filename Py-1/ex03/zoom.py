import numpy as np

def ft_zoom(array : np.ndarray) -> np.ndarray :
    
    # array = array[len(array[0])/2 - 200:len(array[0])/2 + 200, len(array[1])/2 - 200:len(array[1])/2 + 200]
    len_ = array.shape
    # len_x = len_[0] / 2 - 200
    # print (int(len_x))
    return array[int(len_[0]/2 - 200):int(len_[0]/2 + 200), int(len_[0]/2 - 200):int(len_[0]/2 + 200)]

#array[int(len_[0])/2 - 200:int(len_[0])/2 + 200, int(len_[0])/2 - 200:int(len_[0])/2 + 200 ]