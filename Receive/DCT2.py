import numpy as np

def idct(dct_matrix):
    matrix = np.zeros_like(dct_matrix, dtype=np.float64)
    
    for x in range(8):
        for y in range(8):
            dct_value = 0.0
            for u in range(8):
                for v in range(8):
                    C_u = np.sqrt(1/8) if u == 0 else np.sqrt(1/4)
                    C_v = np.sqrt(1/8) if v == 0 else np.sqrt(1/4)
                    dct_value += dct_matrix[u][ v] * np.cos((2*x+1)*u*np.pi / 16) * np.cos((2*y+1)*v*np.pi / 16) * C_u * C_v
            matrix[x, y] = dct_value

    matrix = np.round(matrix).astype(np.int64)

    return matrix
def batch_idct(dct_matrices):
    output_matrices=[]
    for matrix in dct_matrices:
        output_matrices.append(idct(matrix))
    return output_matrices
# """ dct_matrix1 = np.array([[185, -19, 14, -10, 22, -10, -14, -19],
#                        [21, -33, 28, -8, -10, 12, 14, 7],
#                        [-11, -24, -2, 6, -19, 3, -21, -1],
#                        [-8, -5, 14, -15, -9, -3, -3, 8],
#                        [-3, 10, 9, 2, -10, 19, 19, 15],
#                        [3, -3, -19, 7, 7, -4, 0, -7],
#                        [10, 2, -2, 5, 0, -7, -1, -2],
#                        [0, -8, -3, 1, 1, 4, -7, 0]]) """
# dct_matrix2 = np.array( [[[2528,    0,    0,    0,    0,    0,    0,    0],
#        [  12,    0,    0,    0,    0,    0,    0,    0],
#        [ -28,    0,   16,    0,    0,    0,    0,    0],
#        [ -28,    0,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0],
#        [  24,    0,    0,    0,    0,    0,    0,    0],
#        [  49,    0,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0]], 
# [[2528,  -11,   10,    0,    0,    0,    0,    0],
#        [-120,    0,    0,    0,    0,    0,    0,    0],
#        [ -42,   13,    0,    0,    0,    0,    0,    0],
#        [  14,    0,    0,    0,    0,    0,    0,    0],
#        [  18,    0,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0]],
# [[3024,   11,    0,    0,    0,    0,    0,    0],
#        [ 108,    0,    0,    0,    0,    0,    0,    0],
#        [ -28,  -13,    0,    0,    0,    0,    0,    0],
#        [   0,   17,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0]],
# [[2496,  -11,    0,    0,    0,    0,    0,    0],
#        [  24,    0,    0,    0,    0,    0,    0,    0],
#        [ -14,  -26,    0,    0,    0,    0,    0,    0],
#        [ -42,   17,    0,    0,    0,    0,    0,    0],
#        [ -18,    0,    0,    0,    0,    0,    0,    0],
#        [   0,   35,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0],
#        [   0,    0,    0,    0,    0,    0,    0,    0]]]


#                         )
# result = batch_idct(dct_matrix2)

# print("IDCT 結果:")
# for r in result:
#     print(r.astype(int))
