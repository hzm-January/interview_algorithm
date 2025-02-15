def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
        动态规划
        i-1,j-1 简化初始化
    """
    n,m = len(text1), len(text2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            # print(i, j)
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            # print(i,j,dp)
    return dp[-1][-1]

def longestCommonSubsequence2(text1: str, text2: str) -> int:
    """
        动态规划
        i,j 没有简化初始化
    """
    n,m = len(text1), len(text2)
    dp = [[0]*m for _ in range(n)]

    # 初始化
    Flag=False
    for i in range(n):
        if text1[i] == text2[0] or Flag:
            dp[i][0] = 1
            Flag =True
    Flag=False
    for i in range(m):
        if text1[0] == text2[i] or Flag:
            dp[0][i] = 1
            Flag =True

    for i in range(1, n):
        for j in range(1, m):
            # print(i, j)
            if text1[i] == text2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            # print(i,j,dp)
    return dp[-1][-1]


if __name__ == '__main__':
    # text1, text2 = "abcde", "ace"
    text1, text2 = "bsbininm", "jmjkbkjkv"
    print(longestCommonSubsequence(text1, text2))
    print(longestCommonSubsequence2(text1, text2))
