def integerBreak(n: int) -> int:
    dp = [0] * (n + 1)
    dp[2] = 1
    for i in range(3, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
    return dp[n]


def integerBreak_2(n: int) -> int:
    """
        初始化优化
    """
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
    return dp[n]


def integerBreak_3(n: int) -> int:
    """
        时间复杂度优化
    """
    if n <= 3:
        return n - 1
    dp = [0] * (n + 1)
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = max(2 * dp[i - 2], 2 * (i - 2), 3 * dp[i - 3], 3 * (i - 3))
    return dp[n]

def integerBreak_4(n: int) -> int:
    if n<=3:
        return n-1
    p, m = n//3, n%3
    if m==0:
        ans = 3**p
    elif m==1:
        ans = 3**(p-1)*4
    else: #m==2
        ans = 3**p *2
    return ans

if __name__ == '__main__':
    # max_m = integerBreak(10)
    # max_m = integerBreak_2(10)
    # max_m = integerBreak_3(10)
    max_m = integerBreak_4(10)
    print(max_m)
