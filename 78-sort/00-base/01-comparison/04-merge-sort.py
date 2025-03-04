"""
    归并排序

    时间复杂度 O(nlogn) - 树深logn，树宽n
    空间复杂度 O(n) - 树每层需要总共长度为n的临时空间

"""


def mergeSort(nums: list[int]) -> list[int]:
    """ 归并排序 数组版 """

    def merge(left: list[int], right: list[int]) -> list[int]:
        sorted = []
        p, q, = 0, 0
        while p < len(left) and q < len(right):
            if left[p] <= right[q]:
                sorted.append(left[p])
                p += 1
            else:
                sorted.append(right[q])
                q += 1
        while p < len(left):
            sorted.append(left[p])
            p += 1
        while q < len(right):
            sorted.append(right[q])
            q += 1
        return sorted

    def sort(arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2  # 左闭右开
        # 左闭右开，merge中也是左闭右开
        left = sort(arr[:mid])  # 注意这里不能使用mid+1，当len=2时，mid+1=2，传入的数组长度又为2，会一直递归，导致栈溢出
        right = sort(arr[mid:])
        return merge(left, right)

    return sort(nums)


def mergeSort2(nums: list[int]) -> list[int]:
    """ 归并排序 指针版 """

    def merge(l, mid, r):
        sorted = []
        p, q = l, mid + 1
        while p <= mid and q <= r:
            if nums[p] <= nums[q]:
                sorted.append(nums[p])
                p += 1
            else:
                sorted.append(nums[q])
                q += 1
        while p <= mid:
            sorted.append(nums[p])
            p += 1
        while q <= r:
            sorted.append(nums[q])
            q += 1
        # print(l, r, sorted)
        nums[l:r + 1] = sorted

    def msort(l, r):
        if l >= r: return
        mid = l + (r - l) // 2  # 左闭右闭
        # 左闭右闭，merge中也是左闭右闭
        msort(l, mid)
        msort(mid + 1, r)  # 注意这里不能使用mid，当r-l=1时，mid=l，msort(mid,r)会一直迭代
        merge(l, mid, r)

    msort(0, len(nums) - 1)  # 左闭右闭
    return nums


def mergeSort3(nums: list[int]) -> list[int]:
    """ 非递归 归并排序 自底向上 """

    def merge(left, mid, right):
        sorted = []
        p, q = left, mid + 1
        while p <= mid and q <= right:
            if nums[p] <= nums[q]:
                sorted.append(nums[p])
                p += 1
            else:
                sorted.append(nums[q])
                q += 1
        while p <= mid:
            sorted.append(nums[p])
            p += 1
        while q <= right:
            sorted.append(nums[q])
            q += 1
        nums[left:right + 1] = sorted

    size = 1
    n = len(nums)
    while size < n:  # 递增每次处理子数组的长度
        # 子数组排序
        left = 0
        while left < n:
            mid = min(left + size - 1, n - 1)  # 找到mid
            right = min(left + size * 2 - 1, n - 1)  # 找到right
            merge(left, mid, right)  # 归并
            left = left + size * 2  # 更新left，进行下一组归并
        size <<= 1  # 子数组长度更新，每次更新为之前的两倍
    return nums


def mergeSort4(nums: list[int]) -> list[int]:
    """ 非递归 归并排序 自顶向下 """
    def merge(left, mid, right):
        sorted = []
        p, q = left, mid + 1
        while p <= mid and q <= right:
            if nums[p] <= nums[q]:
                sorted.append(nums[p])
                p += 1
            else:
                sorted.append(nums[q])
                q += 1
        while p <= mid:
            sorted.append(nums[p])
            p += 1
        while q <= right:
            sorted.append(nums[q])
            q += 1
        nums[left:right + 1] = sorted

    stack = [(0, len(nums) - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        mid = low + (high - low) // 2
        stack.append((low, mid))
        stack.append((mid + 1, high))
        merge(low, mid, high)
    return nums


if __name__ == '__main__':
    # nums = [5, 4, 3, 2, 1]
    # nums = [3, 2, 1, 5, 6]
    nums = [3, 6, 5, 2, 1]
    print(mergeSort(nums))
    print(mergeSort2(nums))
    print(mergeSort3(nums))
    print(mergeSort4(nums))
