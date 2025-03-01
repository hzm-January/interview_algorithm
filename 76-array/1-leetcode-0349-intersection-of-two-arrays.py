from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ hash 表 """
        h1, h2 = {}, {}
        ans = []
        for num in nums1:
            h1[num] = h1.get(num, 0) + 1
        for num in nums2:
            h2[num] = h2.get(num, 0) + 1
        for k, v in h1.items():
            if k in h2:
                ans.append(k)
        return ans

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p, q = 0, 0
        ans = []
        while p < len(nums1) and q < len(nums2):
            if nums1[p] < nums2[q]:
                p += 1
            elif nums1[p] > nums2[q]:
                q += 1
            else: # nums1[p] == nums2[q] and
                if not ans or nums1[p] != ans[-1]:
                    ans.append(nums1[p])
                p += 1
                q += 1
        return ans


if __name__ == '__main__':
    # nums1, nums2 = [1, 2, 2, 1], [2, 2]
    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    print(Solution().intersection(nums1, nums2))
    print(Solution().intersection2(nums1, nums2))
