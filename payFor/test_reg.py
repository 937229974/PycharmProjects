

#dc483e80a7a0bd9ef71d8cf973673924
#dc483e80a7a0bd9ef71d8cf973673924
#dc483e80a7a0bd9ef71d8cf973673924

import hashlib
import  requests
import  json

def test_post():
    hreader={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Referer": "http://channel.ymt.nongyaodai.com/",
        "Content-Type":"application/json;charset=UTF-8"
    }
    dict ='{\
        "accountNumber": "18435136815",\
        "chanelUrl": "http://channel.ymt.nongyaodai.com/#/ymt/guide?source=gnqb01",\
        "password": "dc483e80a7a0bd9ef71d8cf973673924",\
        "smsCode": "257086",\
        "source": "gnqb01",\
    }'
    url ="http://channel.ymt.nongyaodai.com/user/channel/register"
    h = requests.post(url=url,data=dict,headers=hreader)
    print(h.status_code)
    print(h.text)

def md5(password):
    hl = hashlib.md5()
    hl.update(password.encode(encoding='utf-8'))
    print('MD5加密前为 ：' + password)
    print('MD5加密后为 ：' + hl.hexdigest())
    return hl.hexdigest()

if __name__ =="__main__":
    test_post()