def searchInsert(nums: list[int], target: int) -> int:
    """
        二分查找 左闭右开
        时间复杂度：O(logn)
        空间复杂度：O(1)
    """
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def searchInsert2(nums: list[int], target: int) -> int:
    """
        二分查找 左闭右开
        时间复杂度：O(logn)
        空间复杂度：O(1)
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    # target, nums = 5, [1, 3, 5, 6]
    target, nums = 2, [1, 3, 5, 6]
    # ans = searchInsert(nums, target)
    ans = searchInsert2(nums, target)
    print(ans)
