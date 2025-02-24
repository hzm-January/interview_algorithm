from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
            错误代码 超时
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



if __name__ == '__main__':
    # nums, k = [4, 2, 3], 1
    # nums, k = [3, -1, 0, 2], 3
    nums, k = [2, -3, -1, 5, -4], 2
    print(Solution().largestSumAfterKNegations(nums, k))
