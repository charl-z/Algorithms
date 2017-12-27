# -*- coding: utf-8 -*-
'''
enqueue(item)  入队，在队列尾部加入一个数据项，参数是数据项，无返回值。
dequeue()      删除队列头部的数据项，不需要参数，返回值是被删除的数据，队列本身有变化。
isEmpty()      检测队列是否为空。无参数，返回布尔值。
size()         返回队列数据项的数量。无参数，返回一个整数。
'''


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

# 利用队列判断字符串是否是回文
def is_palindrome(astring):
    # 判断是否是回文
    que = Queue()
    for i in astring:
        que.enqueue(i)
    revserse_astring = ''.join(que.queue)
    if revserse_astring == astring:
        return True
    else:
        return False

if __name__=="__main__":
    print is_palindrome("abccba")
    print is_palindrome("12345654123")