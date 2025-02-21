def numDistinct(s: str, t: str) -> int:
    """
        动态规划

        1 dp数组定义：以s[i]为结尾s子串中以t[j]为结尾t子串的个数为dp[i][j]
        2 递推公式：计算dp[i][j]时，只模拟删除s[i-1]，因为要求的是s中t的个数，只能删除s中的字符。
        3 dp数组初始化：dp[i][0]=1, dp[0][j]=0, dp[0][0]=1
        4 遍历顺序：从左到右从上到下，左上，左，上都可以推出dp[i][j]
        5 打印
    """
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # 初始化
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


if __name__ == '__main__':
    # s, t = "rabbbit", "rabbit"
    s,t = "babgbag","bag"
    print(numDistinct(s, t))
