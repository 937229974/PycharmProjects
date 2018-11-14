# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import subprocess,os,sys,time
import threading, time, random,datetime
import  requests
import json
def test():



    i = datetime.datetime.now()
    print('%s'%i.hour)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    # return url,sta,z
    dict ={"physics_home": "E:/pics/images/ppd/20180524/20180524145703.png", "physics_details": "E:/pics/images/ppd/20180524/20180524145713.png", "url_details": "http://117.36.75.174:58008/images/20180524145713.png", "url_home": "http://117.36.75.174:58008/images/20180524145703.png"}
    print(dict.get('physics_home'))


def test_white():
    # uname = '13299043462'
    # status ='2'
    # dict={
    #     'mobile': uname,
    #     'status': status
    # }
    # resp = requests.post('http://117.34.95.108:7072/cms/v1/api/addWhiteCustomer',dict)
    # data = json.loads(resp.text)
    # print(data)
    # code = data.get('code')
    # print(code)
    # if code != '1':
    #     print("111")
    for i in range(0,11):
        print("111111111111")




    # url = "http://console.saas.zhishensoft.com/api/v2/OuputCusAction/ppd?sign=3ab7873060b6de9ca93b664e752bca6f"
    # s = requests.post(url, dict)


if __name__ == "__main__":
    # 连接的手机列表
    test_white()
    # url,sta,z = test()
    # print(url)
    # print(sta)
    # print(z)
