from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ hash 表 """
        h1,h2 = {},{}
        ans = []
        for num in nums1:
            h1[num] = h1.get(num, 0) + 1
        for num in nums2:
            h2[num] = h2.get(num, 0) + 1
        for k,v in h1.items():
            if k in h2:
                ans.append(k)
        return ans


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    # nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    print(Solution().intersection(nums1, nums2))
