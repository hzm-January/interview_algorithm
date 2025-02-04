def uniquePaths(m: int, n: int) -> int:
    dp = [[0] * n] * m
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


def uniquePaths_2(m: int, n: int) -> int:
    dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

def uniquePaths_3(m: int, n: int) -> int:
    ans = 1
    for i,j in zip(range(n, n+m-1), range(1, m)):
        ans = ans*i//j # 使用//保证是整数
    return ans
def uniquePaths_4(m: int, n: int) -> int:
    import math
    return math.comb(m+n-2,m-1)

if __name__ == '__main__':
    # n = uniquePaths(3,7)
    # n = uniquePaths_2(3, 7)
    n = uniquePaths_4(3, 7)
    print(n)
