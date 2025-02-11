def coinChange(coins: list[int], amount: int) -> int:
    """
        完全背包  动态规划  组合
        dp数组含义：背包容量为j，装满背包最少需要dp[j]个硬币。
        先遍历物品后遍历背包
    :param coins:
    :param amount:
    :return:
    """
    n = len(coins)
    dp = [10001] * (amount + 1)
    dp[0] = 0
    for i in range(n):  # 先遍历物品
        for j in range(coins[i], amount + 1):  # 后遍历背包
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        # print(i, dp)
    return dp[-1] if dp[-1] != 10001 else -1

def coinChange2(coins: list[int], amount: int) -> int:
    """
        完全背包  动态规划  组合
        dp数组含义：背包容量为j，装满背包最少需要dp[j]个硬币。
        先遍历背包后遍历物品
    :param coins:
    :param amount:
    :return:
    """
    n = len(coins)
    dp = [10001] * (amount + 1)
    dp[0] = 0
    for j in range(amount + 1):  # 后遍历背包
        for i in range(n):  # 先遍历物品
            if j>=coins[i]:
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        # print(i, dp)
    return dp[-1] if dp[-1] != 10001 else -1

if __name__ == "__main__":
    # coins, target = [1, 2, 5], 11
    coins, target = [2], 3
    # coins, target = [1], 0
    # ans = coinChange(coins, target)
    ans = coinChange2(coins, target)
    print(ans)
