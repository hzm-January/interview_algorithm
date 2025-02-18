def numDistinct(s: str, t: str) -> int:
    """
        动态规划
        1 dp数组定义：以s[i]为结尾子串中存在dp[i][j]个以t[j]为结尾子串
        2 递推公式：dp[i][j]=
        3 dp数组初始化：

    :param s:
    :param t:
    :return:
    """
    n, m = len(s), len(t)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for k in range(1, i):
            subs = s[k:i]
            for j in range(1, m+1):
                if 

    return - 1


if __name__ == '__main__':
    s, t = "rabbbit", "rabbit"
    print(numDistinct(s, t))
