from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """ 回溯 树层去重 """
        n = len(nums)
        path, ans = [], []

        def backtracking(startIndex):
            if len(path) >= 2:
                ans.append(path.copy())
            # if startIndex>=n: # 可省略，因为下面的循环最大为n-1，如果startIndex为n，不会再进入循环
            #     return
            used = {} # 也可以用set
            for i in range(startIndex, n):
                if nums[i] in used and used[nums[i]]==1: continue # 树层去重
                used[nums[i]] = 1
                if path and path[-1] > nums[i]: continue # 非递减过滤
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()
        backtracking(0)
        return ans

if __name__ == '__main__':
    # nums = [4, 6, 7, 7]
    nums = [4,4,3,2,1]
    print(Solution().findSubsequences(nums))
