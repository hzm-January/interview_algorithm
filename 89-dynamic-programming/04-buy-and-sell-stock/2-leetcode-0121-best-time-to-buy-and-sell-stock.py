def maxProfit(prices: list[int]) -> int:
    """
        动态规划
        dp数组含义：
        dp[i][0]: 未持有股票的最大利润
        dp[i][1]:  持有股票的最大利润

    :param prices:
    :return:
    """
    n = len(prices)
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 0  #
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # 可以理解为：第一次买股票，手头金额一定是0，买完股票的金额一定是 0-prices[i]。没有递推关系。
        dp[i][1] = max(dp[i - 1][1], - prices[i]) # 注：该题只能买卖一次，这里必须是-prices[i]，
        # print(dp)
    return max(dp[n - 1][0], dp[n - 1][1])

def maxProfit2(prices: list[int]) -> int:
    """
        暴力解法 两层迭代找最优区间

        该方法会超时
    :param prices:
    :return:
    """
    ans = 0
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            ans = max(ans, prices[j] - prices[i])
    return ans

def maxProfit3(prices: list[int]) -> int:
    """ 贪心 """
    n = len(prices)
    min_price,max_profit = prices[0],0
    for i in range(n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit

def maxProfit4(prices: list[int]) -> int:
    """ 双指针 """
    n = len(prices)
    max_profit = 0
    slow = 0
    fast = 1
    while fast<n:
        profit = prices[fast] - prices[slow]
        if profit > max_profit:
            max_profit = profit
        elif profit < 0:
            slow = fast
        fast += 1
    return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    ans = maxProfit(prices)
    print(ans)
    ans = maxProfit2(prices)
    print(ans)
    ans = maxProfit3(prices)
    print(ans)
    ans = maxProfit4(prices)
    print(ans)
