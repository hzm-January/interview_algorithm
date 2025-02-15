def maxProfit(k: int, prices: list[int]) -> int:
    """
        动态规划
    """
    # 1 dp数组含义及初始化
    dp = [[0]*(2*k+1) for _ in range(len(prices))]
    for i in range(1, 2*k+1):
        if i%2==1:
            dp[0][i] = -prices[0]
    # 2 dp数组遍历
    for i in range(1, len(prices)):
        for j in range(1, 2*k+1):
            if j%2==1: # 第j//2次买入
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])
            else: # 第 j//2次卖出
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i])
    return dp[-1][-1]

def maxProfit2(k: int, prices: list[int]) -> int:
    """
        动态规划 写法优化
    """
    # 1 dp数组含义及初始化
    dp = [[0]*(2*k+1) for _ in range(len(prices))]
    for i in range(1, 2*k, 2):
        dp[0][i] = -prices[0]
    # 2 dp数组遍历
    for i in range(1, len(prices)):
        for j in range(0, 2*k, 2):
            dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i])
            dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i])
    return dp[-1][-1]

if __name__ == '__main__':
    prices,k = [3,2,6,5,0,3],2
    ans = maxProfit(k, prices)
    print(ans)