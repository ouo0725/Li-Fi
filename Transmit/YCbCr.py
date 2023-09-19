import numpy as np
import cv2

def YCbCr_trans(img) :
    #分離出B,G,R
    B,G,R = cv2.split(img)
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    Cb = -0.1687 * R - 0.3313 * G + 0.5 * B +128
    Cr = 0.5 * R -0.4187 * G - 0.0813 * B + 128
    

    YCbCr = cv2.merge([Y,Cb,Cr])
    #print(YCbCr)
    return YCbCr

if __name__ == '__main__':
    img = cv2.imread('lena_color_256.tif')

    if img is not None:
        test = YCbCr_trans(img)
        print(test)
    else:
        print(f"Failed to load the image from lena_color_256.tif. Make sure the file exists.")
    