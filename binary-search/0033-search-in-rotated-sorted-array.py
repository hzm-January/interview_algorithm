import math


def search(nums: list[int], target: int) -> int:
    n = len(nums)
    ans = nums.index(min(nums))  # 时间复杂度为O(n)，不满足题目要求
    # 查找target
    left, right = ans, ans + n
    while left <= right:
        mid = (left + (right - left) // 2)
        if nums[mid % n] == target:
            return mid % n
        if nums[mid % n] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def search2(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]: # 左半边有序，注意这里的等号
            if nums[left]<=target<nums[mid]: # target在左半边有序子数组中，注意这里的等号
                right = mid - 1
            else: # target不在左半边有序子数组中，所以在右半边找
                left = mid + 1
        else: # 右半边有序
            if nums[mid]<target<=nums[right]: # target 在右半边有序子数组中，注意这里的等号
                left = mid + 1
            else: # target 不在右半边有序子数组中，所以在左半边找
                right = mid - 1
    return -1


if __name__ == "__main__":
    # target, nums = 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # target, nums = 7, [4, 5, 6, 7, 0, 1, 2]
    # target, nums = 0, [1]
    target, nums = 2, [3, 4, 5, 6, 1, 2]
    # ans = search(nums, target)
    ans = search2(nums, target)
    print(ans)
