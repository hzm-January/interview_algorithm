def search(nums: list[int], target: int) -> int:
    """
        左闭右闭
    """
    left, right = 0, len(nums) - 1  # 右闭，所以right=len(arr)-1
    while left <= right:  # 右闭，所以right必须能访问到
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1  # 右闭，因为已经判断mid>target，所以右边界不能是mid，必须是mid-1
    return -1


def search2(nums: list[int], target: int) -> int:
    """
        左闭右开
    """
    left, right = 0, len(nums)  # 右开，所以定义为len(nums)，下一轮右开区间一定不包含mid
    while left < right: # 右开，所以right不能被访问到
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid # 右开，并且已经判断了nums[mid]>target，所以下一轮右开区间一定不包含mid
    return -1


if __name__ == "__main__":
    nl = [-1, 0, 3, 5, 9, 12]
    # ans = search(nl, 9)
    ans = search(nl, 2)
    print(ans)
