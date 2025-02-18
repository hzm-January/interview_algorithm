from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """ 暴力  超时 """
        n=len(nums)
        min_len = n+1
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total>=target:
                    min_len = min(min_len, j-i+1)
        return min_len if min_len!=n+1 else 0

if __name__ == '__main__':
    # nums, t = [2,3,1,2,4,3],7
    # nums,t = [1,4,4], 4
    nums,t = [1,1,1,1,1,1,1,1], 11
    print(Solution().minSubArrayLen(t, nums))
