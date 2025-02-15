def maxProfit(prices: list[int], fee: int) -> int:
    """
        动态规划
        1 dp数组定义
            dp[i][0]
            dp[i][1] 不持有股票
            dp[i][2] 持有股票
    """
    n = len(prices)
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0][0] = 0 # 未进行过任何操作，该状态可省略
    dp[0][1] = 0
    dp[0][2] = -prices[0]
    for i in range(1, n):
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] + prices[i] - fee)
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i]) # 题目要求可以进行多次交易，所以这里用用dp[i - 1][1] - prices[i]
        print(dp)
    # return dp[-1][1]
    return max(dp[-1])


if __name__ == '__main__':
    # prices, fee = [1, 3, 2, 8, 4, 9], 2
    prices, fee = [1, 3, 7, 5, 10, 3], 3
    ans = maxProfit(prices, fee)
    print(ans)
