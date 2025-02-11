def partition(s: str) -> list[list[str]]:
    """ 使用组合思想 切割 """
    path, ans = [], []

    def ispalindrome(subs: str) -> bool:
        p, q = 0, len(subs) - 1
        while p < q:
            if subs[p] != subs[q]:
                return False
            else:
                p += 1
                q -= 1
        return True

    def backtrack(cur):  # 1 参数列表 与 返回值
        if cur >= len(s):  # 2 终止条件
            tmp = path.copy()
            if ''.join(tmp) == s: ans.append(tmp)
            return
        for i in range(cur, len(s)):  # 3 单层搜索
            if ispalindrome(s[cur:i + 1]):
                path.append(s[cur:i + 1])
                backtrack(i + 1)
                path.pop()
            else:
                backtrack(i + 1)

    backtrack(0)
    return ans


def partition2(s: str) -> list[list[str]]:
    """ 使用组合思想 切割 优化写法 """
    path, ans = [], []

    def ispalindrome(subs: str) -> bool:
        p, q = 0, len(subs) - 1
        while p < q:
            if subs[p] != subs[q]:
                return False
            else:
                p += 1
                q -= 1
        return True

    def backtrack(cur):  # 1 参数列表 与 返回值
        if cur >= len(s):  # 2 终止条件
            tmp = path.copy()
            if ''.join(tmp) == s: ans.append(tmp)
            return
        for i in range(cur, len(s)):  # 3 单层搜索
            if not ispalindrome(s[cur:i + 1]):  # 如果本次切割的子串不是回文串，跳过，进行下一个[cur,i+1]范围的切割
                continue
            path.append(s[cur:i + 1])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return ans


def partition3(s: str) -> list[list[str]]:
    """
        使用组合思想 切割 优化写法
        使用 动态规划 预处理 回文串判断
    """
    path, ans = [], []

    # dp 预判断 子串是否回文
    dp = [[True] * len(s) for _ in range(len(s))]  # 二维dp数组
    # 先更新列，后更新行，从左上到右下
    for j in range(1, len(s)): # dp[i][0]=True，第一列j=0肯定小于等于每一行的i，因为行数和列数相等
        for i in range(len(s)-1): # dp[len(s)-1][j]=True，最后一行i=len(s)-1肯定大于等于每一列的j，因为行数和列数相等
            if i >= j:
                dp[i][j] = True
            else:
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
    import numpy
    print(numpy.array(dp))

    def backtrack(cur):  # 1 参数列表 与 返回值
        if cur >= len(s):  # 2 终止条件
            tmp = path.copy()
            if ''.join(tmp) == s: ans.append(tmp)
            return
        for i in range(cur, len(s)):  # 3 单层搜索
            if not dp[cur][i]:  # 如果本次切割的子串不是回文串，跳过，进行下一个[cur,i+1]范围的切割
                continue
            path.append(s[cur:i + 1])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return ans

def partition4(s: str) -> list[list[str]]:
    """
        使用组合思想 切割 优化写法
        使用 动态规划 预处理 回文串判断
    """
    path, ans = [], []

    # dp 预判断 子串是否回文
    dp = [[True]* len(s) for _ in range(len(s))] # 二维dp数组
    # 先更新行，后更新列
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
    import numpy
    print(numpy.array(dp))

    def backtrack(cur):  # 1 参数列表 与 返回值
        if cur >= len(s):  # 2 终止条件
            tmp = path.copy()
            if ''.join(tmp) == s: ans.append(tmp)
            return
        for i in range(cur, len(s)):  # 3 单层搜索
            if not dp[cur][i]:  # 如果本次切割的子串不是回文串，跳过，进行下一个[cur,i+1]范围的切割
                continue
            path.append(s[cur:i + 1])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return ans

if __name__ == '__main__':
    # s = "google"
    s = "aab"
    # ans = partition(s)
    # ans = partition2(s)
    ans = partition3(s)
    print(ans)
