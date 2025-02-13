def rob(nums: list[int]) -> int:
    """
        打家劫舍2 动态规划
    """

    def _rob(nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            # print(i, dp)
        return dp[-1]

    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums[0], nums[1])
    return max(_rob(nums[1:]), _rob(nums[:-1]))


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    ans = rob(nums)
    print(ans)
