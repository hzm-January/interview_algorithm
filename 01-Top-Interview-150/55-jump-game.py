def canJump(nums: list[int]) -> bool: # 错误版本
    # if len(nums) == 1: return True
    i, prev = 0, 0
    while i < len(nums) - 1:
        max_next = i + nums[i]
        for j in range(i, min(i + nums[i] + 1, len(nums))):
            max_next = max(max_next, j + nums[j])
        i = max_next
        if prev == i:
            break
        prev = i

    return i >= len(nums) - 1


if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    # nums = [0]
    # nums = [2, 0, 0]
    nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
    flag = canJump(nums)
    print(flag)
