import serial
from time import sleep
import cv2
import numpy as np
from LTcode_decoding import LTcode_decoding
from main2 import main2
from main_gray2 import main_gray2
COM_PORT = 'COM4'
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES)

signal=[0]*7
b = [1,1,1,-1,-1,1,-1]
data_length=35

receive_time = 0
pre_data = [0xff]*data_length
A = 0b000000000000000000
B = 0b0
C = 0b0000000000000000
file = open('test.txt','w')

def process_symbol(symbol):
    return str(symbol)
def barker_code_detect(vector):
    return np.correlate(b,vector, mode='valid')[0] == 7

def signal_received():
    signal_dict = {'0': -1, '1': 1}
    receive = ser.readline().decode('ISO-8859-1').strip()
    for i in range(6):
        signal[i] = signal[i+1]
    signal[6] = signal_dict.get(receive, 0)

    receive_data_detect_1 = barker_code_detect(signal)
    if receive_data_detect_1:
        for i in range(data_length):
            receive = ser.readline().decode('ISO-8859-1').strip()
            pre_data[i]= str(receive)
        for i in range(7):
            receive = ser.readline().decode('ISO-8859-1').strip()
            signal[i] = signal_dict.get(receive, 0)

        receive_data_detect_2=barker_code_detect(signal)
        if receive_data_detect_2:
            pre_data_str = ''.join(map(str, pre_data))  # 將 pre_data 轉換為字符串
            A = int(pre_data_str[:18], 2)
            B = int(pre_data_str[18:19], 2)
            C = int(pre_data_str[19:], 2)
            return A,B,C
    return 0,0,0


matrices1 = []
# while(1):

#     signal_received()
message_count = 0
################################
decode_threshold = 500
number = 29
#################################
end2=False
print("Start Receive")
while True:
    message_info = signal_received()
    #number+=1
    if message_info != (0, 0, 0):
        message_count += 1
        deg, symbols, seed = message_info
        print("Generated "+ str(message_count) +"th Message: deg={}, symbols={}, seed={}".format(deg, symbols, seed))
        matrices1.append([deg, symbols, seed])
        # message_count += 1
        # print(message_count)
        if message_count >= decode_threshold:
            if message_count%number==0:                   
                output_symbols = LTcode_decoding(matrices1)
                #print("Decoded Symbols:", output_symbols)
                end2 = all(x != 2 for x in output_symbols)
                output_symbols_count = sum(1 for x in output_symbols if x != 2)
                print("Total Decoded Symbols Count:", output_symbols_count)
        if end2:
            print("Receive Enough!")
            output_1 = ''.join(map(process_symbol, output_symbols))
            file.write(str(output_1))
            output = main_gray2(output_1)
            cv2.imwrite('test.jpg',output)
            file.close()
            # print(output_symbols)
            break
