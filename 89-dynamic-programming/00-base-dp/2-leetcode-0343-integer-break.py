def integerBreak(n: int) -> int:
    """
        动态规划
        1 dp数组含义：正整数i进行拆分后乘积最大为dp[i]
        2 递推公式：dp[i]=max(i*(j-i), i*dp[j-i], d[i])
        3 dp数组初始化：dp[2]=1
        4 遍历顺序：从前到后
        5 打印：
        6 优化：j遍历到i//2即可，数学证明：尽量拆分成相同数字能得到乘积最大值，例如：10 遍历到 5*5，再往后6*4没有5*5大
    """
    dp = [0] * (n + 1)
    dp[2] = 1
    for i in range(3, n + 1):
        for j in range(1, i // 2 + 1):
            dp[i] = max(j * (i - j), j * dp[i - j], dp[i])
    return dp[-1]

def integerBreak_5(n: int) -> int:
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
