def canJump(nums: list[int]) -> bool:
    # if len(nums) == 1: return True
    i, max_next = 0, nums[0]
    while i <= max_next and i < len(nums):
        max_next = max(max_next, i + nums[i])
        i += 1
    return i >= len(nums)


def canJump2(nums: list[int]) -> bool:  # 逻辑优化
    # if len(nums) == 1: return True
    i, max_next = 0, 0
    while i <= max_next:
        max_next = max(max_next, i + nums[i])
        if max_next >= len(nums) - 1:
            return True
        i += 1
    return False


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    # nums = [0]
    # nums = [2, 0, 0]
    # nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
    # flag = canJump(nums)
    flag = canJump2(nums)
    print(flag)
