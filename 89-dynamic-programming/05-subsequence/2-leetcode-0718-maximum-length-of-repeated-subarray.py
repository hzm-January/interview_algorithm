def findLength(nums1: list[int], nums2: list[int]) -> int:
    """
        动态规划
        1 dp数组定义：以nums[i-1]为结尾的子序列1和nums2[j-1]为结尾的子序列2的最长重复子序列长度为dp[i][j]
            为什么用i-1,j-1？- 方便初始化
    :param nums1:
    :param nums2:
    :return:
    """
    n, m = len(nums1), len(nums2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if nums1[i - 1] == nums2[j - 1]:
                # print(i, j)
                dp[i][j] = dp[i - 1][j - 1] + 1
            max_len = max(max_len, dp[i][j])
        print(dp)
    return max_len


def findLength2(nums1: list[int], nums2: list[int]) -> int:
    """
        动态规划
        使用i,j
    """
    n, m = len(nums1), len(nums2)
    dp = [[0] * m for _ in range(n)]
    # 初始化
    # max_len要在初始化时一起更新，因为遍历是从1开始，最长重复子序列有可能在第一个元素，即dp的首行和首列
    # 最长重复子序列在第一个元素：[1, 2, 3, 2, 8], [5, 6, 1, 4, 7]
    # 没有最长重复子序列：[70,39,25,40,7], [52,20,67,5,31]
    max_len = 0
    for i in range(n):
        if nums1[i] == nums2[0]:
            dp[i][0] = 1
            max_len = max(max_len, dp[i][0])
    for i in range(m):
        if nums1[0] == nums2[i]:
            dp[0][i] = 1
            max_len = max(max_len, dp[0][i])

    for i in range(1, n):
        for j in range(1, m):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            max_len = max(max_len, dp[i][j])
            print(dp)
    return max_len


if __name__ == '__main__':
    # nums1, nums2 = [1, 2, 3, 2, 1], [3, 2, 1, 4, 7]
    # nums1, nums2 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    # nums1, nums2 = [1, 1, 0, 0, 1, 1], [0, 0]
    nums1, nums2 = [1, 2, 3, 2, 8], [5, 6, 1, 4, 7]
    ans = findLength(nums1, nums2)
    print(ans)
    print('--------------------------------------')
    ans = findLength2(nums1, nums2)
    print(ans)
