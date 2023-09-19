DC_Huff = ['00', '010', '011', '100', '101', '110', '1110', '11110', '111110', '1111110', '11111110', '111111110' ]


def dc(dc_value):
    
    if dc_value == 0:               #差值為0只回傳前綴
        dc_pre = DC_Huff[0]
        return dc_pre
    elif dc_value == -1:
        dc_output = '010' + '0'
        return dc_output
    else:
        bit_len = len(format(abs(dc_value), 'b'))   #dc值轉換為binary後的長度
        dc_pre = DC_Huff[bit_len]                   #查表(用長度)
        if dc_value > 0:                            #dc值大於0直接回傳前綴加二進制轉換
            dc_output = dc_pre + format(dc_value, 'b')
            return dc_output                               
        else:
            binary = bin(abs(dc_value)^(2**(bit_len+1)-1))[-bit_len:]    #dc值為負要變號(XOR)
            dc_output = dc_pre + binary.zfill(bit_len)
            return dc_output                               
    
if __name__ == '__main__':
    dc_value = -33
    output = dc(dc_value)
    print(output)