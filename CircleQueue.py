# -*-coding: utf-8 -*-
__auth__ = "wade"
__date__ = '2017/12/23 21:47'


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print self.name, " ", self.age


class CircleQueue:
    def __init__(self, queue_capacity):

        self.queue_len = 0
        self.queue_capacity = queue_capacity
        self.elems = [None] * queue_capacity
        self.head = 0
        self.tail = 0

    def clearQueue(self):
        # 清空队列
        self.head = 0
        self.tail = 0
        self.queue_len = 0

    def queue_empty(self):
        # 判断队列是否为空
        return self.queue_len == 0

    def queue_full(self):
        # 判断队列是为满
        return self.queue_len == self.queue_capacity

    def queue_len(self):
        # 求队列的长度
        return self.queue_len

    def en_queue(self, elem):
        # 新元素入队,入的是队列的尾部
        if self.queue_full():
            print "queue is full"
            return False
        self.elems[self.tail] = elem
        self.tail += 1
        self.tail = self.tail % self.queue_capacity  #
        self.queue_len += 1
        return True

    def delete_queue(self):
        # 首元素出
        if self.queue_empty():
            return False
        #elem = self.elems[self.head]
        self.elems[self.head] = None
        self.head += 1
        self.head = self.head % self.queue_capacity
        self.queue_len -= 1
        return True

    def queue_traverse(self):
        # 遍历队列中的元素
        print self.head, self.tail, self.queue_len
        for i in xrange(self.head, self.queue_len + self.head):
            print self.elems[i % self.queue_capacity]

if __name__ == "__main__":
    circle_queue = CircleQueue(4)
    circle_queue.en_queue(1)
    circle_queue.en_queue(2)
    circle_queue.en_queue(3)
    circle_queue.delete_queue()
    circle_queue.en_queue(4)
    circle_queue.en_queue(5)
    circle_queue.en_queue(6)
    circle_queue.delete_queue()
    circle_queue.queue_traverse()

