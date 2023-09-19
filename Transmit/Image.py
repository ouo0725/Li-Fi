import numpy as np
import cv2

def input(img_name): 
    img = cv2.imread(img_name)
    return img

#cv2.imwrite('image.png',img)

    cv2.waitKey(0)
    return img


    