def maxSubArray(nums: list[int]) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = nums[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i])
    return max_sum


if __name__ == '__main__':
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1]
    nums = [5, 4, -1, 7, 8]
    print(maxSubArray(nums))
