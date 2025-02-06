def lowerbound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)  # 左闭右开，有可能最后一个元素都小于target，所以最后一个元素必须能访问到。
    while left < right:
        mid = left + (right - left) // 2
        # 注意这里没有 nums[mid] == target，整个算法需要[left,right]夹住答案
        if nums[mid] >= target:  # 注意这一步，必须有等号
            right = mid
        else:
            left = mid + 1
    print(left, right)
    return left


def upperbound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)  # 左闭右开，有可能最后一个元素都小于target，所以最后一个元素必须能访问到。
    while left < right:
        mid = left + (right - left) // 2
        # 注意这里没有 nums[mid] == target，整个算法需要[left,right]夹住答案
        if nums[mid] > target:  # 注意这一步，没有等号
            right = mid
        else:
            left = mid + 1
    print(left, right)
    return left


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    # ans = lowerbound(nums, 5, 0, len(nums))
    # ans = upperbound(nums, 5, 0, len(nums))
    # ans = upperbound(nums, 10)
    ans = lowerbound(nums, 10)
    print(ans)
