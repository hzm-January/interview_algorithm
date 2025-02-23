from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path, ans = [], []
        used = [0] * n

        def backtracking():
            if len(path) == n:
                ans.append(path.copy())
                return

            for i in range(0, n):  # 注意这里是从0到n-1
                if used[i] == 1: continue
                path.append(nums[i])
                used[i] = 1
                backtracking()
                used[i] = 0
                path.pop()
        backtracking()
        return ans

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))