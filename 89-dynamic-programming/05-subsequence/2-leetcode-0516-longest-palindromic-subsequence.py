class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
            动态规划
            1 dp数组定义：dp[i][j]表示s从i到j的子串有多少回文子串
            2 递推公式
            3 dp数组初始化
            4 遍历顺序：从下到上，从左到右。因为当前值是从左下推导。最终dp数组应该是上三角
            5 打印
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                print(s[i:j + 1])
                if s[i] == s[j]:
                    if j == i:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # dp[i][j] = max(dp[i + 1][j - 1], dp[i][j - 1], dp[i + 1][j])
                    dp[i][j] = max(dp[i + 1][j - 1], dp[i][j - 1], dp[i + 1][j])
        return dp[0][-1]

    def longestPalindromeSubseq2(self, s: str) -> int:
        """ 动态规划 通俗易懂 """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # print(s[i:j + 1])
                if s[i] == s[j]:
                    if i == j:  # 处理一个字符的情况
                        dp[i][j] = 1
                    elif j - i == 1:  # 处理相邻两个字符相同的情况，i+1=j时
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # dp[i][j] = max(dp[i + 1][j - 1], dp[i][j - 1], dp[i + 1][j])
                    dp[i][j] = max(dp[i + 1][j - 1], dp[i][j - 1], dp[i + 1][j])
            # print(dp)
        return dp[0][-1]

    def longestPalindromeSubseq3(self, s: str) -> int:
        """ 动态规划 通俗易懂2 """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1  # 处理一个字符的情况
            for j in range(i + 1, n):
                # print(s[i:j + 1])
                if s[i] == s[j]:  # 处理相邻两个字符相同的情况，i+1=j时，dp[i+1][j-1]==dp[i+1][i]这个下标其实不合法，但是可以AC
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # dp[i][j] = max(dp[i + 1][j - 1], dp[i][j - 1], dp[i + 1][j])
                    dp[i][j] = max(dp[i + 1][j - 1], dp[i][j - 1], dp[i + 1][j])
            # print(dp)
        return dp[0][-1]


if __name__ == '__main__':
    s = "bbbab"
    # print(Solution().longestPalindromeSubseq(s))
    print(Solution().longestPalindromeSubseq2(s))
