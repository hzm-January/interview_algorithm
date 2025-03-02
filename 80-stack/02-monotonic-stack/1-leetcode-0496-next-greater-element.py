from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 单调栈 """
        hash = {}
        stack = [0]
        n, m = len(nums1), len(nums2)
        for i in range(m):
            while stack and nums2[i] > nums2[stack[-1]]:
                hash[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        ans = []
        for i in range(n):
            if nums1[i] in hash:
                ans.append(hash[nums1[i]])
            else:
                ans.append(-1)
        return ans
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 单调栈 写法优化 """
        hash = {}
        stack = [nums2[0]]
        n, m = len(nums1), len(nums2)
        for i in range(m):
            while stack and nums2[i] > stack[-1]:
                hash[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        ans = []
        for i in range(n):
            if nums1[i] in hash:
                ans.append(hash[nums1[i]])
            else:
                ans.append(-1)
        return ans

if __name__ == '__main__':
    # nums1, nums2 = [4, 1, 2], [1, 3, 4, 2]
    nums1, nums2 = [2, 4], [1, 2, 3, 4]
    print(Solution().nextGreaterElement(nums1, nums2))
    print(Solution().nextGreaterElement2(nums1, nums2))
