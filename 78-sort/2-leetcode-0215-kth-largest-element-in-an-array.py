import random
from typing import List


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #
    #     """
    #         错误代码：该写法有一个超长测试点不通过，超时
    #         快排
    #     """
    #
    #     def partition(l, r):
    #         p_i = random.randint(l, r)
    #         nums[p_i], nums[r] = nums[r], nums[p_i]
    #         pivot = nums[r]
    #         p, q = l, l
    #         while q < r:  # 左闭右闭，但不访问最后一个元素pivot
    #             if nums[q] > pivot:
    #                 nums[p], nums[q] = nums[q], nums[p]
    #                 p += 1
    #             q += 1
    #         nums[p], nums[r] = nums[r], nums[p]
    #         return p
    #
    #     def qSort(l, r):
    #         # 注意：为什么这里直接返回nums[k-1]，不断缩小搜索区间来逼近第 k 个最大元素。
    #         # 当区间缩小到只有一个元素时，这个元素一定是我们要找的结果，因为：
    #         # 在每次分区操作中，我们已经确保了左边的元素都大于等于基准元素，右边的元素都小于基准元素。
    #         # 通过递归或迭代，我们已经将搜索范围缩小到了第k个最大元素所在的区间。
    #         # 当区间只有一个元素时，这个元素就是第k个最大元素。
    #
    #         if l >= r: return nums[k - 1]  # 因为此时数组0~k-2一定是大于nums[k-1]的数，nums[k-1]就是最终答案
    #         # if l >= r: return nums[r] # 这里返回nums[r]也可以
    #         # if l >= r: return nums[l] # 这里返回nums[l]也可以
    #         p = partition(l, r)
    #         if p == k - 1:
    #             return nums[p]
    #         elif p > k - 1:
    #             return qSort(l, p - 1)
    #         else:
    #             return qSort(p + 1, r)
    #
    #     return qSort(0, len(nums) - 1)

    def findKthLargest4(self, nums: List[int], k: int) -> int:
        """ 快排 """

        def partition(l, r):
            # p_i = random.randint(l, r)
            # nums[p_i], nums[r] = nums[r], nums[p_i]
            pivot = nums[r]
            i, j = l, r - 1  # 初始化 i 和 j
            while i <= j:
                while nums[i] > pivot:  # 找到左边第一个 >= partition 的元素
                    i += 1
                while nums[j] < pivot:  # 找到右边第一个 <= partition 的元素
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]  # 交换元素
                    i += 1
                    j -= 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

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
            print(p, nums)
            if p == k - 1:
                return nums[p]
            elif p > k - 1:
                return qSort(l, p - 1)
            else:
                return qSort(p + 1, r)

        return qSort(0, len(nums) - 1)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """ 快排 """

        def partition(l, r):
            p_i = random.randint(l, r)
            nums[p_i], nums[r] = nums[r], nums[p_i]
            pivot = nums[r]
            p, q = l - 1, r + 1
            while p < q:
                p += 1
                while nums[p] > pivot:
                    p += 1
                q -= 1
                while nums[q] < pivot:
                    q -= 1
                if p < q:
                    nums[p], nums[q] = nums[q], nums[p]
            return q

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
            if p >= k - 1:
                return qSort(l, p)
            else:
                return qSort(p + 1, r)

        return qSort(0, len(nums) - 1)

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        """ 堆排序 """
        import heapq
        nums[:] = [-num for num in nums]
        heapq.heapify(nums)  # 小顶堆
        nums[:] = [-heapq.heappop(nums) for _ in range(len(nums))]
        return nums[k - 1]


if __name__ == '__main__':
    # nums,k = [5, 1, 6, 2, 4, 3], 3
    nums, k = [3, 2, 1, 5, 6, 4], 2
    # nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    ans = Solution().findKthLargest4(nums, k)
    # ans = Solution().findKthLargest2(nums, k)
    print(nums)
    print(ans)
