# -*-coding: utf-8 -*-
__auth__ = "wade"
__date__ = '2018/1/2 21:48'


class Node:
    def __init__(self, val = 0, pnext = None):
        self.val = val
        self._next = pnext

    def __repr__(self):
        # 用来定义Node的字符输出，print为输出data
        return str(self.val)


class LinkList(object):
    def __init__(self):
        self.length = 0
        self.head = Node()

    def clear_list(self):
        # 清空链表，就是将链表所有节点删除
        self.length = 0
        self.head = None

    def empty_list(self):
        # 判断链表是否为空
        return self.length == 0

    def list_length(self):
        # return 链表长度
        return self.length

    def search_element(self, node):
        # 检索元素是否在链表中
        item = None
        # 判断给定的node是否为node的类型，如果不是就转为node的类型
        if isinstance(node, Node):
            item = node
        else:
            item = Node(node)
        current_node = self.head
        while current_node._next:
            current_node = current_node._next
            print "----", current_node.val
            if current_node.val == item.val:
                return True
        return False

    def list_insert_head(self, node):
        # 在头节点后面插入一个节点
        item = None
        # 判断给定的node是否为node的类型，如果不是就转为node的类型
        if isinstance(node, Node):
            item = node
        else:
            item = Node(node)
        temp_node = self.head._next
        item._next = temp_node
        self.head._next = item
        self.length += 1

    def list_insert_tail(self, node):
        # 在尾节点后面插入一个节点
        item = None
        # 判断给定的node是否为node的类型，如果不是就转为node的类型
        if isinstance(node, Node):
            item = node
        else:
            item = Node(node)

        if not self.head:
            self.head._next = item
            self.length += 1
        else:
            temp_node = self.head
            while temp_node._next:
                # 找到最后一个节点
                temp_node = temp_node._next
            temp_node._next = item
            self.length += 1

    def list_insert(self, i, node):
        # 在第i个节点后面插入一个节点，i=0表示第一个节点
        item = None
        # 判断给定的node是否为node的类型，如果不是就转为node的类型
        if i > self.length-1:
            print "需要插入的节点索引超过了节点长度"
            return
        if isinstance(node, Node):
            item = node
        else:
            item = Node(node)
        current_node = self.head._next
        j = 0
        while current_node and j < i:
            j += 1
            current_node = current_node._next
        item._next = current_node._next
        current_node._next = item
        self.length += 1

    def list_delete(self, index):
        # 删除第i个节点, index=0表示第一个节点(非头结点)
        itme = Node()
        if self.empty_list():
            print "链表为空"
            return False
        if index < 0 or index >= self.length:
            print "索引超出最大长度"
            return False

        # pre_node为保存前导节点
        # current_node为保存当前节点
        # 当j与index相等时就
        # 相当于找到要删除的节点
        j = -1
        current_node = self.head
        pre_node = self.head
        while current_node._next and j < index:
            pre_node = current_node
            current_node = current_node._next
            j += 1
        if j == index:
            pre_node._next = current_node._next
            self.length -= 1

    def list_travel(self):
        if self.empty_list():
            print "Linked list is empty"
            return
        node = self.head
        print "Head -->", node.val
        while node._next:
            node = node._next
            print "-->", node.val
        print "--> None. Linked node finished"



if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node5 = Node(5)
    link = LinkList()
    link.list_insert_head(node1)
    link.list_insert_head(node2)
    link.list_insert_head(node3)
    link.list_insert_tail(node5)
    link.list_travel()
    link.list_delete(3)
    link.list_travel()