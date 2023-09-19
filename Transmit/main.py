import numpy as np
import cv2
import sys
from Image import input
from YCbCr import YCbCr_trans
from Split import split
from DCT import dct
from Quantizatuon import Q
from Quantization_C import Q_C
from DPCM import diff
from DPCM import dpcm
from RLC import AC,RLC
from HuffmanDC import dc
from HuffmanAC import ac


def main():
    img_name = 'lena_color_256.tif'
    img = input(img_name)
    ycbcr = YCbCr_trans(img)
    #print(np.shape(ycbcr))
    output3 = ''
    for i in range(3):
        split_matrix = ycbcr[:,:,i]
        matrix = split(split_matrix)
        #print(matrix)
        matrices = []
        Q_matrices = []
        if i == 0:
            for j in range(1024):
                matrices = matrix[j]
                #print(matrices)
                dct_matrix = dct(matrices)
                #print(dct_matrix)
                Q_matrix = Q(dct_matrix)
                Q_matrices.append(Q_matrix)
            #print('第一迴圈')
        else:
            for j in range(1024):
                matrices = matrix[j]
                #print(matrices)
                dct_matrix = dct(matrices)
                #print(dct_matrix)
                Q_matrix = Q_C(dct_matrix)
                Q_matrices.append(Q_matrix)
            #print('第二迴圈')
        
        #print(Q_matrices)
        dpcm_matrices = dpcm(Q_matrices)
        #print(dpcm_matrices)
        output = []
        for j in range(1024):
            AC_vector = AC(dpcm_matrices[j])   
            RLC_matrix = RLC(AC_vector)   
            RLC_matrix.insert(0,int(dpcm_matrices[j][0,0]))
            dc_value = RLC_matrix[0]
            del RLC_matrix[0]
            ac_value = RLC_matrix
            dc_output = dc(dc_value)
            ac_output = ac(ac_value)
            dc_output = '' if dc_output == None else dc_output
            ac_output = '' if ac_output == None else ac_output
            #output = dc_output  + ac_output
            #yield output        #生成器儲存多筆資料輸出
            output.append(dc_output  + ac_output)
        output2 = ''
        for j in range(len(output)):
            output2 = output2 + output[j]
        output3 = output3 + output2
    return output3

if __name__ == '__main__':
    file = open('test.txt','w')
    output = main()
    print(len(output))
    file.write(output)
    file.close()
        


    
    
    

    
        



