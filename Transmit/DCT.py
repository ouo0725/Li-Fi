import numpy as np
import cv2

def dct(matrix):
    dct_matrix = np.zeros_like(matrix, dtype=np.float64)

    for u in range(8):
        for v in range(8):
            C_u=np.sqrt(1/8) if u==0 else np.sqrt(1/4)
            C_v=np.sqrt(1/8) if v==0 else np.sqrt(1/4)
            dct_value=0.0
            for x in range(8):
                for y in range(8):
                    dct_value += matrix[x][y] * np.cos((2*x+1)*u*np.pi / 16) * np.cos((2*y+1)*v*np.pi / 16)
                    
            dct_matrix[u][v] =dct_value*C_u*C_v
    
    dct_matrix[0, 0] =  matrix.sum()/8

    dct_matrix = np.round(dct_matrix).astype(np.int64)
    
    return dct_matrix







