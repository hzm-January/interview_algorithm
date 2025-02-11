def searchRange(nums: list[int], target: int) -> list[int]:  # 错误代码
    """
        错误原因：题目要求的数字一定在数组中，不能按照lower upper bound（数字可能不在数组中）
    :param nums:
    :param target:
    :return:
    """

    def lower_bound(nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def upper_bound(nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

    lower = lower_bound(nums, target)
    upper = upper_bound(nums, target) - 1
    # print(lower, upper)
    if lower < 0 or upper < 0 or lower > len(nums) - 1 or upper > len(nums) - 1:
        return [-1, -1]
    if nums[lower] != target or nums[upper] != target:
        return [-1, -1]
    return [lower, upper]


if __name__ == "__main__":
    # target, nums = 8, [5, 7, 7, 8, 8, 10]
    # target, nums = 6, [5, 7, 7, 8, 8, 10]
    target, nums = 0, []
    ans = searchRange(nums, target)
    print(ans)
