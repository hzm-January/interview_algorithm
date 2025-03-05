from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        n = len(nums)
        for i in range(n):
            num1 = nums[i]
            num2 = target - num1
            if num2 in hash: # 先判断是否在hash中，如果没有再添加，可以保证不使用重复元素，即不将自己与自己匹配
                return [hash[num2],i]
            hash[num1]=i

