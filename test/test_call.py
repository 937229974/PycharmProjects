import serial
import time
import datetime

def sms(mobile):
    # ser=serial.Serial(port='COM4', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=2)
    # ser.write(str.encode('ATD%s;\n'%mobile))
    # time.sleep(10)
    # ser.write(b'ATH;\n')
    #
    #
    # flag = True
    # while flag:
    #     lines = ser.readlines()
    #     for line in lines:
    #         line1 =str(line, encoding='utf-8')
    #         print(line1)
    #         respones = 0
    #         if line1.count("NO ANSWER")>0:
    #             print("无应答--------1")
    #             respones = 1
    #         elif line1.count('BUSY')>0:
    #             print('忙碌----------2')
    #             respones = 2
    #         elif line1.count('+COLP:') or line1.count('OK'):
    #             print('打通电话-------------3')
    #             respones = 3
    #         elif line1.count('NO CARRIER')>0: #打不通
    #             print('空号----------4')
    #             respones = 4
    #         if respones != 0 :
    #             flag = False
    # print('----空号检测结果  %s-----------'%respones)
    #
    # ser.close()
    # return respones
    starttime = datetime.datetime.now()

    # lon
    time.sleep(10)
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)


if __name__ =="__main__":
    mobile= '13299043162'
    sms(mobile)
