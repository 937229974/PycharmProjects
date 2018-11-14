# -*- coding:utf-8 -*-
import requests
from  lxml import html
import urllib.parse, urllib.request
import time
import json
import hashlib
import base64

new_href = 'https://m.biquga.com//0_30/18504690_2.html'
def main():
    f = open('F:/model/zs.wav', 'rb')  # 格式：wav/pcm  采样率：8k/16k  声道：单声道   位数:16
    file_content = f.read()
    base64_audio = base64.b64encode(file_content)

    text = "智深数据互联网应用系统解决方案提供商"
    body = urllib.parse.urlencode({'audio': base64_audio, 'text': text})

    url = 'http://api.xfyun.cn/v1/service/v1/ise'
    api_key = 'a2303cd2b2a5a432e04fa930ce690203'
    param = {"aue": "raw", "result_level": "simple", "language": "zh_cn", "category": "read_sentence"}

    x_appid = '5b7a7622'
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))

    x_time = int(int(round(time.time() * 1000)) / 1000)

    x_checksum_content = api_key + str(x_time) + str(x_param, 'utf-8')
    x_checksum = hashlib.md5(x_checksum_content.encode('utf-8')).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url=url, data=body.encode('utf-8'), headers=x_header, method='POST')

    result = urllib.request.urlopen(req)
    result = result.read().decode('utf-8')
    # print(result)
    score = result.find("total_score")
    result = result[score: (score + 20)]
    result = result.replace('\"', '')
    print(text)
    print(result)
    return
def test_txt():
    url = "https://m.biquga.com//0_30/18279620_2.html"
    repson = requests.get(new_href)
    htm = repson.text.encode('iso-8859-1')
    hh = str(htm).replace('\xa0'*8,'\n\n')
    #
    elements = html.fromstring(repson.content)
    # print(elements)
    ss = elements.xpath('//*[@id="nr1"]/text()')
    for s in ss:
        print(s)
    href = elements.xpath('//*[@id="pb_next"]/@href')
    print(href)
    news = "https://m.biquga.com/"+href[0]
    print(news)
    # # print(texts[0].text.replace('\xa0' * 8, '\n\n'))
    # print(ss)
    # page_req = requests.get(url)
    # html = page_req.text.encode('iso-8859-1')
    # bf = BeautifulSoup(html)
    # texts = bf.find_all('div', id='content')
    # print(texts[0].text.replace('\xa0' * 8, '\n\n'))


if __name__ == '__main__':
    # main()
    test_txt()