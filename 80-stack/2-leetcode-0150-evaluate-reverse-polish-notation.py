import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            r = s
            if s in ['+', '-', '*', '/']:
                b, a = stack.pop(), stack.pop()
                if s == '+':
                    r = a + b
                elif s == '-':
                    r = a - b
                elif s == '*':
                    r = a * b
                elif s == '/':
                    r = int(a / b)
            stack.append(int(r))
        return stack.pop()
    def evalRPN2(self, tokens: List[str]) -> int:
        stack = []
        op_fn = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b), # 需要注意 python 中负数除法的表现与题目不一致
        }
        for s in tokens:
            r = s
            if s in ['+', '-', '*', '/']:
                b,a = stack.pop(), stack.pop()
                r = op_fn[s](a, b)
            stack.append(int(r))
        return stack.pop()


if __name__ == '__main__':
    # tokens = ["2", "1", "+", "3", "*"]
    # tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens))
    print(Solution().evalRPN2(tokens))



