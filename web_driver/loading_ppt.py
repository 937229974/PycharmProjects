import os
import random
import uuid


import requests
from   selenium import webdriver
import time
def test():
    # url = "http://www.1ppt.com/"
    global  driver
    # driver = webdriver.Chrome(executable_path="D:\Python34\Scripts\phantomjs\\bin\phantomjs.exe")
    # driver = webdriver.PhantomJS(executable_path="D:\Python34\Scripts\phantomjs\\bin\phantomjs.exe")
    driver = webdriver.Chrome()
    # 'http://www.1ppt.com/moban/jianjie/',
    # 'http://www.1ppt.com/moban/shangwu/',

    list=[
    'http://www.1ppt.com/moban/aiqing/',
    'http://www.1ppt.com/moban/jianzhu/',
    'http://www.1ppt.com/moban/gudian/',
    'http://www.1ppt.com/moban/shishang/',
    'http://www.1ppt.com/moban/ziran/',
    'http://www.1ppt.com/moban/renwu/',
    'http://www.1ppt.com/moban/zhiwu/',
    'http://www.1ppt.com/moban/huanbao/',
    'http://www.1ppt.com/moban/liti/',
    'http://www.1ppt.com/moban/zhongguofeng/',
    'http://www.1ppt.com/moban/keji/',
    'http://www.1ppt.com/moban/jiaoyu/',
    'http://www.1ppt.com/moban/canyin/',
    'http://www.1ppt.com/moban/jingji/',
    'http://www.1ppt.com/moban/tiyu/',
    'http://www.1ppt.com/moban/dangzheng/',
    'http://www.1ppt.com/moban/junshi/',
    'http://www.1ppt.com/moban/lvyou/',
    'http://www.1ppt.com/moban/yixue/',
    'http://www.1ppt.com/moban/qiche/',
    'http://www.1ppt.com/moban/gongye/',
    'http://www.1ppt.com/moban/jixie/',
    'http://www.1ppt.com/moban/meirong/',
    'http://www.1ppt.com/moban/fangdichan/',
    'http://www.1ppt.com/xiazai/zongjie/',
    'http://www.1ppt.com/xiazai/huibao/',
    'http://www.1ppt.com/xiazai/jihua/',
    'http://www.1ppt.com/xiazai/rongzi/',
    'http://www.1ppt.com/xiazai/dabian/',
    'http://www.1ppt.com/xiazai/shuzhi/',
    'http://www.1ppt.com/xiazai/jianli/',
    'http://www.1ppt.com/xiazai/jieshao/',
    'http://www.1ppt.com/xiazai/gongsi/',
    'http://www.1ppt.com/xiazai/peixun/',
    'http://www.1ppt.com/xiazai/fenxi/',
    'http://www.1ppt.com/xiazai/kejian/',
    'http://www.1ppt.com/xiazai/donghua/',
    'http://www.1ppt.com/xiazai/huiben/',
    'http://www.1ppt.com/moban/xinnian/',
    'http://www.1ppt.com/moban/laodongjie/',
    'http://www.1ppt.com/moban/qingmingjie/',
    'http://www.1ppt.com/moban/jiandangjie/',
    'http://www.1ppt.com/moban/duanwujie/',
    'http://www.1ppt.com/moban/muqinjie/',
    'http://www.1ppt.com/moban/shengdanjie/',
    'http://www.1ppt.com/moban/qingrenjie/',
    'http://www.1ppt.com/moban/guoqingjie/',
    'http://www.1ppt.com/moban/zhongqiujie/',
    'http://www.1ppt.com/moban/ertongjie/',
    'http://www.1ppt.com/moban/jiaoshijie/',
    'http://www.1ppt.com/moban/ganenjie/',
    'http://www.1ppt.com/moban/funvjie/',
    'http://www.1ppt.com/moban/shengri/',
    'http://www.1ppt.com/xiazai/nianhui/',
    'http://www.1ppt.com/moban/qita/',
    'http://www.1ppt.com/beijing/jianjie/',
    'http://www.1ppt.com/beijing/danya/',
    'http://www.1ppt.com/beijing/shangwu/',
    'http://www.1ppt.com/beijing/yishu/',
    'http://www.1ppt.com/beijing/keji/',
    'http://www.1ppt.com/beijing/ziran/',
    'http://www.1ppt.com/beijing/dongwu/',
    'http://www.1ppt.com/beijing/zhiwu/',
    'http://www.1ppt.com/beijing/katong/',
    'http://www.1ppt.com/beijing/aiqing/',
    'http://www.1ppt.com/beijing/chouxiang/',
    'http://www.1ppt.com/beijing/biankuang/',
    'http://www.1ppt.com/beijing/xiexie/',
    'http://www.1ppt.com/beijing/zhongguofeng/',
    'http://www.1ppt.com/kejian/yuwen/',
    'http://www.1ppt.com/kejian/shuxue/',
    'http://www.1ppt.com/kejian/yingyu/',
    'http://www.1ppt.com/kejian/kexue/',
    'http://www.1ppt.com/kejian/shenghuo/',
    'http://www.1ppt.com/kejian/shehui/',
    'http://www.1ppt.com/kejian/pinde/',
    'http://www.1ppt.com/kejian/wuli/',
    'http://www.1ppt.com/kejian/huaxue/',
    'http://www.1ppt.com/kejian/dili/',
    'http://www.1ppt.com/kejian/lishi/',
    'http://www.1ppt.com/kejian/shengwu/',
    'http://www.1ppt.com/kejian/meishu/',
    'http://www.1ppt.com/kejian/youer/'  ]
    for href in list:
        num = 0
        read_html(href,num)
        # global  num


def read_html(href,num):
    driver.get(href)

    #/html/body/div[5]/dl/dt/span/a[3]
    # type = driver.find_element_by_xpath('//dl[class="dlbox"]/dt/span/a[3]').text
    type = driver.find_element_by_css_selector('body > div:nth-child(5) > dl > dt > span > a:nth-child(3)').text
    path = "E:/ppt/"+type+"/"
    if not os.path.exists(path):
        os.makedirs(path)

    # tag_a = driver.find_elements_by_xpath('/html/body/div[5]/dl/dd/ul/li/a')

    for i in range(1,21):
        print("打开子页面")#            /html/body/div[5]/dl/dd/ul/li[1]/h2/a
                                      #/html/body/div[5]/dl/dd/ul/li[5]/a/img
        try:
            driver.find_element_by_xpath('/html/body/div[5]/dl/dd/ul/li[%s]/a/img'%str(i)).click()
            zipName = driver.find_element_by_xpath('/html/body/div[5]/dl/dd/ul/li[%s]/h2/a'%str(i)).text


            now_handle=driver.current_window_handle
            handles = driver.window_handles
            driver.switch_to_window(handles[-1])
            time.sleep(3)

            driver.find_element_by_xpath('/html/body/div[6]/div[1]/dl/dd/div[1]/div[1]/ul/li[8]/a[2]').click()
            #操作新窗口
            time.sleep(3)
            href = driver.find_element_by_xpath('/html/body/div[6]/div[1]/dl/dd/ul[1]/li/a').get_attribute('href')
            print('============='+href)
            # href = driver.find_element_by_xpath('.//ul[class="downurllist"]/li/a').get_attribute('href')
            r = requests.get(href)
            time.gmtime()
            # mkName = uuid.uuid4()
            ran = random.randint(100000, 999999)
            with open(path+str(ran)+zipName+".zip",'wb') as  f:
                f.write(r.content)
            print(path+str(ran)+zipName+".zip---下载完成。。。")
            driver.close()
            driver.switch_to_window(now_handle)
            time.sleep(1)
        except:
            continue
    #翻页保存：
    if num == 0:
        pn = 15
    else:
        pn = 16                                #/html/body/div[5]/dl/dd/div/ul/li[15]/a
    try:                                              #/html/body/div[5]/dl/dd/div/ul/li[16]/a
        button_next =driver.find_element_by_xpath("/html/body/div[5]/dl/dd/div/ul/li[%s]/a"%str(pn)).text
        # button_next = tag.text()
        print(button_next)
        if button_next == "下一页":

            next_href = driver.find_element_by_xpath("/html/body/div[5]/dl/dd/div/ul/li[%s]/a"%str(pn)).get_attribute("href")
            print("正在翻页----"+next_href)
            num += 1
            read_html(next_href,num)
    except:
        pass
def save_int():
    driver = webdriver.Chrome()
    url="https://www.jdfcloud.com/"
    # s = requests.get(url)
    # print(s.text)
    driver.get(url)
    s = driver.page_source
    print(s)
if __name__ =="__main__":
    # save_int()
    test()

    # print(s)
