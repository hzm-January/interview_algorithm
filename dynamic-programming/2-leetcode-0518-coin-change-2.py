def change(amount: int, coins: list[int]) -> int:
    """
        完全背包 动态规划
        dp数组含义：dp[j] 背包容量为j，有dp[j]种组合可以装满背包
    :param amount:
    :param coins:
    :return:
    """
    n = len(coins)
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(n):  # 先遍历物品
        for j in range(coins[i], amount + 1):  # 后遍历背包
            dp[j] = dp[j] + dp[j - coins[i]]
        print(i, dp)
    return dp[-1]


def change2(amount: int, coins: list[int]) -> int:
    """
        完全背包 动态规划
        dp数组含义：dp[j] 背包容量为j，有dp[j]种组合可以装满背包
    :param amount:
    :param coins:
    :return:
    """
    n = len(coins)
    dp = [0] * (amount + 1)
    dp[0] = 1
    # 在每一轮背包容量 j 的遍历中，尝试放入每一个物品 i，更新 dp[j]
    for j in range(amount + 1): # 先遍历背包
        for i in range(n): # 后遍历物品
            if j>=coins[i]:
                print(j, j - coins[i])
                dp[j] = dp[j] + dp[j - coins[i]]
            # print(' ', i, dp)
        # print(j, dp)
    return dp[-1]


if __name__ == '__main__':
    coins, amount = [1, 2, 5], 5
    # coins, amount = [2], 3
    # coins, amount = [10], 10
    ans = change(amount, coins)
    print(ans)
    ans = change2(amount, coins)
    print(ans)
