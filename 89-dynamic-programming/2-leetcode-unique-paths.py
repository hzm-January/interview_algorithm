def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    print(uniquePaths(m=3, n=7))
    print(uniquePaths(m=3, n=2))
    print(uniquePaths(m=7, n=3))
    print(uniquePaths(m=3, n=3))
