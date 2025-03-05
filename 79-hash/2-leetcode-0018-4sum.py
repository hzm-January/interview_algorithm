from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                if i>0 a