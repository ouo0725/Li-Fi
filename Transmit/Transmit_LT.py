import serial
import math
import random
from time import sleep
import sys
import time
from LTcode_encode import lt_encoding
from main import main
from main_gray import main_gray
#######################
# k=6400
#######################
# COM_PORT = 'COM3'  
# BAUD_RATES = 115200
# ser = serial.Serial(COM_PORT, BAUD_RATES)
numbers = ''
# input_symbols = [random.randint(0, 1) for _ in range(k)]
number=0
seed = 0
file = open('test.txt','w')
sleep(1)
def to_binary(n, bits):
    return format(n, '0' + str(bits) + 'b')

def signal_transmitted(A,B,C):
    # data = '1110010'+'/'+to_binary(A,18)+'/'+to_binary(B,1)+'/'+to_binary(C,16)+'/'+'1110010'
    data = '1110010'+to_binary(A,18)+to_binary(B,1)+to_binary(C,16)+'1110010'
    #print(data)
    ser.write(data.encode())
    time.sleep(0.09)
print("Collecting Data")
output = main()
for item in output:
    numbers += item
file.write(numbers)
input_symbols = [int(char) for char in numbers]
file.close()
print("The Data Length is "+str(len(numbers)))
a=input("I'm Ready :D\nType Anything to Transmit\n")
while(1):
    seed = (number)% 65536
    number+=1
    deg, encoded_symbols, seed_value = lt_encoding(input_symbols, seed)
    print(deg,encoded_symbols,seed_value)
    signal_transmitted(deg, encoded_symbols, seed_value)