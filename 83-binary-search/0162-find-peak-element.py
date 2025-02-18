import math
import random


def findPeakElement1(nums: list[int]) -> int:
    return nums.index(max(nums))


def findPeakElement1_2(nums: list[int]) -> int:
    index, max_n = 0, nums[0]
    for i in range(len(nums)):
        if max_n < nums[i]:
            max_n = nums[i]
            index = i
    return index


def findPeakElement1_3(nums: list[int]) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[index] < nums[i]:
            index = i
    return index


def findPeakElement2(nums: list[int]) -> int:
    """
        爬坡
    :param nums:
    :return:
    """
    n = len(nums)
    idx = random.randint(0, n - 1)

    def get(index: int):
        if index == -1 or index == n:
            return -math.inf
        return nums[index]

    while not get(idx - 1) < get(idx) > get(idx + 1):
        if get(idx) > get(idx + 1):  # 爬坡，向上，也可以向下
            idx = idx - 1
        else:
            idx = idx + 1
    return idx


def findPeakElement2_2(nums: list[int]) -> int:
    """
        爬坡
    :param nums:
    :return:
    """
    n = len(nums)
    idx = random.randint(0, n - 1)

    def get(index: int):
        if index == -1 or index == n:
            return -math.inf
        return nums[index]

    while not get(idx - 1) < get(idx) > get(idx + 1):
        if get(idx) < get(idx - 1):  # 爬坡，向上，也可以向下
            idx = idx - 1
        else:
            idx = idx + 1
    return idx


def findPeakElement3(nums: list[int]) -> int:
    """
        二分查找
    """
    nums = [-math.inf] + nums + [-math.inf]
    left, right = 1, len(nums) - 2
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid - 1
        if nums[mid] < nums[mid - 1]:  # 这里使用nums[mid-1]判断，也可使用nums[mid+1]判断
            right = mid - 1
        else:
            left = mid + 1
    return -1


def findPeakElement3_2(nums: list[int]) -> int:
    """
        二分查找
    """
    nums = [-math.inf] + nums + [-math.inf]
    left, right = 1, len(nums) - 2
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid - 1
        if nums[mid] < nums[mid + 1]:  # 这里使用nums[mid-1]判断，也可使用nums[mid+1]判断
            left = mid + 1
        else:
            right = mid - 1
    return -1


def findPeakElement3_3(nums: list[int]) -> int:
    """
        二分查找
        空间复杂度优化
    """
    n = len(nums)

    def get(idx: int):
        if idx == -1 or idx == n: return -math.inf
        return nums[idx]

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if get(mid - 1) < get(mid) > get(mid + 1):
            return mid
        if get(mid) < get(mid - 1):  # 这里使用nums[mid-1]判断，也可使用nums[mid+1]判断
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    # nums = [1, 2, 3, 1]
    nums = [1, 2, 1, 3, 5, 6, 4]
    # nums=[1]
    # ans = findPeakElement3(nums)
    # ans = findPeakElement2(nums)
    ans = findPeakElement3_3(nums)
    print(ans)
