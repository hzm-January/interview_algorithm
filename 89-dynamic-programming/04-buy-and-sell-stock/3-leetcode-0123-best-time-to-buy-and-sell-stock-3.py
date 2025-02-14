def maxProfit(prices: list[int]) -> int:
    """
        动态规划
        1 dp数组定义
            dp[i][0]: 不操作
            dp[i][1]；第一次持有股票
            dp[i][2]: 第一次不持有股票
            dp[i][3]: 第二次持有股票
            dp[i][4]: 第二次不持有
        2 递推公式
        3 初始化
        4 遍历顺序
    :param prices:
    :return:
    """
    n = len(prices)
    dp = [[0] * 5 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0] # 第一天买入
    dp[0][2] = 0 # 第一天买入又卖出
    dp[0][3] = -prices[0] # 第一天买入又卖出，再买入
    dp[0][4] = 0 # 第一天买入又卖出，再买入又卖出
    for i in range(1, n):
        dp[i][0] = dp[i][0]
        # dp[i][1]=max(dp[i-1][1], 0-prices[i]) # 直接写0也可以，首次买入前现金一定是0,
        dp[i][1]=max(dp[i-1][1], dp[i][0]-prices[i])
        dp[i][2]=max(dp[i-1][2], dp[i-1][1]+prices[i])
        dp[i][3]=max(dp[i-1][3], dp[i-1][2]-prices[i])
        dp[i][4]=max(dp[i-1][4], dp[i-1][3]+prices[i])
        print(dp)
    # return max(dp[-1]) # 取最大值也可以
    # 关于第二次卖出一定包含第一次卖出的例子：第一次卖出金额达到了最大，那么当天再买入一次卖出一次，就完成了题目要求的2次买卖，并且金额还是最大
    return dp[-1][4] # 卖出一定大于买入手头金额，且第二次卖出包含了第一次卖出手头金额


if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    ans = maxProfit(prices)
    print(ans)
