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
        pivot_index = random.randint(l,r)  # 左闭右闭
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

if __name__ == '__main__':
    # nums = [5, 4, 3, 2, 1]
    # nums = [3, 2, 1, 5, 6]
    nums = [3, 6, 5, 2, 1]
    print(quickSort(nums))
    print(quickSort2(nums))
    print(quickSort3(nums))
