from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """ 单调栈 """
        n = len(nums)
        nums = nums + nums
        stack = [0]
        ans = [-1] * n
        for i in range(1, n + n):
            while stack and nums[i] > nums[stack[-1]]:
                top = stack.pop()
                ans[top % n] = nums[i]
            stack.append(i)
        return ans


if __name__ == '__main__':
    # nums = [1, 2, 1]
    nums = [1, 2, 3, 4, 3]
    print(Solution().nextGreaterElements(nums))
