import numpy as np
def inverse_RLC(RLC_matrix):
    AC_vector = []
    for item in RLC_matrix:
        if isinstance(item, int):  # 判斷是否為整數(int)
            AC_vector.append(item)
        elif isinstance(item,str):# 判斷是否為EOB(字串)
            break
        else:  # 若不是整數，則為陣列(array)
            count, num = item
            if count == 0:
                AC_vector.append(num)
            else:
                for j in range(count):
                    AC_vector.append(0)
                AC_vector.append(num)

    AC_vector_count = len(AC_vector)
    for k in range(63 - AC_vector_count):
        AC_vector.append(0)

    return AC_vector

def inverse_AC(AC_vector):
    N = 0 #矩陣的上三角判斷要做幾次運算的變數
    O = 0 #AC_vector從0讀取到64的變數
    P = 1
    M = 7 #矩陣的下三角判斷要做幾次運算的變數
    matrix = [[0 for _ in range(8)] for _ in range(8)]
    matrix[0][0]=AC_vector[0]
    for i in range(14):
        if N < 8:
            for j in range(N + 1):
                if i % 2 != 0:
                    
                    matrix[j][N - j ]=AC_vector[O]
                    O=O+1
                else: 
                                      
                    matrix[N - j ][j]=AC_vector[O]
                    O=O+1
            N= N+1            
        else:
            for j in range(M ):
                if i % 2 == 0:
                    matrix[ 7-j][P+j]=AC_vector[O]
                    O=O+1
                else:
                    matrix[P +j][7-j]=AC_vector[O]
                    O=O+1
            M = M -1
            P=P+1
            
    return matrix


