def isSubsequence(s: str, t: str) -> bool:
    """ 动态规划 最长公共子序列
        使用 i-1,j-1 简化dp数组初始化
    """
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1] == n
def isSubsequence2(s: str, t: str) -> bool:
    """
        动态规划 最长公共子序列
        使用i,j
    """
    n, m = len(s), len(t)
    if n==0: return True
    if m==0: return False
    dp = [[0] * m for _ in range(n)]
    #
    Flag = False
    for i in range(n):
        if s[i] == t[0] or Flag:
            dp[i][0] = 1
            Flag = True
    Flag = False
    for j in range(m):
        if s[0] == t[j] or Flag:
            dp[0][j] = 1
            Flag = True

    for i in range(1, n): # 注意这里是n
        for j in range(1, m): # 注意这里是m
            if s[i] == t[j]: # 注意这里是i,j
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1] == n

if __name__ == '__main__':
    # s, t = 'abc', 'ahbgdc'
    s, t = '', 'ahbgdc'
    # print(isSubsequence(s, t))
    print(isSubsequence2(s, t))
