#encoding=utf8
import os
import urllib.request
import urllib
import socket
import requests
from bs4 import BeautifulSoup

class  IP(object):
    def auto_ip(self):
        User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
        header = {}
        header['User-Agent'] = User_Agent

        url = 'http://www.xicidaili.com/nn/1'
        html = requests.get(url, headers=header)
        soup = BeautifulSoup(html.content, "lxml")
        # req = urllib.request.Request(url,headers=header)
        # res = urllib.request.urlopen(req).read()
        # soup = BeautifulSoup(res,"lxml")
        ##
        ips = soup.findAll('tr')
        print(ips)
        if  not os.path.exists("F://ip"):
            os.mkdir("F://ip")
        f = open("F://ip//proxy","w")

        for x in range(1,len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]+"\n"

            # print tds[2].contents[0]+"\t"+tds[3].contents[0]
            f.write(ip_temp)
    def test_ip(self):
        # encoding=utf8

        socket.setdefaulttimeout(3)
        f = open("F://ip//proxy")
        lines = f.readlines()
        proxys = []
        for i in range(0, len(lines)):
            ip = lines[i].strip("\n").split("\t")
            proxy_host = "https://" + ip[0] + ":" + ip[1]
            proxy_temp = {"https": proxy_host}
            proxys.append(proxy_temp)
        url = "http://ip.chinaz.com/getip.aspx"
        for proxy in proxys:
            #urllib  代理 ip
            # try:
            #     proxy_handler = urllib.request.ProxyHandler(proxy)
            #     opener = urllib.request.build_opener(proxy_handler)
            #     r = opener.open(url)
            #     print(r.read().decode('utf8'))
            # except:
            #     print('当前代理ip异常')
            #requests 代理 ip
            url2  = 'https://www.toutiao.com/i6615814285832487438/'
            # proxies1 = {"http": "http://221.228.17.172:8181",}
            try:
                res = requests.get(url2, proxies=proxy)
                # print(res.text)
                print("请求成功====="+res)
            except:
                print('代理异常ip')
    def test2(self):
        url2 = 'https://www.houxue.com/error/forbidip.html'
        proxies1 = {"http": "http://221.228.17.172:8181", }
        try:
            res = requests.get(url2, proxies=proxies1)
            print(res.text)
        except:
            print('代理异常ip')
if  __name__ == "__main__":
    ip = IP()
    # ip.auto_ip()
    ip.test_ip()
    # ip.test2()