from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n1, n2, n3, n4 = len(nums1), len(nums2), len(nums3), len(nums4)
        map = {}
        count = 0
        for i in range(n1):
            for j in range(n2):
                map[nums1[i] + nums2[j]] = map.get(nums1[i] + nums2[j], 0) + 1
        for i in range(n3):
            for j in range(n4):
                target = -(nums3[i] + nums4[j])
                count += map.get(target, 0)  # 不存在返回0，存在返回数量
        return count
