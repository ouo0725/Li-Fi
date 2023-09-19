import serial
from time import sleep, time
import sys
import numpy as np
from main_gray2 import main_gray2
from main2 import main2
import cv2

COM_PORT = 'COM4'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES, timeout=1)  # 設定timeout值

def main():
    a = input("Write anything to start :D\n")
    print("Start Receive")
    data = ''
    while True:
        start_time = time()
        while True:
            receive = ser.read().decode('ISO-8859-1').strip()
            if receive:
                print("Receiving")
                data += receive
                # print(receive)
                break  # 收到數據，跳出內部迴圈
            elif time() - start_time > 0.5:  # 設定等待時間
                data = data[1:-1]
                return data  # 超過等待時間，返回data

# print(main())
def receive_data(receive):
    # print(receive)
    file.write(receive)
if __name__ == '__main__':
    file = open("test.txt",mode='w')
    data = main()
    receive_data(data)
    file.close()
    output = main_gray2(data)
    cv2.imwrite('test.jpg',output)
