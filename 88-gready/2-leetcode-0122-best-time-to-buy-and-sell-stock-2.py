from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            贪心
            求相邻两天的利润，大于0则相加
        """
        n = len(prices)
        sum = 0
        for i in range(1, n):
            profit = prices[i] - prices[i - 1]
            if profit>0: sum += profit
        return sum
    def maxProfit2(self, prices: List[int]) -> int:
        """
            贪心 - 精简写法
            求相邻两天的利润，大于0则相加
        """
        n = len(prices)
        sum=0
        for i in range(1, n):
            sum += max(0, prices[i] - prices[i - 1])
        return sum

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))