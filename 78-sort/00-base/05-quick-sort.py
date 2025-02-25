"""
    快速排序

    时间复杂度：O(nlong)
    空间复杂度：O(1)

    最坏时间复杂度情况O(n^2)-初始就有序，每层遍历都是从0~n-1，没有分治

"""
def quickSort(nums: list[int]) -> list[int]:
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


if __name__ == '__main__':
    # nums = [5, 4, 3, 2, 1]
    # nums = [3, 2, 1, 5, 6]
    nums = [3, 6, 5, 2, 1]
    print(quickSort(nums))
    # print(mergeSort2(nums))
    # print(mergeSort3(nums))
