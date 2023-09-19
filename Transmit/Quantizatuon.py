import numpy as np
import math

Q_table = np.array(
[[40,28,25,40,60,100,128,153],
[30,30,35,48,65,145,150,138],
[35,33,40,60,100,143,173,140],
[35,43,55,73,128,218,200,155],
[45,55,93,140,170,273,258,193],
[60,88,138,160,203,260,283,230],
[123,160,195,218,258,303,300,253],
[180,230,238,245,280,250,258,248]]
)
def Q(dct_matrix):
   
    Q_matrix=np.divide(dct_matrix,Q_table)
    Q_matrix = np.round(Q_matrix).astype(int)
    return Q_matrix


