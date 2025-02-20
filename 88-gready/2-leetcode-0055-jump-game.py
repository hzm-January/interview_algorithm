from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ 贪心 """
        n = len(nums)
        max_steps = nums[0]
        j = 0
        while j <= max_steps:
            if j >= n: return True
            max_steps = max(max_steps, j + nums[j])
            j += 1
        return False


if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    print(Solution().canJump(nums))
