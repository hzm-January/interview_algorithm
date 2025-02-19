from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ 暴力  超时 """
        n = len(nums)
        max_sum = nums[0]
        for i in range(n): # i为左边界
            sum=0
            for j in range(i, n): # 移动右边界j
                sum += nums[j]
                max_sum = max(max_sum, sum)
        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        """ 贪心 """
        n = len(nums)
        max_sum = nums[0]
        sum = 0
        for i in range(1, n):
            if sum<0:
                sum = nums[i]
            else:
                sum += nums[i]
            max_sum = max(max_sum, sum)
        return max_sum



if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(nums)
    s = Solution()
    print(s.maxSubArray(nums))
    print(s.maxSubArray2(nums))
