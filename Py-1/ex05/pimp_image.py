import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array: np.ndarray) :
    """Inverts the color of the image received."""
    
    # for i in range(len(array)) :
    #     for j in range(len(array[0])) :
    #         for k in range(3) :
    #             array[i][j][k] = 255 - array[i][j][k]
    
    res = array.copy()
    
    res = 255 - array
    
    plt.imshow(res)
    plt.savefig("Invert.png")
    
    return

def ft_red(array: np.ndarray) :

    res = array.copy()

    res[:, :, 1] = 0
    res[:, :, 2] = 0

    plt.imshow(res)
    plt.savefig("Red.png")

    return

def ft_green(array: np.ndarray) :
    
    res = array.copy()
    
    res[:, :, 0] = 0
    res[:, :, 2] = 0

    plt.imshow(res)
    plt.savefig("Green.png")

    return

def ft_blue(array: np.ndarray) :

    res = array.copy()
    
    res[:, :, 0] = 0
    res[:, :, 1] = 0
    
    plt.imshow(res)
    plt.savefig("Blue.png")

    return

def ft_grey(array: np.ndarray) :
    
    res = array.copy()

    grey = np.mean(res, axis=2).astype(np.uint8)
    res[:, :, 0] = grey
    res[:, :, 1] = grey
    res[:, :, 2] = grey
    
    plt.imshow(res)
    plt.savefig("Grey.png")

    return

