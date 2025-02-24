from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        path, ans = nums.copy(), []
        maxSum = [0]
        self.backtracking(nums, k, 0, path, ans, maxSum, 0)
        return maxSum[0]

    def backtracking(self, nums: List[int], k: int, t: int, path: List[int], ans: List[List[int]],
                     maxSum: list[int], curSum:int) -> None:
        """ 该写法 超时 """
        if t == k:  # 1 终止条件
            if maxSum[0] < curSum:
                maxSum[0] = curSum
                ans = path.copy()
            return
        for i in range(len(nums)):
            path[i] = -path[i]
            self.backtracking(nums, k, t + 1, path, ans, maxSum, curSum-(-path[i])+path[i])
            path[i] = -path[i]


if __name__ == '__main__':
    # nums, k = [4, 2, 3], 1
    # nums, k = [3, -1, 0, 2], 3
    nums, k = [2, -3, -1, 5, -4], 2
    print(Solution().largestSumAfterKNegations(nums, k))
