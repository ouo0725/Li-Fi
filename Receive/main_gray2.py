import numpy as np
import cv2
import sys
from HuffmanDC2 import dc2
from HuffmanAC2 import ac2
from RLC2 import inverse_RLC
from RLC2 import inverse_AC
from DPCM2 import Idiff
# from Quantization2 import IQ
from quantizatuon2 import IQ2
from DCT2 import batch_idct
from Split2 import merge
from YCbCr2 import YCbCr_inverse
# from main_gray import main_gray
# from test import main_gray_test



def main_gray2(input):
    matrices = []
    while input != '':
        input,dc_d = dc2(input)                 
        input,ac_d = ac2(input)
        RLC_matrix = dc_d + ac_d
        ac_vector = inverse_RLC(RLC_matrix)
        matrix = inverse_AC(ac_vector)
        matrices.append(matrix)
    #print(matrices)#DPCM後
    modified_matrices = Idiff(matrices)
    #print(modified_matrices)
    dct_matrices = IQ2(modified_matrices)
    #print(dct_matrices)                            #因編碼端進行四捨五入，解碼會有誤差
    dct_matrix = batch_idct(dct_matrices)           #[3072,8,8]
    #print(dct_matrix)
    img_merge = merge(dct_matrix)                   #[3,256,256]
    #print(img_merge)
    #print(np.shape(img_merge))
    Y = img_merge
    R,G,B = Y,Y,Y
    img_BGR = cv2.merge([B,G,R])
    return img_BGR

if __name__ == '__main__':
    input = ''
    # print(len(input))
    output = main_gray2(input)
    cv2.imwrite('test.jpg',output)