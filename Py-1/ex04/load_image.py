import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from rotate import rotate

def load_img() :
    
    try :
        img = Image.open("animal.jpeg")
    except Exception as e :
        raise ValueError(f"Error: {e}")
    
    img = img.convert("L")
    array = np.array(img)
    len_ = array.shape
    array = array[int(len_[0]/2 - 200):int(len_[0]/2 + 200), int(len_[0]/2 - 200):int(len_[0]/2 + 200)]    
    array_ = array
    array = array[:,:,np.newaxis]

    print(f"The shape of image is: {array.shape} or {array_.shape}\n{array}")
    
    array = rotate(array)
    
    # array = array[:,:,0]
    print(f"New shape after Transpose: {array.shape}")
    
    print(array)
    
    plt.imshow(array, cmap='gray')
    plt.savefig("image_final.png")
    
        
    return

def main() -> int :
    load_img()
    
    return 1

if (__name__ == "__main__") :
    main()

