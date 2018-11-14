from requests import Request, Session

s = Session()


postdata = {
'callback':'jQuery172009809002760861385_1514005232994',
'req_time': '1514005243560',
'redirectURL':'http://www.10010.com',
'userName':'15691046772',
'password':'921017',
'pwdType':'01',
'productType':'01',
'redirectType':'01',
'rememberMe':'1',
'_':'1514005243561',
}
url = 'https://uac.10010.com/portal/Service/MallLogin'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
   'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.9',
}
req = Request('GET',  url,
    data=postdata,
    headers=headers
)
prepped = s.prepare_request(req)
resp = s.send(prepped
)
res = s.get('https://upay.10010.com/npfweb/NpfWeb/Mustpayment/getMustpayment?number=15691046772',headers=headers)
print(res.content)