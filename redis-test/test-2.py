import redis
r = redis.Redis(host='localhost' , port='6379' , db=3 ,decode_responses=True,password='123456')
r.lpush("3",1)
r.lpush("3",2)
r.lpush("3",3)
r.lpush("3",4)
print(r.lrange("3" , 0 , -1)) #打印列表"3"的全部内容
r.lpop("3")
print(r.lrange("3" , 0 , -1))
