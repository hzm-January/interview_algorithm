from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, num in enumerate(nums):
            if nums[i] in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False


if __name__ == '__main__':
    # nums, k = [1, 2, 3, 1], 3
    # nums, k = [1, 0, 1, 1], 1
    nums, k = [1, 2, 3, 1, 2, 3], 2
    print(Solution().containsNearbyDuplicate(nums, k))
