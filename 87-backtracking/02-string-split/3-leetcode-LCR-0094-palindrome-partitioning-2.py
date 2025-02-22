class Solution:
    def minCut(self, s: str) -> int:
        """ 代码超时 """
        # 动态规划  回文串预处理
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        # 回溯
        path, ans = [], []
        min_t = [n]

        def backtracking(cur):
            if cur >= n:
                if ''.join(path) == s:
                    ans.append(cur)
                    min_t[0] = min(min_t[0], len(path) - 1)
                return
            for i in range(cur, n):
                if dp[cur][i]:
                    path.append(s[cur:i + 1])
                    backtracking(i + 1)
                    path.pop()
                else:
                    backtracking(i + 1)

        backtracking(0)
        return min_t[0]

    def minCut2(self, s: str) -> int:
        """ 代码超时 """
        # 动态规划  回文串预处理
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        # 回溯
        path, ans = [], []
        min_t = [n]

        def backtracking(cur, t):
            if t >= min_t[0]: return # 剪枝
            if cur >= n:
                if ''.join(path) == s:
                    # ans.append(cur)
                    min_t[0] = min(min_t[0], t - 1)
                return
            for i in range(cur, n):
                if dp[cur][i]:
                    path.append(s[cur:i + 1])
                    backtracking(i + 1, t + 1)
                    path.pop()
                else:
                    backtracking(i + 1, t + 1)

        backtracking(0, 0)
        return min_t[0]


if __name__ == '__main__':
    s = "aab"
    # s = "a"
    # s = "ab"
    # print(Solution().minCut(s))
    print(Solution().minCut2(s))
