def combine(n: int, k: int) -> list[list[int]]:
    res, ans = [], []

    def backtracking(cur):
        if len(res) == k:  # 终止条件
            tmp = res.copy()
            ans.append(tmp) # 收集结果
            return
        for i in range(cur, n + 1):
            res.append(i) # 节点处理
            backtracking(i + 1) # 递归 回溯 让下次递归知道从i+1开始找，因为该题是组合不是排列。
            res.pop() # 撤销节点处理
        return

    backtracking(1)
    return ans

def combine2(n: int, k: int) -> list[list[int]]:
    """
     剪枝
    :param n:
    :param k:
    :return:
    """
    res, ans = [], []

    def backtracking(cur):
        if len(res) == k:  # 终止条件
            tmp = res.copy()
            ans.append(tmp) # 收集结果
            return
        for i in range(cur, (n - (k-len(res)) + 1) + 1): # 剪枝，需要更换单层搜索的最大值为n-(k-path.size)+1
            res.append(i) # 节点处理
            backtracking(i + 1) # 递归 回溯 让下次递归知道从i+1开始找，因为该题是组合不是排列。
            res.pop() # 撤销节点处理
        return

    backtracking(1)
    return ans

if __name__ == '__main__':
    # ans = combine(4, 2)
    # ans = combine(1, 1)
    ans = combine2(1, 1)
    print(ans)
