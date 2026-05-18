import numpy as np
from PIL import Image


def ft_load(path : str) :
    
    try :
        img = Image.open(path)    
    except Exception as e :
        raise ValueError(f"Error: {e}")
    
    array = np.array(img)
    
    print(f"The shape of images is: {array.shape}\n{array}")
    
    return array

def main() :
    ft_load("landscape.jpg")
    
    
if (__name__ == "__main__") :
    main()