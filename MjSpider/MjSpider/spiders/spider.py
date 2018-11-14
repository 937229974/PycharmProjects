#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

import requests
import matplotlib.pyplot as plt


import scrapy
import time
from scrapy.selector import Selector
import matplotlib.image as mpimg
from scrapy.http import Request, FormRequest
from scrapy.spiders import CrawlSpider
import  ssl
ssl._create_default_https_context=ssl._create_unverified_context()#取消ssl 证书认证

#学信网数据爬取
class mj_spider(CrawlSpider) :
    name = "MjSpider"
    allowed_domains = ['afterloan.91naxia.com']
    #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数

    def start_requests(self):
        return [Request("http://afterloan.91naxia.com/afterloan/auth/login",meta={'cookiejar':1}, callback = self.post_login)]

    #FormRequeset出问题了
    def post_login(self, response):
       # print( response.body)
        Cookie1 = response.request.headers.getlist('Cookie')
        print('登录时携带请求的Cookies1：', Cookie1)
        #下面这句话用于抓取请求网页后返回网页中的lt字段的文字, 用于成功提交表单
        img =   'http://afterloan.91naxia.com'
        img += Selector(response).xpath('//*[@id="kaptchaImage"]/@src')[0].extract()
        print (img)
        with open('{}//{}.jpg'.format("F:\\pics", 'test'), 'wb') as f:
            req = requests.get(img)
            f.write(req.content)
        lena = mpimg.imread('F:\\pics\\test.jpg')
        plt.imshow(lena)  # 显示图片
        plt.axis('off')  # 不显示坐标轴
        plt.show()
        cord = input("请输入验证码：")


        return [FormRequest.from_response(response,
                            url='http://afterloan.91naxia.com/afterloan/auth/login',
                            meta={'cookiejar': response.meta['cookiejar']},
                            # headers = self.headers,  #注意此处的headers
                            formdata = {
                            'phone':'13817044255',
                            'password':'20170707',
                            'picCode':cord,
                            },
                            callback = self.after_login,
                            #dont_filter = True
                            )]

    def after_login(self, response) :
        #print(response.body)
        print("登录成功")     #
        Cookie2 = response.request.headers.getlist('Cookie')
        print('登录时携带请求的Cookies：', Cookie2)
        time.sleep(3)
        yield Request('http://afterloan.91naxia.com/afterloan/urgeRepayment/myConditionData?startPage=1&pageNum=10',
                      meta={'cookiejar':True,'dont_redirect': True,'handle_httpstatus_list': [302]},callback=self.parse_page)


    def parse_page(self, response):
        print(response.body )
        print(response)
        htx= Selector(response)
        ss= htx.xpath('//*[@id="content"]/div[2]/div[2]/div[1]/div/p/a[1]/text()').extract()
        print(ss)
        #/html/body/table/tbody/tr[2]/td[3]


    def parse(self, response):
        print(response.body.decode("utf-8") )
        sites = json.loads(response.body_as_unicode())
        print(sites)
        # print(response.body)
        # htc = Selector(response)
        # url = 'http://afterloan.91naxia.com'
        # for i in range(2,11):
        #           #//*[@id="common_list"]/table/tbody/tr[3]/td[14]/a[1]
        #     url2 = htc.xpath('//*[@id="common_list"]/table/tbody/tr[%d]/td[14]/a[1]/@href'% i).extract()
        #     print(url2)
            #http://afterloan.91naxia.com/afterloan/urgeRepayment/myConditionData?startPage=2&pageNum=10



