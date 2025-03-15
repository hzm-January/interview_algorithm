def combinationSum3(k: int, n: int) -> list[list[int]]:
    path, ans = [], []

    def backtracking(cur):
        if sum(path) == n and len(path) == k:
            tmp = path.copy()
            ans.append(tmp)
            return
        for i in range(cur, 10):  # 题目要求数字范围[1,9]
            path.append(i)
            backtracking(i + 1)
            path.pop()
        return

    backtracking(1)
    return ans


def combinationSum3_2(k: int, n: int) -> list[list[int]]:
    """
        写法优化
    :param k:
    :param n:
    :return:
    """
    path, ans = [], []

    def backtracking(cur, sum):
        if len(path) == k or sum > n:  # 元素个数够了就退出，剪枝1：sum>n退出
            if sum == n:
                tmp = path.copy()
                ans.append(tmp)
            return
        # 因为回溯初始从1开始，所以这里必须是n-(k-len(path))+1可以访问到
        for i in range(cur, 9 - (k - len(path)) + 1 + 1): # 剪枝2：单层搜索剪枝
            path.append(i)
            sum += i
            backtracking(i + 1, sum)
            path.pop()
            sum -= i
        return

    backtracking(1, 0)
    return ans

def combinationSum3_3(k: int, n: int) -> list[list[int]]:
    """
        写法优化
    :param k:
    :param n:
    :return:
    """
    path, ans = [], []

    def backtracking(cur, sum):
        if len(path) == k or sum > n:  # 元素个数够了就退出，剪枝1：sum>n退出
            if sum == n:
                tmp = path.copy()
                ans.append(tmp)
            return
        # 因为回溯初始从1开始，所以这里必须是n-(k-len(path))+1可以访问到
        for i in range(cur, 9 - (k - len(path)) + 1 + 1): # 剪枝2：单层搜索剪枝
            path.append(i)
            backtracking(i + 1, sum+i)
            path.pop()
        return

    backtracking(1, 0)
    return ans



if __name__ == '__main__':
    print(combinationSum3(3, 7))

    # print(combinationSum3(3, 9))
    # print(combinationSum3(4, 1))

    print(combinationSum3_2(3, 7))
