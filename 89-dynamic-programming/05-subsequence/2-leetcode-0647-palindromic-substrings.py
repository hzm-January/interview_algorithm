class Solution:
    def countSubstrings(self, s: str) -> int:
        """
            动态规划
            1 dp数组定义：dp[i][j]表示s从i到j的子串是否是回文子串
            2 递推公式
            3 dp数组初始化
            4 遍历顺序：从下到上，从左到右。因为当前值是从左下推导。最终dp数组应该是上三角
            5 打印
        """
        n = len(s)
        # print(n)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1: # 同一字符i==j，相邻两个字符i+1=j且s[i]==s[j]
                        dp[i][j] = True
                        ans += 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                        if dp[i][j]: ans += 1
                    # print('--------------',i,j)
                # print(i,j,dp)
            print(dp)
        return ans

    def countSubstrings2(self, s: str) -> int:
        """
            动态规划
            1 dp数组定义：dp[i][j]表示s从i到j的子串是否是回文子串。i为左指针，j为右指针
            2 递推公式：dp[i][j]=dp[i+1][j-1]
            3 dp初始化
            4 遍历顺序：从下到上，从左到右。因为递推公式是从左下退出当前
        """
        n = len(s)
        # print(n)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1): # 左边界
            for j in range(i, n): # 右边界
                print(i, j, s[i:j + 1])
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans += 1
        return ans


if __name__ == '__main__':
    s = "aaa"
    # s = "abc"
    # s = "ababa"
    # s = "fdsklf"
    print(Solution().countSubstrings(s))
    # print(Solution().countSubstrings2(s))
