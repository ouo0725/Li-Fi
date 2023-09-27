import serial
from time import sleep, time
import sys
import numpy as np
import cv2


COM_PORT = 'COM4'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES, timeout=1)  # 設定timeout值

# def receive():
#     a = input("Write anything to start ")
#     print("Start Receive")
#     # receive_1 = ''
def receive():
    try:
     data=''
     num=0
     a = input("Write anything to start ")
     print("Start Receive")
     while True:
      start_time = time()
      while True:
        if ser.in_waiting:          # 若收到序列資料…
            receive = ser.readline().decode()  # 讀取一行   receive為str
            # print(receive)
           # data = data_raw.decode()   # 用預設的UTF-8解碼
            # print("Receiving")
            receive1=int(receive)
            if(num%2==1):
                element="1"
                for item in range(receive1):
                 data+=element
                 print("1")
            else:
                element="0"
                for item in range(receive1):
                 data+=element
                 print("0")
                #element = next(alternating_iterator)
                #element1=str(element)
                # for i in range(receive1):
                #  data+=element
            num=num+1

            # information = element*receive1
            # data+=information
            break
        elif time() - start_time > 3:  # 設定等待時間
                data = data[1:-1]
                return data  # 超過等待時間，返回data



    except KeyboardInterrupt:
     ser.close()    # 清除序列通訊物件
     print('再見！')


                # print("Receiving")
                # # 创建一个空的列表，用于存储数字
                # while(i<63940):
                #      data.append(receive)
                #      i=i+1
                #      data = ','.join(map(str, data))
# # 逐个添加数字到列表中
# numbers.append(1)
# numbers.append(10)  # 超过9的值
# numbers.append(3.5)  # 浮点数值
# # ... 可以继续添加更多数字

# # 使用逗号将数字连接成一个字符串
# result = ','.join(map(str, numbers))

# # 输出结果
# print(result)

                # receive_1 += receive
                # data = ','.join(receive_1)
                #print(receive)


#print(main())
# def receive_data(receive):
#     print(receive)
#     file.write(receive)
if __name__ == '__main__':
    file = open("C:/Users/88697/Desktop/test1.txt",mode='w')
    data = receive()
    print(data)
    file.write(data)
    # receive_data(data)
    print(len(data))
    file.close()
