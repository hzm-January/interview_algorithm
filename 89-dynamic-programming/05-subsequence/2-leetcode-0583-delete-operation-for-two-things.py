class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
           1 dp定义：dp[i][j] word1以i-1结尾和word2以j-1结尾的字符串需要dp[i][j]步操作后相同
           2 递推公式：相同-dp[i-1][j-1]，不同-min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)
           3 dp初始化：dp[i][0]=i, dp[0][j]=j
           4 遍历顺序：从前到后，从上到下
           5 打印：
        """
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # dp 初始化
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(m + 1):
            dp[0][i] = i
        # 遍历
        for i in range(1, n + 1):  # 注：这里从1开始
            for j in range(1, m + 1): # 注 ：这里从1开始
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] # 不需要删除字符
                else:
                    # 通俗易懂版
                    # dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 2)

                    # 简化版 dp[i - 1][j - 1] + 2 的情况包含在 dp[i - 1][j] + 1 中，也包含在dp[i][j - 1] + 1中
                    # 模拟删除s[i-1]，模拟删除t[j-1]
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)

        return dp[-1][-1]


if __name__ == '__main__':
    # word1, word2 = "sea", "eat"
    word1, word2 = "leetcode", "etco"
    print(Solution().minDistance(word1, word2))
