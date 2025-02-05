def numTrees(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    return dp[n]


def numTrees_2(n: int) -> int:
    """
     卡特兰数
    """
    C = 1
    for i in range(0, n):
        C = C * 2 * (2 * i + 1) / (i + 2)
    return int(C)


if __name__ == '__main__':
    # nt = numTrees(10)
    # nt = numTrees(3)
    # nt = numTrees(1)
    nt = numTrees_2(3)
    # nt = numTrees_2(1)
    print(nt)
