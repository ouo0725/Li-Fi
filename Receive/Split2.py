import numpy as np


def merge(dct_matrix):
    img_merge = []
    if np.shape(dct_matrix) == (1024,8,8):
        img_merge = np.reshape(dct_matrix,(256,256))
    else:
        for i in range(3):
            img_splitinto3 = dct_matrix[1024*i:1024*(i+1)]
            img_split = np.reshape(img_splitinto3,(256,256))
            img_merge.append(img_split)
    

    # img_merge = np.reshape(dct_matrix,(256,256,3))
    return img_merge