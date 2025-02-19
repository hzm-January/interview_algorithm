from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ 暴力  超时 """
        n = len(nums)
        max_sum = nums[0]
        for i in range(n):  # i为左边界
            sum = 0
            for j in range(i, n):  # 移动右边界j
                sum += nums[j]
                max_sum = max(max_sum, sum)
        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        """
            贪心
            局部最优的情况下，并记录最大的“连续和”，可以推出全局最优。
        """
        n = len(nums)
        max_sum = nums[0]
        sum = nums[0]
        for i in range(1, n):
            if sum < 0:  # 贪心：只要前序和为负数，累加在后面一定会减小后面的和
                sum = nums[i]
            else:
                sum += nums[i]
            max_sum = max(max_sum, sum)
        return max_sum

    def maxSubArray3(self, nums: List[int]) -> int:
        """ 动态规划 """
        n = len(nums)
        dp = [0] * n
        dp[1] = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])
        return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(nums)
    s = Solution()
    print(s.maxSubArray(nums))
    print(s.maxSubArray2(nums))
    print(s.maxSubArray3(nums))
