# -*- coding: UTF-8 -*-

import socket


class NetServer(object):
    def tcpServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('192.168.10.109', 6000))  # 绑定同一个域名下的所有机器
        sock.listen(5)

        while True:
            clientSock, (remoteHost, remotePort) = sock.accept()
            print("[%s:%s] connect" % (remoteHost, remotePort))  # 接收客户端的ip, port

            revcData = clientSock.recv(1024)
            # sendDataLen = clientSock.send("this is send  data from server")
            print(revcData)
            # "revcData: ", revcData
            # print
            # "sendDataLen: ", sendDataLen

            clientSock.close()


if __name__ == "__main__":
    netServer = NetServer()
    netServer.tcpServer()  