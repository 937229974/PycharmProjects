import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='123456', db=1)
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline(transaction=True)

class redis_conn(object):
    #
    def __init__(self):
        self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379,password='123456', db=1)
        self.r = redis.Redis(connection_pool=self.pool)
        self.pipe = self.r.pipeline(transaction=True)
    def conn_redis2(self):
        # 通过管道取值 取出来是  字符 转换为str

        self.pipe.set('name', 'root')
        self.pipe.set('test', 'test')
        self.pipe.execute()

        self.pipe.get("name")
        self.pipe.get("test")
        v = self.pipe.execute()
        print(v)
        print('--------------')
        #第一种方式
        print(v[0].decode())
        #第二种方式
        values = str(v[0], encoding='utf-8')
        print(values)

    def get_conn(self):
        pipe.setex('test3', 'ssss', 5)
        vale1 = pipe.execute()
        pipe.get("test3")
        vale1 = pipe.execute()
        # vale1 = self.pipe.execute()
        print(vale1)
        # #字符转码
        # print(vale1[0].decode())
        #
        # #redids 设置
        # time.sleep(6)
        # print("------------")
        # self.pipe.get("test2")
        # v = self.pipe.execute()
        # print(v[0])

    def test_hash(self):
        #列表
        # self.pipe.set('test', '222')
        # self.pipe.hset("hash","2",'2')
        # self.pipe.execute()

        self.pipe.hmset("hash",{'k1':'v1', 'k2': 'v2'})
        self.pipe.execute()

    def test_lpush(self):
        self.pipe.lpush('list',2)
        self.pipe.lrange("list", 0, -1)
        v1 = self.pipe.execute()
        print(v1)
        time.sleep(5)

        self.pipe.lpop('list')
        self.pipe.lrange("list", 0, -1)
        v2 = self.pipe.execute()
        print(v2)





if __name__ =="__main__":
    conn = redis_conn()
    # conn.conn_redis2()
    # conn.get_conn()
    # conn.test_hash()
    # conn.test_lpush()
    # redis_conn.get_conn()