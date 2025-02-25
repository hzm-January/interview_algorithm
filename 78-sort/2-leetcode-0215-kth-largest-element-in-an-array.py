import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ 快排 """

        def partition(l, r):
            p_i = random.randint(l, r)
            nums[p_i], nums[r] = nums[r], nums[p_i]
            pivot = nums[r]
            p, q = l, l
            while q < r:  # 左闭右闭，但不访问最后一个元素pivot
                if nums[q] > pivot:
                    nums[p], nums[q] = nums[q], nums[p]
                    p += 1
                q += 1
            nums[p], nums[r] = nums[r], nums[p]
            return p

        def qSort(l, r):
            # 注意：为什么这里直接返回nums[k-1]，不断缩小搜索区间来逼近第 k 个最大元素。
            # 当区间缩小到只有一个元素时，这个元素一定是我们要找的结果，因为：
            # 在每次分区操作中，我们已经确保了左边的元素都大于等于基准元素，右边的元素都小于基准元素。
            # 通过递归或迭代，我们已经将搜索范围缩小到了第k个最大元素所在的区间。
            # 当区间只有一个元素时，这个元素就是第k个最大元素。

            if l >= r: return nums[k - 1]  # 因为此时数组0~k-2一定是大于nums[k-1]的数，nums[k-1]就是最终答案
            # if l >= r: return nums[r] # 这里返回nums[r]也可以
            # if l >= r: return nums[l] # 这里返回nums[l]也可以
            p = partition(l, r)
            if p == k - 1:
                return nums[p]
            elif p > k - 1:
                return qSort(l, p - 1)
            else:
                return qSort(p + 1, r)

        return qSort(0, len(nums) - 1)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """ 堆排序 """
        import heapq
        nums[:] = [-num for num in nums]
        heapq.heapify(nums) # 小顶堆
        nums[:] = [-heapq.heappop(nums) for _ in range(len(nums))]
        return nums[k - 1]


if __name__ == '__main__':
    # nums,k = [5, 1, 6, 2, 4, 3], 3
    nums, k = [3, 2, 1, 5, 6, 4], 2
    # ans = Solution().findKthLargest(nums, k)
    ans = Solution().findKthLargest2(nums, k)
    print(nums)
    print(ans)
