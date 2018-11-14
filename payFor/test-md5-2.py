import hashlib

#str = '152818734'
# {'authkey': '64d7de71a6', 'timestamp': '1528188559', 'mobile': '13834523621'}
# str ="138345236211528188559liweimin"
import time

mobile ="18635423536"
str_time = time.time()
str_time1 = str(str_time).split(".")
key = "liweimin"
auth_key = "%s%s%s"%(mobile,str_time1[0],key)
# 创建md5对象
print(str_time1[0])
hl = hashlib.md5()
hl.update(auth_key.encode(encoding='utf-8'))
print('MD5加密前为 ：' + auth_key)
print(hl.hexdigest())
print('MD5加密后为 ：' + hl.hexdigest()[5:15])