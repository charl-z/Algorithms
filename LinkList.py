# -*-coding: utf-8 -*-
__auth__ = "wade"
__date__ = '2018/1/2 21:48'


class Node:
    def __init__(self, val, pnext = None):
        self.val = val
        self._next = pnext

    def __repr__(self):
        # 用来定义Node的字符输出，print为输出data
        return str(self.val)


class LinkList(object):
    def __init__(self):
        self.length = 0

    def clear_list(self):
        # 清空链表，就是将链表所有节点删除
        pass

    def empty_list(self):
        # 判断链表是否为空
        pass

    def list_length(self):
        # return 链表长度
        pass

    def locate_element(self, node):
        # 获取node在第几个节点
        pass

    def prior_element(self, current_node, pre_node):
        # 获取当前结点的前一个节点
        pass

    def next_element(self, current_node, pre_node):
        # 获取当前节点的下一个节点
        pass

    def list_insert_head(self, node):
        # 在头节点后面插入一个节点
        pass

    def list_insert_tail(self, node):
        # 在尾节点后面插入一个节点
        pass

    def list_insert(self, i, node):
        # 在第i个节点后面插入一个节点
        pass

    def list_delete(self, i):
        # 删除第i个节点，并将删除的节点返回
        pass

    def list_travel(self):
        # 遍历全部节点数据
        pass

