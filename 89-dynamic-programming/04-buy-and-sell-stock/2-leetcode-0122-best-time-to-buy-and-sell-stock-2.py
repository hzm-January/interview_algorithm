def maxProfit(prices: list[int]) -> int:
    """
        动态规划
        dp数组含义：
        dp[i][0] 未持有股票，最大利润
        dp[i][1] 持有股票，最大利润
    """
    n = len(prices)
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]) # 注意
    return dp[-1][0] # 最后未持有股票一定比持有股票利润大


def maxProfit2(prices: list[int]) -> int:
    """ 贪心 """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i]-prices[i-1] > 0:
            profit += prices[i]-prices[i-1]
    return profit
if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # ans = maxProfit(prices)
    ans = maxProfit2(prices)
    print(ans)
