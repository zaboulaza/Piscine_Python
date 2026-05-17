import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from zoom import ft_zoom

def load_img() :
    """Charge une image"""
    
    try :
        img = Image.open("animal.jpeg")
    except Exception as e :
        raise ValueError(f"Error {e}")
    
    array = np.array(img)
    
    print(f"The shape of image is: {array.shape}\n{array}")
    
    img = img.convert("L")
    array = np.array(img)
    
    array = ft_zoom(array)
    array_ = array
    array = array[:,:,np.newaxis]

    
    print(f"The shape of image is: {array.shape} or {array_.shape}\n{array}")
    
    plt.imshow(array, cmap='gray')
    plt.savefig("output.png")
    
    return

def main() -> int :
    load_img()
    
    return 1

if (__name__ == "__main__") :
    main()