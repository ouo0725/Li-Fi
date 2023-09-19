from bytes import byte
import numpy as np
# from main import main

def byte2(in_bytes,input_len):                     #例：bytearray(b'\xd2\x18')     
    bits = []
    b_list = list(in_bytes)                        #bytearray轉list型態
    for i in range(int(np.ceil(input_len / 8 ))):
        for j in range(8):
            byte = b_list[i]
            bit = b_list[i] & 1         #從最末端讀取(encoding有對輸入做反轉)
            b_list[i] = byte >> 1       #位移，下一個迴圈接續讀取
            bits.append(bit)
    return(bits)                        #例：[0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0]

#可能會多出8個以內的0，可以判斷input長度來判斷結尾

if __name__ == '__main__':
    input = main()
    in_byte = byte(input)
    intput_len = len(input)
    bits = byte2(in_byte,intput_len)
    print(bits)
    

