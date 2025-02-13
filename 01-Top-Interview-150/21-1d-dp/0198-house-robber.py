def rob(nums: list[int]) -> int:
    """
        打家劫舍 动态规划

    :param nums:
    :return:
    """
    if not nums: return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])  # 注意dp[1]的初始化，0大偷0,1大偷1
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        # print(dp)
    return dp[-1]


if __name__ == '__main__':
    # nums = [1, 2, 3, 1]
    # nums = [2, 7, 9, 3, 1]
    nums = [2, 1, 1, 2]
    ans = rob(nums)
    print(ans)
