from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ 回溯写法1 """
        path, ans = [], []

        def backtracking(nums, startIndex):
            ans.append(path.copy())
            if startIndex >= len(nums):
                return
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return ans

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """ 回溯写法1 省略终止条件 """
        path, ans = [], []

        def backtracking(nums, startIndex):
            ans.append(path.copy())
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return ans

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        """ 回溯写法2 """
        path, ans = [], []
        n = len(nums)

        def backtracking(nums, startIndex, k):
            if len(path) == k:
                ans.append(path.copy())
                return
            for i in range(startIndex, n - (k - len(path)) + 1):
                path.append(nums[i])
                backtracking(nums, i + 1, k)
                path.pop()

        for i in range(n + 1):
            path = []
            backtracking(nums, 0, i)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
