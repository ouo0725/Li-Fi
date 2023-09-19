import numpy as np
def IQ_C(Q_matrices):
    Q_table = np.array([[1,1,1,1,1,1,1,1],
[ 1,1,1,1,1,1,1,1],
[ 1,1,1,1,1,1,1,1],
[ 1,1,1,1,1,1,1,1],
[ 1,1,1,1,1,1,1,1],
[ 1,1,1,1,1,1,1,1],
[ 1,1,1,1,1,1,1,1],
[ 1,1,1,1,1,1,1,1]])
    dct_matrices = []
    for matrix in Q_matrices:
        dct_matrix = np.multiply(matrix, Q_table)
        dct_matrices.append(dct_matrix)
    return dct_matrices
