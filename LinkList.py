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
        self.head = None

    def clear_list(self):
        # 清空链表，就是将链表所有节点删除
        pass

    def empty_list(self):
        # 判断链表是否为空
        return self.length == 0

    def list_length(self):
        # return 链表长度
        return self.length

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
        item = None
        # 判断给定的node是否为node的类型，如果不是就转为node的类型
        if isinstance(node, Node):
            item = node
        else:
            item = Node(node)

        if not self.head:
            self.head = item
            self.length += 1
        else:
            temp_node = self.head
            while temp_node._next:
                # 找到最后一个节点
                temp_node = temp_node._next
            temp_node._next = item
            self.length += 1





        pass

    def list_insert(self, i, node):
        # 在第i个节点后面插入一个节点
        pass

    def list_delete(self, index):
        # 删除第i个节点
          if self.empty_list():
            return False



    def list_travel(self):
        # 遍历全部节点数据
        pass

###########################################
    # 删除一个节点之后记得要把链表长度减一
    def delete(self, index):
        if self.isEmpty():
            print "this chain table is empty."
            return

        if index < 0 or index >= self.length:
            print 'error: out of index'
            return
        # 要注意删除第一个节点的情况
        # 如果有空的头节点就不用这样
        # 但是我不喜欢弄头节点
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        # prev为保存前导节点
        # node为保存当前节点
        # 当j与index相等时就
        # 相当于找到要删除的节点
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            prev._next = node._next
            self.length -= 1