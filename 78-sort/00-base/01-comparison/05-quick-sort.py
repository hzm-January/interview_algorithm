"""
    快速排序

    时间复杂度：O(nlong)
    空间复杂度：O(1)

    最坏时间复杂度情况O(n^2)-初始就有序，每层遍历都是从0~n-1，没有分治

"""
import random


def quickSort(nums: list[int]) -> list[int]:
    """ pivot 选最后一个元素 """

    def partition(l, r) -> int:
        pivot = nums[r]
        p, q = l, l
        while q < r:
            if nums[q] < pivot:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            q += 1
        nums[p], nums[r] = nums[r], nums[p]
        return p

    def qsort(l, r):
        if l >= r: return
        p = partition(l, r)
        qsort(l, p - 1)
        qsort(p + 1, r)

    qsort(0, len(nums) - 1)  # 左闭右闭
    return nums


def quickSort2(nums: list[int]) -> list[int]:
    """
        pivot 三数取中
        首，中，尾 三个数字的中位数
    """

    def partition(l, r) -> int:
        import statistics
        # 求三数中的中位数
        median = statistics.median([nums[l], nums[l + (r - l) // 2], nums[r]])
        median_index = nums.index(median)  # 找到中位数的索引
        nums[median_index], nums[r] = nums[r], nums[median_index]  # 交换中位数与末尾元素，方便后续处理
        pivot = nums[r]
        p, q = l, l
        while q < r:
            if nums[q] < pivot:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            q += 1
        nums[p], nums[r] = nums[r], nums[p]
        return p

    def qsort(l, r):
        if l >= r: return
        p = partition(l, r)
        qsort(l, p - 1)
        qsort(p + 1, r)

    qsort(0, len(nums) - 1)  # 左闭右闭
    return nums


def quickSort3(nums: list[int]) -> list[int]:
    """
        pivot 随机选择
    """

    def partition(l, r) -> int:
        import statistics
        # 求三数中的中位数
        pivot_index = random.randint(l, r)  # 左闭右闭
        nums[pivot_index], nums[r] = nums[r], nums[pivot_index]  # 交换pivot与末尾元素，方便后续处理
        pivot = nums[r]
        p, q = l, l
        while q < r:
            if nums[q] < pivot:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            q += 1
        nums[p], nums[r] = nums[r], nums[p]
        return p

    def qsort(l, r):
        if l >= r: return
        p = partition(l, r)
        qsort(l, p - 1)
        qsort(p + 1, r)

    qsort(0, len(nums) - 1)  # 左闭右闭
    return nums


def quickSort4(nums: list[int]) -> list[int]:
    """
        上面的方法都不是三路划分的写法，在leetcode 第k大元素问题中都会有超时问题，
        当前 三路划分 写法，能避免超时问题
        参考：leetcode 1738 官方题解
    """

    def partition(l, r) -> (int, int):
        """ 三路划分 """
        pivot = nums[r]
        p, q = l - 1, l - 1
        for i in range(l, r + 1):
            if nums[i] < pivot:  # 注：换成nums[i]>pivot，其他地方无需修改，就是降序排序
                q += 1
                if q != i:
                    nums[i], nums[q] = nums[q], nums[i]
                p += 1
                if p != q:
                    nums[p], nums[q] = nums[q], nums[p]
            elif nums[i] == pivot:
                q += 1
                if p != i:
                    nums[i], nums[q] = nums[q], nums[i]
        return p, q

    def qsort(l, r):
        if l >= r: return
        p, q = partition(l, r)  # [l,p]小于pivot，[p+1,q]等于pivot，[q+1,r]大于pivot
        qsort(l, p)
        qsort(q + 1, r)

    qsort(0, len(nums) - 1)  # 左闭右闭
    return nums


if __name__ == '__main__':
    # nums = [5, 4, 3, 2, 1]
    # nums = [3, 2, 1, 5, 6]
    nums = [3, 6, 5, 5, 4, 4, 3, 3, 5, 5, 2, 1]
    print(quickSort(nums))
    print(quickSort2(nums))
    print(quickSort3(nums))
    print(quickSort4(nums))
