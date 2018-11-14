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
    driver.get("http://www.1ppt.com/")
    # 'http://www.1ppt.com/moban/jianjie/',
    # 'http://www.1ppt.com/moban/shangwu/',


if __name__ =="__main__":
    # save_int()
    test()

    # print(s)
