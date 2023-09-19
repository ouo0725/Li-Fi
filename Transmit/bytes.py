import sys
import numpy as np
from main import main
from main_gray import main_gray
from test import main_test

def byte(input):
    input_len = len(input)
    anti_input = ''.join(reversed(input))       #反轉字串
    x = int(anti_input,2)                       #str轉int
    y = (2**8)-1                                #建立mask = 11111111
    
    output = bytearray()                        
    for i in range(int(np.ceil(input_len/8))):
        z = x & y                               #利用遮罩讀取末8位
        x = x >> 8                              #達成下個迴圈讀取接續8位
        output.append(z)                        #以bytearray(output的型態)儲存
    return output

if __name__ == '__main__':
    input = main_test()
    output = byte(input)
    print(sys.getsizeof(output))
