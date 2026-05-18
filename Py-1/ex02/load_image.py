import numpy as np
from PIL import Image

def ft_load(path: str) -> np.array : 
    """charger une image et print son format"""
    
    try :
        img = Image.open(path)
    except Exception as e:
        raise ValueError(f"Error: {e}")
        
    if (img.format != "JPEG") :
        raise ValueError("Error: img dont have good format")

    
    array = np.array(img)
    
    print(f"The shape of image is: {array.shape}")
    
    return array

