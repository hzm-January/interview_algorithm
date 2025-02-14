def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    dp = [[0] * 5 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0] # 持有股票的状态
    dp[0][2] = 0 # 保持卖出股票的状态
    dp[0][3] = 0 # 卖出股票
    dp[0][4] = 0 # 冷冻期
    for i in range(1, n):
        dp[i][1] = max(dp[i - 1][1], max(dp[i - 1][2], dp[i - 1][4]) - prices[i]) # 持有股票（状态1）前一天为持有股票（状态1）或者（保持卖出股票）或者（冷冻期）
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][4]) # 保持卖出（状态2）前一天为保持卖出（状态2）或者冷冻期（状态4）
        dp[i][3] = dp[i - 1][1] + prices[i] # 卖出股票（状态3）前一天一定为持有股票（状态1）
        dp[i][4] = dp[i - 1][3] # 冷冻期（状态4）前一天一定为卖出股票（状态3）

    return max(dp[-1])


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    ans = maxProfit(prices)
    print(ans)
