class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
            双指针 是 错误解法
            测试样例："aa", "ab", "aaba"
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        p1, p2, p3 = 0, 0, 0
        if n1 + n2 != n3: return False
        if n1 == 0: return s2 == s3
        if n2 == 0: return s3 == s1
        while p3 < n3:
            if (p1 < n1 and s1[p1] != s3[p3]) and (p2 < n2 and s2[p2] != s3[p3]):
                return False
            while p1 < n1 and s1[p1] == s3[p3]:
                p1 += 1
                p3 += 1
            while p2 < n2 and s2[p2] == s3[p3]:
                p2 += 1
                p3 += 1
        return True

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        """ 动态规划 """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        for i in range(0, n1 + 1):
            for j in range(0, n2 + 1):
                if i>0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                # print('--', dp)
                if j>0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1] # 这里必须写dp[i][j]，否则有可能在i>0的逻辑中更新为True后，这里又重新被赋值为False
                # print('++', dp)
        return dp[-1][-1]

    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool:
        """ 动态规划 """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        for i in range(0, n1 + 1):
            for j in range(0, n2 + 1):
                if i > 0:
                    dp[i][j] = dp[i][j] or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                print('--', dp)
                if j > 0:
                    dp[i][j] = dp[i][j] or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])  # 这里必须写dp[i][j]，否则有可能在i>0的逻辑中更新为True后，这里又重新被赋值为False
                print('++', dp)
        return dp[-1][-1]


if __name__ == '__main__':
    # s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
    # s1, s2, s3 = "", "", ""
    # s1, s2, s3 = "", "", "a"
    # s1, s2, s3 = "", "b", "b"
    # s1, s2, s3 = "a", "", "c"
    # s1, s2, s3 = "aa", "ab", "aaba"
    s1, s2, s3 = "ab", "bc", "babc"
    # print(Solution().isInterleave(s1, s2, s3))
    print(Solution().isInterleave2(s1, s2, s3))
    print(Solution().isInterleave3(s1, s2, s3))
