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

    def peek(self):
        # 返回栈顶元素
        return self.elems[self.top - 1]

    def pop(self):
        # 元素出栈
        if self.stack_empty():
            return False
        self.top -= 1
        # elem = self.peek()
        self.elems.pop()
        # return elem

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


'''
十进制转二进制
'''
def decToban(num):
    stack = Stack(num)
    while num != 1:
        stack.push(num % 2)
        num = num / 2
    stack.push(num)
    result = ''
    while (not stack.stack_empty()) and stack.peek() != None:
        result += str(stack.peek())
        stack.pop()
    return result

'''
中缀表达式转换为后缀表达式
1）如果遇到数字，我们就直接将其输出。
2）如果遇到非数字时，若栈为空或者该符号为左括号或者栈顶元素为括号，直接入栈。
3）如果遇到一个右括号，持续出栈并输出符号，直到栈顶元素为左括号，然后将左括号出栈（注意，左括号只出栈，不输出），右括号不入栈
4）如果遇到运算符号且栈非空，查看栈顶元素，如果栈顶元素的运算优先级大于或者等于该运算符号，则持续出栈，直到栈顶元素优先级小于该运算符。最后将该元素入栈
5）如果我们读到了输入的末尾，则将栈中所有元素依次弹出。
'''
def infix_to_postfix(astring):
    symbol = ['(', '+', '-', '*', '/', ')']
    astring_len = len(astring)
    stack = Stack(astring_len)
    result = ''
    for i in astring:
        if i not in symbol:
            result += i
        if stack.stack_empty() or i == '(' or stack.peek() == '(':
            stack.push(i)
        if i == ')':
            while stack.peek() != '(':
                result += stack.peek()
                stack.pop()
            stack.pop()
        if i == '*' or i == '/':
            if not stack.stack_empty():
                result += stack.peek()
                stack.pop()


if __name__ == "__main__":
    exs = ['({([()])}){}', '{{[](}}', '({)[}]']
    for ex in exs:
        print check_parentheses(ex)


