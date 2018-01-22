# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 18:18
# @Author  : wadedy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = 0  # 如果有仅为temp=1 否则为0
        current_node1 = l1
        current_node2 = l2
        self.headnode = ListNode(0)
        while (current_node1 and current_node2):
            current_sum = (current_node1.val + current_node2.val + temp) % 10
            if (current_node1.val + current_node2.val + + temp) > 9:
                temp = 1
            else:
                temp = 0
            self.tail_insert(current_sum)
            current_node1 = current_node1.next
            current_node2 = current_node2.next

        while current_node1:
            current_sum = (current_node1.val + temp) % 10
            self.tail_insert(current_sum)

            if (current_node1.val + temp) > 9:
                temp = 1
            else:
                temp = 0
            current_node1 = current_node1.next
        while current_node2:
            current_sum = (current_node2.val + temp) % 10
            self.tail_insert(current_sum)
            # temp = 0
            if (current_node2.val + temp) > 9:
                temp = 1
            else:
                temp = 0
            current_node2 = current_node2.next
        if temp:
            self.tail_insert(temp)

        return self.headnode.next  # 从头结点的下一个节点才算实际需要的链表

    def tail_insert(self, vlaue):
        item = ListNode(vlaue)
        current_node = self.headnode
        while current_node.next:
            current_node = current_node.next
        current_node.next = item