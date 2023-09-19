import numpy as np

dpcm_vector=[]

def diff(Q_matrix, Q_matrix2):
    num = Q_matrix2[0][0] - Q_matrix[0][0]
    dpcm_vector.append(num)
    return dpcm_vector

# 示例矩陣
# Q_matrix1 = np.array([[10, 20, 30],
#                       [40, 50, 60]])

# Q_matrix2 = np.array([[7, 8, 9],
#                     [10, 11, 12]])

# Q_matrix3 = np.array([[53, 14, 15],
#                     [16, 17, 18]])

# Q_matrix4 = np.array([[19, 20, 21],
#                     [22, 23, 24]])

# Q_matrix5 = np.array([[29, 26, 27],
#                     [28, 29, 30]])

#將所有矩陣都存入matrices
#matrices = [Q_matrix1, Q_matrix2, Q_matrix3, Q_matrix4, Q_matrix5] 
def dpcm(matrices):
    # 使用迴圈計算差值並將結果存儲在 dpcm_vector 中
    dpcm_vector = []
    for i in range(len(matrices) - 1):
        num = matrices[i+1][0][0] - matrices[i][0][0]
        dpcm_vector.append(num)

    #print("差值向量：", dpcm_vector)


    # 使用迴圈逐一修改每個矩陣中的 [0][0] 元素
    for i in range(len(matrices) - 1):
        if i < len(dpcm_vector):
            matrices[i+1][0][0] = dpcm_vector[i]
            #print(dpcm_matrices[i+1][0][0])
    
    return(matrices)


if __name__ == '__main__':
    matrices = np.array([[[80,  0,  0,  0,  0,  0,  0,  0],        
       [ 1,  0,  0,  0,  0,  0,  0,  0],
       [-2,  0,  0,  0,  0,  0,  0,  0],
       [-2,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0],
       [ 1,  0,  0,  0,  0,  0,  0,  0],
       [ 1,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0]],[[ 88,  -1,   0,   0,   0,   0,   0,   0],
       [-10,   0,   0,   0,   0,   0,   0,   0],
       [ -3,   0,   0,   0,   0,   0,   0,   0],
       [  1,   0,   0,   0,   0,   0,   0,   0],
       [  1,   0,   0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0]],[[86,  1,  0,  0,  0,  0,  0,  0],
       [ 9,  0,  0,  0,  0,  0,  0,  0],
       [-2, -1,  0,  0,  0,  0,  0,  0],
       [ 0,  1,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0]],[[84, -1,  0,  0,  0,  0,  0,  0],        
       [ 2,  0,  0,  0,  0,  0,  0,  0],
       [-1, -2,  0,  0,  0,  0,  0,  0],
       [-3,  1,  0,  0,  0,  0,  0,  0],
       [-1,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  1,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0]],[[80,  0,  0,  0,  0,  0,  0,  0],        
       [ 1,  0,  0,  0,  0,  0,  0,  0],
       [-2,  0,  1,  0,  0,  0,  0,  0],
       [-2,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0],
       [ 1,  0,  0,  0,  0,  0,  0,  0],
       [ 1,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0]],[[ 88,  -1,   1,   0,   0,   0,   0,   0],
       [-10,   0,   0,   0,   0,   0,   0,   0],
       [ -3,   1,   0,   0,   0,   0,   0,   0],
       [  1,   0,   0,   0,   0,   0,   0,   0],
       [  1,   0,   0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0]],[[86,  1,  0,  0,  0,  0,  0,  0],
       [ 9,  0,  0,  0,  0,  0,  0,  0],
       [-2, -1,  0,  0,  0,  0,  0,  0],
       [ 0,  1,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0]],[[84, -1,  0,  0,  0,  0,  0,  0],        
       [ 2,  0,  0,  0,  0,  0,  0,  0],
       [-1, -2,  0,  0,  0,  0,  0,  0],
       [-3,  1,  0,  0,  0,  0,  0,  0],
       [-1,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  1,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0]]])
    Q_matrices = dpcm(matrices)
    print(Q_matrices)


