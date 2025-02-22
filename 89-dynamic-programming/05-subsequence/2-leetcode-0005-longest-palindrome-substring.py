class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 0
        ans =''
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j==i:
                    dp[i][j] = True
                elif j-i==1:
                    dp[i][j] = s[i]==s[j]
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
                # max_len = max(max_len, j-i+1)
                if dp[i][j] and j - i + 1 > max_len:
                    ans=s[i:j + 1]
                    max_len = j - i + 1
                # print(i,j,s[i:j+1])
                # print(dp)
        return ans


if __name__ == '__main__':
    s = "babad"
    # s = "cbbd"
    print(Solution().longestPalindrome(s))
