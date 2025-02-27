from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0: return []
        left = 0 # 记录区间左端点
        ans = []
        for i in range(1, n):
            if nums[i - 1] + 1 != nums[i]: # 找到右端点，i-1
                if i-1 == left: # 如果 左端点==右端点
                    ans.append(str(nums[left]))
                else: # 如果 左端点<右端点
                    ans.append(str(nums[left])+'->'+str(nums[i-1]))
                left = i # 更新左端点
        if left==n-1: # 最后一个区间
            ans.append(str(nums[left]))
        else:
            ans.append(str(nums[left])+'->'+str(nums[n-1]))
        return ans

    def summaryRanges2(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0: return []
        left = 0 # 记录区间左端点
        ans = []
        for i in range(0, n-1):
            if nums[i] + 1 != nums[i+1]: # 找到右端点，i-1
                if i == left: # 如果 左端点==右端点
                    ans.append(str(nums[left]))
                else: # 如果 左端点<右端点
                    ans.append(str(nums[left])+'->'+str(nums[i]))
                left = i+1 # 更新左端点
        # 最后一个区间
        # Case 1: left==n-1
        # Case 2: left<n-1
        # 不可能left==n，最后一个区间一定是右开，不可能是右闭，例: [8->9]和[6->7, 9]两种情况后面都仍然可能递增只是没数字了，
        if left==n-1: # 只有最后一个数字
            ans.append(str(nums[left]))
        else: # 至少两个数字
            ans.append(str(nums[left])+'->'+str(nums[n-1]))
        return ans

if __name__ == '__main__':
    # nums = [0, 1, 2, 4, 5, 7]
    nums = [0, 2, 3, 4, 6, 8, 9]
    print(Solution().summaryRanges(nums))
    print(Solution().summaryRanges2(nums))
