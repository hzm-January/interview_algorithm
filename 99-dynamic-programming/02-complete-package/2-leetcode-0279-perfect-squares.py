def numSquares(n: int) -> int:
    """
        完全平方数，动态规划，完全背包
        先遍历物品，后遍历背包
    :param n:
    :return:
    """
    # 求所有完全平方数
    def perfect_squares(n: int) -> list[int]:
        import math
        ps = []
        for i in range(1, n + 1):
            if int(math.sqrt(i)) ** 2 == i:
                ps.append(i)
        return ps

    ps = perfect_squares(n)
    print(ps)

    # dp
    m = len(ps)
    dp = [n+1] * (n + 1) # 要设置为最大值，min才能覆盖初始值
    dp[0],dp[1] = 0,1 # 初始化，0需要0个数。1需要1，1个数。
    for i in range(0, m): # 先遍历物品，必须从物品0开始，否则测试样例n=2报错。物品遍历本来就是从0开始，这里只是自己思维错误写了从1开始报错记录了错误原因。
        for j in range(ps[i], n+1): # 后遍历背包
            dp[j] = min(dp[j], dp[j - ps[i]] + 1)
        print(i, dp)
    # print(dp)

    return dp[-1]

def numSquares2(n: int) -> int:
    """
        完全平方数，动态规划，完全背包
        先遍历背包，后遍历物品
    :param n:
    :return:
    """
    # 求所有完全平方数
    def perfect_squares(n: int) -> list[int]:
        import math
        ps = []
        for i in range(1, n + 1):
            if int(math.sqrt(i)) ** 2 == i:
                ps.append(i)
        return ps

    ps = perfect_squares(n)
    print(ps)

    # dp
    m = len(ps)
    dp = [n+1] * (n + 1) # 要设置为最大值，min才能覆盖初始值
    dp[0],dp[1] = 0,1 # 初始化，0需要0个数。1需要1，1个数。
    for j in range(0, n + 1):  # 后遍历背包
        for i in range(0, m): # 先遍历物品，必须从物品0开始，否则测试样例n=2报错。物品遍历本来就是从0开始，这里只是自己思维错误写了从1开始报错记录了错误原因。
            if j>=ps[i]:
                dp[j] = min(dp[j], dp[j - ps[i]] + 1)
        # print(j, dp)
    # print(dp)

    return dp[-1]


def numSquares3(n: int) -> int:
    """
        完全平方数，动态规划，完全背包
        先遍历物品，后遍历背包
        优化判断完全平方数写法
    :param n:
    :return:
    """
    # dp
    dp = [n+1] * (n + 1) # 要设置为最大值，min才能覆盖初始值
    dp[0],dp[1] = 0, 1 # 初始化，0需要0个数。1需要1，1个数。
    for j in range(0, n + 1):  # 先遍历背包
        i = 0
        while i**2<=j: # 后遍历物品
            dp[j] = min(dp[j], dp[j - i*i] + 1)
            i+=1
        # print(j, dp)
    # print(dp)

    return dp[-1]

if __name__ == '__main__':
    # print(numSquares(12))
    # print(numSquares(13))
    # print(numSquares(3))
    # print(numSquares(2))

    # print(numSquares2(12))
    # print(numSquares2(13))
    # print(numSquares2(3))
    # print(numSquares2(2))

    print(numSquares3(12))
    print(numSquares3(13))
    print(numSquares3(3))
    print(numSquares3(2))
