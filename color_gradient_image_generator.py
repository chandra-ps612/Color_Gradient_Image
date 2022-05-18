# Reference: https://www.webucator.com/article/python-color-constants-module/
'''
Function np.tile() arranges the array vertically and horizontally.
Function np.linspace() generates 1D arrays that increase or decrease at regular intervals. Apart from it, 
it returns an equally spaced 1D array,given start_value, stop_value, and the number of samples i.e. num.
* It calculates intervals (steps) automatically.
'''

''' 
Modules:
Pillow==8.4.0
numpy==1.19.3
'''

from PIL import Image
import numpy as np

#Value of 2D ndarray changes in horizontal direction when is_horizontal is True
# .T create a transpose matrix for vertical orientation

def get_gradient_2d(start, stop, w, h, is_horizontal):
    if is_horizontal: 
        return np.tile(np.linspace(start, stop, w), (h, 1))
    else:
        return np.tile(np.linspace(start, stop, h), (w, 1)).T

'''
Expanding this to 3D ndarray. Set start, stop, and is_horizontal for each color in a list, and 
create a gradient image for each channel with the function for 2D ndarray.
'''

def get_gradient_3d(w, h, start_list, stop_list, is_horizontal_list):
    result = np.zeros((h, w, len(start_list)), dtype=np.float)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, w, h, is_horizontal)

    return result

array = get_gradient_3d(360, 360, (85,26,139), (144,238,144), (False, False, True))
img=Image.fromarray(np.uint8(array))
img=img.transpose(Image.ROTATE_90)
img.save('C:\\Users\\lav singh\\OneDrive\\Desktop\\Assignment_Quantic\\5.png', quality=95)
