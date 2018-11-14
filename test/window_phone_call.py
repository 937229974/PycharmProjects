import serial
import time
class Ser(object):
    def __init__(self):
        # 打开端口
        self.ser = serial.Serial(port='COM4', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)

    # 发送指令的完整流程
    def send_cmd(self, cmd):
        self.ser.write(cmd)
        response = self.ser.readlines()
        time.sleep(10)
        self.ser.write(cmd)
        print(response)
        self.ser.close()
        return response
    # 转成16进制的函数

if  __name__ =="__main__":
    s= Ser()
    cmd =b'ATD13299043162;\n'
    result= s.send_cmd(cmd)
    print(result)
