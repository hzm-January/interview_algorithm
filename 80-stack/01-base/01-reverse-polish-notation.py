"""
    逆波兰表达式 <-> 中缀表达式
"""
import math
import operator


def infix_to_reverse_polish(expression):
    op = {
        '(': 2,
        ')': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    stack = []  # 存储运算符
    ans = []
    for c in expression:
        if c.isdigit():
            ans.append(c)
        else:
            while stack and op[c] < op[stack[-1]]:  # 当前运算符优先级小于栈顶，一直出栈
                top = stack.pop()
                if top == '(':  # 如果栈顶出栈的运算符是左括号，终止出栈
                    break
                ans.append(top)  # 出栈，并加入结果集
            if c != ')': stack.append(c)  # 除右括号不入栈，其他都入栈
    return ''.join(ans)


def reverse_polish_to_infix(expression):
    stack = []  # 存储数字，以及中间状态
    op = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': math.trunc,
    }
    for c in expression:
        if c in op:
            b, a = stack.pop(), stack.pop()
            stack.append('(' + a + c + b + ')')
        else:
            stack.append(c)
    return stack.pop()


if __name__ == '__main__':
    expression = '342*15-/+'
    print(reverse_polish_to_infix(expression))
    expression = '(3+((4*2)/(1-5)))'
    print(infix_to_reverse_polish(expression))
