import numpy as np

AC_vector = []

#Zig-Zag掃描
def AC(matrix):
    N = 0
    M = 7
    P = 1
    AC_vector = []
    for i in range(14):
        if N < 7:
            for j in range(N + 2):
                if i % 2 == 0:
                    num = matrix[j][N - j + 1]
                    AC_vector.append(int(num))
                else:
                    num = matrix[N - j + 1][j]
                    AC_vector.append(int(num))
            N= N+1            
        else:
            for j in range(M ):
                if i % 2 != 0:
                    num = matrix[ 7-j][P+j]
                    AC_vector.append(int(num))
                else:
                    num = matrix[P +j][7-j]
                    AC_vector.append(int(num))
            M = M -1
            P=P+1
    return AC_vector

#RLC
Q=0
def RLC(AC_vector):
    global Q
    RLC_matrix = []
    j = len(AC_vector) - 1
    eob = False
    zero_count = 0

    # 創建AC_vector的複製
    AC_vector_copy = AC_vector.copy()

    # 從AC_vector的尾端往前查找連續的零元素，並將它們從AC_vector_copy中移除
    while j >= 0:
        if AC_vector[j] == 0:
            zero_count += 1
            AC_vector_copy = np.delete(AC_vector_copy, j)
        else:
            eob = True
            break
        j -= 1

    # 根據RLC編碼處理AC_vector_copy中的非零元素
    for i in range(len(AC_vector_copy)):
        if Q < 15:
            if AC_vector_copy[i] != 0:
                num = AC_vector_copy[i]
                matrix = [Q, num]
                RLC_matrix.append(matrix)
                Q = -1
            Q += 1
        else:
            if Q == 15:
                RLC_matrix.append([15, 0])
                Q = -1
            Q += 1
    if eob==True:
        RLC_matrix.append("EOB")
    if zero_count == len(AC_vector):
        RLC_matrix = ["EOB"]

    return RLC_matrix




