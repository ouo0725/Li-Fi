DC_Huff = ['00', '010', '011', '100', '101', '110', '1110', '11110', '111110', '1111110', '11111110', '111111110' ]


def dc2(input):
    for i in DC_Huff:
        if input.startswith(i):
            input = input.removeprefix(i)
            idx = DC_Huff.index(i)
            #print(input)
            break
    # 有找到DC_Huff
    dc_binary = input[:idx]
    #print(dc_binary)
    #print(input[:10])
    if idx == 0:
        dc_d = [0]
        return input,dc_d
    elif dc_binary[0] == '0':
        input = input.removeprefix(dc_binary)
        dc_binary = bin(int(dc_binary, 2)^(2**(idx+1)-1))[-idx:]
        #print(dc_binary)
        dc_d = [-int(dc_binary,2)]

        return input,dc_d
    else:
        input = input.removeprefix(dc_binary)
        #print(dc_binary)
        dc_d = [int(dc_binary,2)]
        
        return input,dc_d
    

if __name__ == '__main__':
    input = '1110011110'
    output = dc2(input)
    print(output)