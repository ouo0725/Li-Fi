import numpy as np
import cv2

def split(matrix):
    #ycbcr = cv2.imread('lena_color_256.tif')
    n = matrix.shape[0]
    m = matrix.shape[1]

    # main : 
    # for i in range(#)
    #   split = np.reshape(ycbcr[:,:,i] , (32,32,8,8))
    matrix = np.reshape(matrix, (int(n/8)*int(m/8),8,8))
    return matrix