def generateParenthesis(n: int) -> list[str]:  # 时间超限
    """
        错误代码  时间超限
    :param n:
    :return:
    """
    path, ans = [], []
    strs = ['('] * n + [')'] * n
    used = [0] * (n * 2)
    dic = {}

    def backstack():
        if len(path) == n * 2:
            tmp = path.copy()
            stack = []

            for t in tmp:
                if stack and t == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(t)

            if not stack:
                s = ''.join(tmp)
                if s not in dic:
                    # print(s)
                    dic[s] = 1
                    ans.append(s)
            return
        for i in range(len(strs)):
            if used[i]: continue
            path.append(strs[i])
            used[i] = 1
            backstack()
            used[i] = 0
            path.pop()

    backstack()
    return ans


def generateParenthesis2(n: int) -> list[str]:  # 时间超限
    path, ans, stack = [], [], []

    def backstack(left, right):
        if len(path) == n * 2:
            tmp = path.copy()
            ans.append(''.join(tmp))
            return
        if left < n:
            path.append('(')
            backstack(left + 1, right)
            path.pop()
        if right < left: # 注意这里是right<left，而不是right<n
            path.append(')')
            backstack(left, right + 1)
            path.pop()

    backstack(0,0)
    return ans


if __name__ == '__main__':
    # print(generateParenthesis(3))
    # print(generateParenthesis(1))
    print(generateParenthesis2(6))
