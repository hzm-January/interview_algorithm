import random
from typing import List


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #
    #     """
    #         错误代码：该写法有一个超长测试点不通过，超时
    #         超时样例[1,1,1,....,1,1,1,1,,1,1,....,1,1,1,11,,1,1,1,1,1,1,....,1,1] 全1
    #
    #           排查发现原因是：partition函数中，快慢指针的分区方式性能差，在全是1的情况下，会一直扫描到r-1，然后下次分区从(l,r-2)再下次从(l,r-3)
    #           方法一：换成两个指针一个从前到后，一个从后到前，遇到符合条件的才交换，可以解决超时问题。
    #                 （猜想）之所以这种方法解决超时，是因为全1的情况下，两边都向中间走，下次分区从(l,l+(r-l)//2)，再下次分区再除2
    #                  这种方法仍然不够优秀，如果测试样例的长度足够长，仍然会超时。
    #           思考：要解决超时问题，就要解决全1这种情况，或者测试样例中，大部分的元素是相同元素的情况
    #           方法二：三路划分（优秀）
    #                   sepl, seqr = l-1, l-1 # 分别指向大于pivot的最后一个元素，大于等于pivot的最后一个元素
    #                   每次分区会有三个子区间：[大于pivot][等于pivot][小于pivot]
    #                   如果 sepl<left+kth<=seqr ，直接返回pivot，此时结果在[等于pivot]区间
    #                   如果 left+kth<=sepl，在[大于pivot]区间内继续找
    #                   如果 left+kth>seqr，在[小于pivot]区间内继续找
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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            快排  三路划分
        """

        def partition(l, r) -> (int, int):
            # p_i = random.randint(l, r)
            # nums[p_i], nums[r] = nums[r], nums[p_i]
            pivot = nums[r]
            #  以下分区代码可以解决超时问题，双指针，一个指针从前到后，一个指针从后到前，符合条件才交换。
            sepl, sepr = l - 1, l - 1  # 初始化 sepl 和 sepr
            for i in range(l, r + 1):
                if nums[i] > pivot:  # 当前元素大于pivot
                    sepr += 1  # 先换到[等于pivot]的最后一个元素的下一个位置
                    if sepr != i:
                        nums[i], nums[sepr] = nums[sepr], nums[i]
                    sepl += 1  # 再换到[大于pivot]的最后一个元素的下一个位置
                    if sepl != sepr:
                        nums[sepl], nums[sepr] = nums[sepr], nums[sepl]
                elif nums[i] == pivot:
                    sepr += 1
                    if sepr != i:
                        nums[i], nums[sepr] = nums[sepr], nums[i]
            return sepl, sepr

        def qSort(l, r, kth):
            if l == r: return
            sepl, sepr = partition(l, r)
            if sepl < l + kth <= sepr:
                return
            elif sepl >= l + kth:
                qSort(l, sepl, kth)  #
            else:
                qSort(sepr + 1, r, kth - (sepr - l + 1))

        qSort(0, len(nums) - 1, k - 1)
        return nums[k - 1]

    def findKthLargest1_2(self, nums: List[int], k: int) -> int:
        """
            快排  三路划分
            带 return 的写法
        """

        def partition(l, r) -> (int, int):
            # p_i = random.randint(l, r)
            # nums[p_i], nums[r] = nums[r], nums[p_i]
            pivot = nums[r]
            #  以下分区代码可以解决超时问题，双指针，一个指针从前到后，一个指针从后到前，符合条件才交换。
            sepl, sepr = l - 1, l - 1  # 初始化 sepl 和 sepr
            for i in range(l, r + 1):
                if nums[i] > pivot:  # 当前元素大于pivot
                    sepr += 1  # 先换到[等于pivot]的最后一个元素的下一个位置
                    if sepr != i:
                        nums[i], nums[sepr] = nums[sepr], nums[i]
                    sepl += 1  # 再换到[大于pivot]的最后一个元素的下一个位置
                    if sepl != sepr:
                        nums[sepl], nums[sepr] = nums[sepr], nums[sepl]
                elif nums[i] == pivot:
                    sepr += 1
                    if sepr != i:
                        nums[i], nums[sepr] = nums[sepr], nums[i]
            return sepl, sepr

        def qSort(l, r, kth):
            if l == r: return nums[l]
            sepl, sepr = partition(l, r)
            if sepl < l + kth <= sepr:
                return nums[sepr]
            elif sepl >= l + kth:
                return qSort(l, sepl, kth)  #
            else:
                return qSort(sepr + 1, r, kth - (sepr - l + 1))

        return qSort(0, len(nums) - 1, k - 1)

    def findKthLargest4(self, nums: List[int], k: int) -> int:
        """
            快排
            这种写法，比三路划分性能更好！
        """

        def partition(l, r):
            p_i = random.randint(l, r)  # 通过提交性能对比，发现随机选择pivot在第k大元素问题中，能将性能从300ms提升到50ms
            nums[p_i], nums[r] = nums[r], nums[p_i]
            pivot = nums[r]
            #  以下分区代码可以解决超时问题，双指针，一个指针从前到后，一个指针从后到前，符合条件才交换。
            i, j = l, r - 1  # 初始化 i 和 j
            while i <= j:
                while nums[i] > pivot:  # 找到左边第一个 > partition 的元素
                    i += 1
                while nums[j] < pivot:  # 找到右边第一个 < partition 的元素
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
            if p == k - 1:
                return nums[p]
            elif p > k - 1:
                return qSort(l, p - 1)
            else:
                return qSort(p + 1, r)

        return qSort(0, len(nums) - 1)

    def findKthLargest4_2(self, nums: List[int], k: int) -> int:
        """
            快排
            这种写法，比三路划分性能更好！
        """

        def partition(l, r):
            p_i = random.randint(l, r)  # 通过提交性能对比，发现随机选择pivot在第k大元素问题中，能将性能从300ms提升到50ms
            nums[p_i], nums[r] = nums[r], nums[p_i]
            pivot = nums[r]
            #  以下分区代码可以解决超时问题，双指针，一个指针从前到后，一个指针从后到前，符合条件才交换。
            i, j = l, r - 1  # 初始化 i 和 j
            while i <= j:
                while nums[i] > pivot:  # 找到左边第一个 > partition 的元素
                    i += 1
                while nums[j] < pivot:  # 找到右边第一个 < partition 的元素
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
            if p >= k - 1:  # 注意这里与findKthLargest4中写法不同，可AC
                return qSort(l, p - 1)
            else:
                return qSort(p + 1, r)

        return qSort(0, len(nums) - 1)

    def findKthLargest4_3(self, nums: List[int], k: int) -> int:
        """
            快排 规范写法 官方题解 排序从小到大
            这种写法的规范写法，比三路划分性能更好！

        """

        def partition(l, r):
            p_i = random.randint(l, r)  # 通过提交性能对比，发现随机选择pivot在第k大元素问题中，能将性能从300ms提升到50ms
            nums[p_i], nums[r] = nums[r], nums[p_i]
            pivot = nums[r]
            #  以下分区代码可以解决超时问题，双指针，一个指针从前到后，一个指针从后到前，符合条件才交换。
            i, j = l-1, r+1  # 初始化 i 和 j
            while i < j:
                i+=1
                while nums[i] < pivot:  # 找到左边第一个 < partition 的元素
                    i += 1
                j-=1
                while nums[j] > pivot:  # 找到右边第一个 > partition 的元素
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]  # 交换元素
            return j

        def qSort(l, r, k):
            # 注意：为什么这里直接返回nums[k-1]，不断缩小搜索区间来逼近第 k 个最大元素。
            # 当区间缩小到只有一个元素时，这个元素一定是我们要找的结果，因为：
            # 在每次分区操作中，我们已经确保了左边的元素都大于等于基准元素，右边的元素都小于基准元素。
            # 通过递归或迭代，我们已经将搜索范围缩小到了第k个最大元素所在的区间。
            # 当区间只有一个元素时，这个元素就是第k个最大元素。

            if l >= r: return nums[k]  # 因为此时数组0~k-2一定是小于nums[k-1]的数，nums[k-1]就是最终答案
            # if l >= r: return nums[r] # 这里返回nums[r]也可以
            # if l >= r: return nums[l] # 这里返回nums[l]也可以
            p = partition(l, r)
            if p >= k:  # 注意这里与findKthLargest4中写法不同，可AC
                return qSort(l, p, k)
            else:
                return qSort(p + 1, r, k)

        return qSort(0, len(nums) - 1, len(nums)-k) # 求第n-k小
    def findKthLargest4_4(self, nums: List[int], k: int) -> int:
        """
            快排 规范写法 官方题解 排序从大到小
            这种写法的规范写法，比三路划分性能更好！

        """

        def partition(l, r):
            # p_i = random.randint(l, r)  # 通过提交性能对比，发现随机选择pivot在第k大元素问题中，能将性能从300ms提升到50ms
            # nums[p_i], nums[r] = nums[r], nums[p_i]
            pivot = nums[r]
            #  以下分区代码可以解决超时问题，双指针，一个指针从前到后，一个指针从后到前，符合条件才交换。
            i, j = l-1, r+1  # 初始化 i 和 j
            while i < j:
                i+=1
                while nums[i] > pivot:  # 找到左边第一个 > partition 的元素
                    i += 1
                j-=1
                while nums[j] < pivot:  # 找到右边第一个 < partition 的元素
                    j -= 1
                if i < j and nums[i]!=nums[j]: # 不相同时再交换，相同不用交换
                    nums[i], nums[j] = nums[j], nums[i]  # 交换元素
            return i

        def qSort(l, r):
            # 注意：为什么这里直接返回nums[k-1]，不断缩小搜索区间来逼近第 k 个最大元素。
            # 当区间缩小到只有一个元素时，这个元素一定是我们要找的结果，因为：
            # 在每次分区操作中，我们已经确保了左边的元素都大于等于基准元素，右边的元素都小于基准元素。
            # 通过递归或迭代，我们已经将搜索范围缩小到了第k个最大元素所在的区间。
            # 当区间只有一个元素时，这个元素就是第k个最大元素。

            if l >= r: return nums[k-1]  # 因为此时数组0~k-2一定是大于nums[k-1]的数，nums[k-1]就是最终答案
            # if l >= r: return nums[r] # 这里返回nums[r]也可以
            # if l >= r: return nums[l] # 这里返回nums[l]也可以
            p = partition(l, r) # p返回的是符合条件范围的下一个位置
            print(nums)
            # 注意：该写法中，不能拆开写为以下，报错，测试样例：[3,2,1,5,6,4]
            # if p==k: return nums[k-1]
            # if p>k: return qSort(l,p-1)
            if p >= k:  # p返回的是符合条件范围的下一个位置。
                return qSort(l, p-1)
            else:
                return qSort(p, r)

        return qSort(0, len(nums) - 1) # 求第n-k小
    
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
    # nums,k=[3,2,1,1,1,1,1,1,1,1,1,1,1],9
    # ans = Solution().findKthLargest(nums, k)
    # print(nums)
    # print(ans)
    # ans = Solution().findKthLargest(nums, k)
    # ans = Solution().findKthLargest1_2(nums, k)
    # ans = Solution().findKthLargest4(nums, k)
    # ans = Solution().findKthLargest4_3(nums, k)
    ans = Solution().findKthLargest4_5(nums, k)
    # ans = Solution().findKthLargest2(nums, k)
    print(nums)
    print(ans)
