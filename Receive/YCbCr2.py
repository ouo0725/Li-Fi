import numpy as np
import cv2

def YCbCr_inverse(Y,Cb,Cr) :

    R = Y + 1.402 * (Cr - 128)
    G = Y - 0.34414 * (Cb - 128) - 0.71414 * (Cr - 128)
    B = Y + 1.772 * (Cb - 128)

    BGR = cv2.merge([B,G,R])
    return BGR