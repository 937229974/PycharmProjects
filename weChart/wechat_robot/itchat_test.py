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
    if text == "101":
        return "有次老公开好房间等我 ，我到了门外想逗逗他，就在门外小声的叫：306，你叫的小姐来了，开门！谁料隔壁的门打开了，一个男的出来对我说：等会儿完事了到我这边来一下啊！"
    elif text == "102":
        return '''　男子去买车，需要10万元，可男子只带了现金99998元，就差2元钱！

　　               突然，他发现门口有一个乞丐，就过去对乞丐说：“求你了，给我2元钱吧，我要买车！”

　　                乞丐听后，大方地拿出4元钱递给男子，说：“帮我也买一辆。”'''
    elif text == "103":
        return "新闻"
    elif text == "104":
        return "图片"
    else:
        return "101 笑话             " \
               "102 故事             " \
               "103 新闻             " \
               "104 图片             "

# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    return  u"[主人暂时不在，我是他的助理小美]{}".format(tulin_robot(msg['Text']))
        # 回复给好友
if __name__ == '__main__':
    itchat.auto_login(hotReload=True)

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    print(myUserName)
    itchat.run(debug=True)