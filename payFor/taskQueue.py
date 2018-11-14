import heapq

import time


class PriorityQueue(object):
    def __init__(self):
        self._queue = []  # 创建一个空列表用于存放队列
        self._index = 0  # 指针用于记录push的次序

    def push(self, item, priority):
        """队列由（priority, index, item)形式的元祖构成"""
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # 返回拥有最高优先级的项


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item: {!r}'.format(self.name)
q = PriorityQueue()

def ppd():
    q.push(Item('foo'), 5)
    q.push(Item('bar'), 1)
    q.push(Item('spam'), 3)
    q.push(Item('grok'), 1)
def task():
    print(q.pop())
def run_q():
    ppd()
    task()
    while q.empty():
        time.sleep(2)
        q.push(Item('foo+z'), 5)
    run_q()
if __name__ == '__main__':
     run_q()

