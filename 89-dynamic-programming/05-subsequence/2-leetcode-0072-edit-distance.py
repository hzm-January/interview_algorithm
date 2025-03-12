class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
           1 dp定义：word1以i-1结尾与word2以j-1结尾最少需要dp[i][j]次操作后相同
           2 递推公式：word1[i-1]==word2[j-1]
               相等：dp[i][j]=dp[i-1][j-1]
               不等：dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)，
                        dp[i-1][j-1]+1 是替换
                        dp[i][j-1]+1和dp[i-1][j] 是删除或添加，删除和添加的操作效果一样，次数一样
           3 初始化：dp[i][0]=i, dp[0][j]=j
           4 遍历顺序：从前到后，从上到下
           5 打印
        """
        n, m = len(word1), len(word2)
        if n * m == 0: return n + m
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
        return dp[-1][-1]


if __name__ == '__main__':
    # word1,word2 = "horse", "rose"
    # word1, word2 = "", "s"
    word1, word2 = "distance", "springbok"

    print(Solution().minDistance(word1, word2))
