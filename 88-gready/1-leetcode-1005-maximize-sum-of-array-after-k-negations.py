from typing import List
"""
    k次取反后最大化的数组和
    首先想到的是回溯，但是超时。
"""

class Solution:
    def largestSumAfterKNegations3(self, nums: List[int], k: int) -> int:
        """
            错误代码 - 超时
            回溯写法 超时
            超时测试样例：[-1,-3,8,-6,-9,2,4,0]
        """
        n = len(nums)
        path, ans = nums.copy(), []
        maxSum = [0]
        # self.backtracking(nums, k, 0, path, ans, maxSum, 0)
        def backtracking(t, curSum):
            """ 该写法 超时 """
            if t == k:  # 1 终止条件
                if maxSum[0] < curSum:
                    maxSum[0] = curSum
                    ans = path.copy()
                return
            for i in range(n):
                path[i] = -path[i]
                backtracking(t+1, curSum - (-path[i]) + path[i])
                path[i] = -path[i]
        backtracking(0, sum(nums))
        return maxSum[0]
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        # print(nums)
        p = 0
        while p < n and p < k and nums[p] < 0:
            nums[p] = -nums[p]
            p += 1
        nums.sort()
        # print(nums)
        while p < k:
            nums[0] = -nums[0]
            p += 1
        return sum(nums)

    def largestSumAfterKNegations2(self, nums: List[int], k: int) -> int:
        """
            贪心 写法优化
            1 对数组按照绝对值从大到小排序
            2 从左向右遍历数组，遇到小于0的数字进行取反，直到结束或者操作次数大于k
            3 如果此时k没有消耗完，说明数组中所有的负数已经全部转换为正数，且还剩余操作次数，则对最小的非负数进行取反操作，直到消耗完k
            4 如果此时k消耗完，说明数组中有可能还有负数，但此时已经算是最优解，因为没有操作次数了，且之前的操作都是贪心的最优子区间的最优解
        """
        n = len(nums)
        nums.sort(key=abs, reverse=True)
        for i in range(n):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        if k % 2 == 1: nums[-1] = -nums[-1]
        return sum(nums)


if __name__ == '__main__':
    # nums,k = [-1, -3, 8, -6, -9, 2, 4, 0], 8
    # nums, k = [3, -1, 0, 2], 3
    # nums, k = [-8, 3, -5, -3, -5, -2], 6
    nums, k = [3, -1, 0, 2], 3
    print(Solution().largestSumAfterKNegations(nums, k))
