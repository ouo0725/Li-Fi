import numpy as np
import math

Q_table = np.array([[ 17,  18,  24,  47,  99,   99,  99,  99],
                    [ 18,  21,  26,  66,  99,   99,  99,  99],
                    [ 24,  26,  56,  99,  99,   99,  99,  99],
                    [ 47,  66,  99,  99,  99,   99,  99,  99],
                    [ 99,  99,  99,  99,  99,   99,  99,  99],
                    [ 99,  99,  99,  99,  99,   99,  99,  99],
                    [ 99,  99,  99,  99,  99,   99,  99, 99],
                    [ 99,  99,  99,  99,  99,   99,  99,  99]])
def Q_C(dct_matrix):
   
    Q_matrix=np.divide(dct_matrix,Q_table)
    Q_matrix = np.round(Q_matrix).astype(int)
    return Q_matrix