def maxSubArray(nums: list[int]) -> int:
    """ 动态规划 """
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = nums[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i])
    return max_sum

def maxSubArray2(nums: list[int]) -> int:
    """ 动态规划 压缩状态矩阵 """
    n = len(nums)
    max_sum = cur_sum = nums[0]
    for i in range(1, n):
        cur_sum = max(cur_sum + nums[i], nums[i])
        max_sum = max(max_sum, cur_sum)
    return max_sum


if __name__ == '__main__':
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1]
    nums = [5, 4, -1, 7, 8]
    print(maxSubArray(nums))
