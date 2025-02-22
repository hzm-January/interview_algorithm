from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            动态规划

        """
        n, m = len(grid), len(grid[0])
        # dp定义
        dp = [[0 for _ in range(m)] for _ in range(n)]
        # 初始化
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # 遍历
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1]) # 推导公式
        return dp[-1][-1]

if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))