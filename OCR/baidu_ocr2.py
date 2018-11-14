import requests
import json

#百度api  图片识别
def ocr_api(image_url):
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Accept':'*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Referer': 'http://ai.baidu.com/tech/ocr/webimage',
        'Cookie':'BAIDUID=370AF38E7427C681843F149494AF060B:FG=1; PSTM=1528362814; BIDUPSID=BACEFC98B946F48FA72A49C0FDDEBE97; BDUSS=paTDdUTTFkeWNycjJKaTBlVlpyWlFoMXJlR2RvNFZ6a1lZfmJCSmJXQ01kMXBiQUFBQUFBJCQAAAAAAAAAAAEAAAA2Dh1YRUFfTlVYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIzqMluM6jJbcn; docVersion=0; BDSFRCVID=JJAsJeC62ui8C_57-wQ6hBRZqesuoSRTH6aop4inACXZ6ifS7zhmEG0PDM8g0Ku-LKeRogKKy2OTH9jP; H_BDCLCKID_SF=tJPJVI82tCD3fP36qRbsMJ8thl63-4oX2TTKWjrJaDvPOMJRy4oTj6DDMbQvKbKfHR582nnPLfcaeJOuXT7-3MvB-fn-aJ3k3IcL-p7RfRbFEJ7oQft20M0EeMtjBbQaBGvILR7jWhvBhl72y5r805TXDNKqt58etn3Q0Rjebn7oD-8kbn5HK-LSMqO8etJya4o2WDvoLUJ5OR5Jj65TDlki5UPfe6c83IbGbfch5lvGO-J43MA--tR3DlQNe4kLbG7y-K-EQx7Ssq0x0MOWe-bQypoa5xbvJKOMahvXtq7xOKTF05CaeP_tqx5Ka43tHD7yWCkE-KJ5OR5JLn7nDn-9hMIfe6FjLNv3ohja-CbtbfbO-lnK-4TyyGCqJ68fJRPqV-t2-POqHtonMKIaj6vbqxby26n-Q2JeaJ5nJDohjDnJBT_bqjFyyx7GQqTD567tWMO4QpP-HJ7xj-r_LftRWGj0KqtfMDbLKl0MLpbYbb0xyn_VXMP80xnMBMn8teOnaIT_LIF-hDt6jj8-enO3Khb-5Rj22P_D_DPyHJOoDDv_yxQ5y4LdjG5ta6vmXbIfs43lJJnIVxclbJbhhptw3-Aq54RjJI5X5lO9yDQEex86247VQfbQ0-OuqP-jW5IL2pvHLJ7JOpvwDxnxy5Fq0a62btt_JnPH_CQP; Hm_lvt_fdad4351b2e90e0f489d7fbfc47c8acf=1530063720,1530063793,1530063978,1530071067; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; PSINO=1; seccode=fc4b186e650d26c86a684a0b61754fc6; Hm_lpvt_fdad4351b2e90e0f489d7fbfc47c8acf=1530083170'
    }
    url = 'http://ai.baidu.com/aidemo'
    dict ={'type': 'webimage',
           'image_url': image_url,
           }
    res = requests.post(url=url,data=dict,headers=headers)
    datas =json.loads(res.text)

    word_result= datas["data"]["words_result"]
    word_length = len(word_result)
    #借款金额  期数计算
    for i in range(0, word_length):
        word = str(word_result[i]["words"])
        if word == "已还总期数":
            qishu = str(word_result[i + 3]["words"])
            loan_money = word_result[i + 2]["words"]
            qs = int(qishu.split("/")[0])
            print("------------"+qishu)
            print("借款金额-----" + loan_money)

    loan_start_date =""
    loan_last_date  =""
    for i in range(0,word_length):
        word1 = str(word_result[i]["words"])
        print(word1)
        if word1 == "已还清":
            print("第一期期还款时间 =====" + word_result[i - 1]["words"])
            dateStr = word_result[i - 1]["words"]
            if dateStr.count(".") > 0:
                string , date = dateStr.split("日")
                loan_start_date, loan_last_date = get_date(date, qs)
            print("开始借款时间-----" + loan_start_date)
            print("最后一期还款时间------" + loan_last_date)

            return loan_money, loan_start_date, loan_last_date
#推算时间
def get_date(date,qs):
    year, month, day = date.split(".")
    month = int(month)
    start_month = month - 1
    back_month = month + qs -2
    if start_month == 0:
        year = int(year) - 1
        start_date = str(year) + "-12-" + str(day)
    elif start_month < 10:
        start_date = str(year) + "-0" + str(start_month) + "-" + str(day)
    else:
        start_date = str(year) + "-" + str(start_month) + "-" + str(day)
    if back_month >12 :
        year =int(year) +1
        new_month = back_month -13
        if new_month > 9:
            last_date =str(year) + "-" + str(new_month) + "-" + str(day)
        else:
            last_date = str(year) + "-0"  + str(new_month) + "-" + str(day)
    elif  back_month > 9:
        last_date = str(year) + "-" + str(back_month) + "-" + str(day)
    else:
        last_date = str(year) + "-0" + str(back_month) + "-" + str(day)
    return   start_date,last_date
image_url = 'http://123.dev.zhishensoft.com:58008/images/ppd/20180730/20180730142216.png'
ocr_api(image_url)