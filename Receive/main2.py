import numpy as np
import cv2
import sys
# from main import main
from HuffmanDC2 import dc2
from HuffmanAC2 import ac2
from RLC2 import inverse_RLC
from RLC2 import inverse_AC
from DPCM2 import Idiff
from Quantization2 import IQ
from Quantizatuon_C2 import IQ_C
from DCT2 import batch_idct
from Split2 import merge
from YCbCr2 import YCbCr_inverse



def main2(input):
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
    dct_matrices = IQ(modified_matrices[:1024])
    #print(dct_matrices)                                    #因編碼端進行四捨五入，解碼會有誤差
    dct_matrices2 = IQ_C(modified_matrices[1024:3072])
    dct_matrix = batch_idct(dct_matrices + dct_matrices2)   #[3072,8,8]
    #print(dct_matrix)
    img_merge = merge(dct_matrix)                           #[3,256,256]
    #print(img_merge)
    #print(np.shape(img_merge))
    Y,Cb,Cr = img_merge[0],img_merge[1],img_merge[2]
    #print(np.shape(Y))
    img_BGR = YCbCr_inverse(Y,Cb,Cr)
    #print(Cb)

    return img_BGR

if __name__ == '__main__':
    input = ''
    output = main2(input)
    cv2.imwrite('test3.jpg',output)




