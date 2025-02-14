def twoSum(nums: list[int], target: int) -> list[int]:
    hash = {}
    for i in range(len(nums)):
        if target - nums[i] in hash:
            return [hash[target - nums[i]], i]
        hash[nums[i]] = i
    print(hash)
    return [-1, -1]


if __name__ == '__main__':
    # nums, target = [2, 7, 11, 15], 9
    # nums, target = [3, 2, 4], 6
    nums, target = [3, 3], 6
    ans = twoSum(nums, target)
    print(ans)
