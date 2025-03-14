from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0: return []
        left = 0  # 记录区间左端点
        ans = []
        for i in range(1, n):
            if nums[i - 1] + 1 != nums[i]:  # 找到右端点，i-1
                if i - 1 == left:  # 如果 左端点==右端点
                    ans.append(str(nums[left]))
                else:  # 如果 左端点<右端点
                    ans.append(str(nums[left]) + '->' + str(nums[i - 1]))
                left = i  # 更新左端点
        if left == n - 1:  # 最后一个区间
            ans.append(str(nums[left]))
        else:
            ans.append(str(nums[left]) + '->' + str(nums[n - 1]))
        return ans

    def summaryRanges2(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0: return []
        left = 0  # 记录区间左端点
        ans = []
        for i in range(0, n - 1):
            if nums[i] + 1 != nums[i + 1]:  # 找到右端点，i-1
                if i == left:  # 如果 左端点==右端点
                    ans.append(str(nums[left]))
                else:  # 如果 左端点<右端点
                    ans.append(str(nums[left]) + '->' + str(nums[i]))
                left = i + 1  # 更新左端点
        # 最后一个区间
        # Case 1: left==n-1
        # Case 2: left<n-1
        # 不可能left==n，最后一个区间一定是右开，不可能是右闭，例: [8->9]和[6->7, 9]两种情况后面都仍然可能递增只是没数字了，
        if left == n - 1:  # 只有最后一个数字
            ans.append(str(nums[left]))
        else:  # 至少两个数字
            ans.append(str(nums[left]) + '->' + str(nums[n - 1]))
        return ans

    def summaryRanges_3(self, nums: List[int]) -> List[str]:
        """
            双指针
        """
        n = len(nums)
        i, j = 0, 1 # i指向区间左端点，j指向区间右端点
        ans = []
        while j < n:
            # 找到连续区间
            while j < n and nums[j - 1] + 1 == nums[j]:
                j += 1
            if i == j - 1:  # 一个数字成区间
                ans.append(str(nums[i]))
            else:  # 包含特殊逻辑：当上面while是因为j<n终止，说明数组中最后一段一直递增，此情况也进行处理
                ans.append(str(nums[i]) + "->" + str(nums[j - 1]))
            i = j  # 下一个区间新的起点为i
            j += 1
        if i == n - 1:  # 最后一个数字单独成区间，在上述逻辑中i=n-1,j=n
            ans.append((str(nums[i])))
        return ans


if __name__ == '__main__':
    # nums = [0, 1, 2, 4, 5, 7]
    nums = [0, 2, 3, 4, 6, 8, 9]
    print(Solution().summaryRanges(nums))
    print(Solution().summaryRanges2(nums))
