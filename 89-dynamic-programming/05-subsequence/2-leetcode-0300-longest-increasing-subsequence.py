def lengthOfLIS(nums: list[int]) -> int:
    """
        动态规划
        1 dp数组定义：以nums[i]结尾的最长连续子序列长度
        2 递推公式
        3 dp数组初始化：全1
        4 遍历顺序：从前到后
        5 打印
    :param nums:
    :return:
    """

    n = len(nums)
    if n==1: return 1
    dp = [1] * n
    max_subs_len = 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_subs_len = max(max_subs_len, dp[i])
    return max_subs_len


if __name__ == '__main__':
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [0, 1, 0, 3, 2, 3]
    nums = [7, 7, 7, 7, 7, 7, 7]
    ans = lengthOfLIS(nums)
    print(ans)
