from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            # num1 去重
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, n):
                # num2 去重
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                curTarget = target - nums[i] - nums[j]
                left, right = j + 1, n - 1
                while left < right:
                    if nums[left] + nums[right] < curTarget:
                        left += 1
                    elif nums[left] + nums[right] > curTarget:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]: left += 1
                        while left < right and nums[right] == nums[right - 1]: right -= 1
                        left += 1
                        right -= 1

        return ans


if __name__ == '__main__':
    # nums, target = [1, 0, -1, 0, -2, 2], 0
    nums, target = [2, 2, 2, 2, 2], 8
    print(Solution().fourSum(nums, target))
