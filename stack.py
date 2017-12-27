# -*-coding: utf-8 -*-
__auth__ = "wade"
__date__ = '2017/12/26 22:05'


class Stack:
    def __init__(self, size):
        self.size = size
        self.top = 0  # 栈顶
        self.elems = [None] * size

    def stack_empty(self):
        # 判断栈是否为空
        return self.top == 0

    def stack_full(self):
        return self.top == self.size

    def clear_stack(self):
        self.top = 0

    def push(self, elem):
        # 元素入栈
        if self.stack_full():
            return False
        self.elems[self.top] = elem
        # self.elems.append(elem)  # 在初始化的时候self.elems = [None] * size，相当于self.elems=[None, None, ...], append添加的元素都在None之后
        self.top += 1
        return True

    def pop(self):
        # 元素出栈
        if self.stack_empty():
            return False
        self.top -= 1
        self.elems.pop()

    def peek(self):
        # 返回栈顶元素
        return self.elems[self.top - 1]

    def stack_traverse(self):
        # 遍历栈中所有元素
        for i in xrange(self.top):
            print self.elems[i]

"""
括号匹配的检验:
假设一个算术表达式中可以包含三种括号：圆括号"(" 和")"，方括号"["和"]"和花括号"{"和"}"，且这三种括号可按任意的次序嵌套使用（如：…[…{…}…[…]…]…[…]…(…)…）。
编写判别给定表达式中所含括号是否正确配对出现的算法
"""
def check_parentheses(astr):
    astr_len = len(astr)
    stack = Stack(astr_len)
    adic = {'(':1, '[':2, '{':3, ')':6, ']':5, '}':4}
    for i in astr:
        if i=='(' or i=='[' or i=='{':  # if i in '([{'
            stack.push(adic[i])
        if i==')' or i==']' or i=='}':
            if stack.peek() + adic[i] == 7:
                stack.pop()
    if stack.stack_empty():
        return True
    return False



if __name__ == "__main__":
    exs = ['({([()])}){}', '{{[](}}', '({)[}]']
    for ex in exs:
        print check_parentheses(ex)