from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
            空间复杂度必须为O(1)
            1 从后向前，寻找第一个“相邻升序”对，例如：123465 找到 "46"，索引记为i,j，此时[j,end]一定为逆序
            2 从后向前，寻找第一个k，使得A[i]<A[k]，找到 "5"
            3 交换 i, k 位置的元素，123465-123564，此时[j,end]一定为降序
            4 此时[j,end]一定为降序，将其反转为升序 123564-123546
            5 如果在1中找不到“相邻升序对”，说明[start,end]为降序，直接跳转到第4步
        """
        n = len(nums)
        j = n - 1
        # 1 从后向前，寻找第一个“相邻升序”对，例如：123465 找到 "46"，索引记为i,j，此时[j,end]一定为逆序
        while j > 0 and nums[j - 1] >= nums[j]:
            j -= 1
        # 找到了“相邻升序”对
        if j > 0:
            i = j - 1
            k = n - 1
            # 2 从后向前，寻找第一个k，使得A[i]<A[k]，找到 "5"
            while k > 0 and nums[i] >= nums[k]:
                k -= 1
            # 3 交换 i, k 位置的元素，123465-123564，此时[j,end]一定为降序
            nums[i], nums[k] = nums[k], nums[i]
        # 4 此时[j,end]一定为降序，将其反转为升序 123564-123546
        r = n - 1
        while j < r:
            nums[j], nums[r] = nums[r], nums[j]
            j += 1
            r -= 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 6, 5]
    Solution().nextPermutation(nums)
    print(nums)
