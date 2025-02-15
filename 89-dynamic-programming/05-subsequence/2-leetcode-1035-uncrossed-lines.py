def maxUncrossedLines(nums1: list[int], nums2: list[int]) -> int:
    """
        动态规划  求最长公共子序列
        使用i-1,j-1简化dp数组初始化
    """
    n,m = len(nums1), len(nums2)
    dp = [[0] * (m + 1) for i in range(n + 1)]
    max_len = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            max_len = max(max_len, dp[i][j])
        # print(dp)

    return dp[-1][-1]


def maxUncrossedLines2(nums1: list[int], nums2: list[int]) -> int:
    n, m = len(nums1), len(nums2)
    dp = [[0] * m for i in range(n)]
    Flag = False
    for i in range(n):
        if nums1[i]==nums2[0] or Flag:
            dp[i][0] = 1
            Flag = True
    Flag=False
    for j in range(m):
        if nums2[j]==nums1[0] or Flag:
            dp[0][j] = 1
            Flag = True
    for i in range(1, n):
        for j in range(1, m):
            if nums1[i]==nums2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[-1][-1]

if __name__ == '__main__':
    nums1, nums2 = [1, 4, 2], [1, 2, 4]
    print(maxUncrossedLines(nums1, nums2))
    print(maxUncrossedLines2(nums1, nums2))
