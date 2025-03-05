from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ 左右指针 """
        n = len(nums)
        nums.sort() # 一定要排序
        ans = []
        for i in range(n):
            if nums[i] > 0: continue
            if i > 0 and nums[i] == nums[i - 1]: continue
            target = -nums[i]
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else: # 找到答案
                    ans.append([nums[i], nums[left], nums[right]])
                    # left和right去重
                    # 值得学习，只用一个索引就可以对结果集中答案进行去重
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1

        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
