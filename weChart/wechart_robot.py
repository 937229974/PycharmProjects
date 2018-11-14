#!/usr/bin/python
#coding=utf8
import itchat
import  time
import   requests
import   json
def  tulin_robot(text):
    url="http://www.tuling123.com/openapi/api"
    data={
        "key":"e4ad535f0eef4674a7b1ccd34643398b",
        "info":text,
        'userid': 'wechat-robot',
        'loc':"武汉"
    }
#!/usr/bin/python
#coding=utf8
import itchat
import  time
import   requests
import   json
def  tulin_robot(text):
    # if text == "101":
    #     return "wwww"
    url="http://www.tuling123.com/openapi/api"
    data={
        "key":"e4ad535f0eef4674a7b1ccd34643398b",
        "info":text,
        'userid': 'wechat-robot',
        'loc':"武汉"
    }
    r=requests.post(url,data=data).json()
    code=r["code"]
    """100000   文本类
       200000   链接类
       302000   新闻类
       308000   菜谱类
       313000   儿歌类
       314000   诗词类"""
    if  code==  302000:
        return  r["text"],r["list"]
    if code==  100000:
        return  r["text"]
    if   code==200000:
        return r["text"],r["url"]
    if   code==313000:
        return r["text"],r["function"]
    if   code==314000:
        return  r["text"],r["function"]
    if   code==308000:
        return r["text"],r["list"]
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    return  u"[主人暂时不在，我是他的助理小美]{}".format(tulin_robot(msg['Text']))
        # 回复给好友
if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run(debug=True)