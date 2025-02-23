from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path, ans = [], []
        used_deep = [0] * n

        def backtracking():
            if len(path) == n:
                ans.append(path.copy())
                return
            used_level = set()
            for i in range(n):
                if used_deep[i] == 1: continue
                if nums[i] in used_level: continue
                path.append(nums[i])
                used_level.add(nums[i])
                used_deep[i] = 1
                backtracking()
                used_deep[i] = 0
                path.pop()

        nums.sort()
        backtracking()
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    # nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
