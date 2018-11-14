# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作

import hashlib
import json

import requests
import time

mobile ="13834523621"
#{'authkey': '64d7de71a6', 'timestamp': '1528188559', 'mobile': '13834523621'}#
str_time = "1528188559"
key = "liweimin"
auth_key = "%s%s%s"%(mobile,str_time,key)

hl = hashlib.md5()
hl.update(auth_key.encode(encoding='utf-8'))

dict = {
    'authkey': hl.hexdigest()[5:15],
    'mobile': mobile,
    'timestamp': str_time[0]
        }
print(dict)
url = 'http://serv.weidab.com/rest/helper/search'
html = requests.post(url, dict)
data_resp = json.loads(html.text)
print(data_resp)