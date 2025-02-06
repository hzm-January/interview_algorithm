def lowerbound(nums: list[int], target: int, left: int, right: int) -> int:
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target: # 注意这一步，必须有等号
            right = mid
        else:
            left = mid + 1
    return left

def upperbound(nums: list[int], target: int, left: int, right: int) -> int:
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target: # 注意这一步，没有等号
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    # ans = lowerbound(nums, 5, 0, len(nums))
    ans = upperbound(nums, 5, 0, len(nums))
    print(ans)
