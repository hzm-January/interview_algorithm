import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ 快排 """
        def qSort(l, r, k):
            if l >= r: return nums[k]
            pivot = nums[l]
            p, q = l-1, r+1
            while p < q:
                p+=1
                while nums[p] < pivot:
                    p += 1
                q-=1
                while nums[q] > pivot:
                    q -= 1
                if p < q:
                    nums[p], nums[q] = nums[q], nums[p]

            if k<=p:
                return qSort(l, q, k)
            else:
                return qSort(q + 1, r, k)

        k = len(nums) - k
        return qSort(0, len(nums) - 1, k)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """ 堆排序 """
        import heapq
        nums[:] = [-num for num in nums]
        heapq.heapify(nums)  # 小顶堆
        nums[:] = [-heapq.heappop(nums) for _ in range(len(nums))]
        return nums[k - 1]


if __name__ == '__main__':
    # nums,k = [5, 1, 6, 2, 4, 3], 3
    nums, k = [3, 2, 1, 5, 6, 4], 2
    ans = Solution().findKthLargest(nums, k)
    # ans = Solution().findKthLargest2(nums, k)
    print(nums)
    print(ans)
