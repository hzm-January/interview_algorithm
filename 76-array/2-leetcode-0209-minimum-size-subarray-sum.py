from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        minlen = n + 1  # 初始化为数组长度+1
        i, j = 0, 0
        while j < n:  # j 窗口右边界
            sum += nums[j]
            while sum >= target:  # 窗口中的值总和大于target，窗口左边界右移，缩小窗口长度，使得窗口内元素总和刚好大于等于target，而不能大的太多
                minlen = min(minlen, j - i + 1)  # 更新记录当前窗口长度
                if sum - nums[i] < target:  # 如果尝试左边界移动，导致窗口内总和小于target，终止左边界右移
                    break
                sum -= nums[i]  # 更新窗口内总和
                # minlen = min(minlen, j - i)
                i += 1  # 窗口左边界右移
            j += 1  # 窗口右边界右移
        return minlen if minlen != n + 1 else 0


if __name__ == '__main__':
    # nums,target = [2, 3, 1, 2, 4, 3],7
    # nums, target = [1, 4, 4], 4
    nums, target = [1, 1, 1, 1, 1, 1, 1, 1], 11
    print(Solution().minSubArrayLen(target, nums))
