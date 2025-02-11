def removeDuplicates(nums: list[int]) -> int:
    p, q = 2, 2
    while q < len(nums):
        if nums[q] != nums[p-2]:
            nums[p] = nums[q]
            p += 1
        q += 1
    print(nums)
    return p


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 5, 6, 6, 6, 6]
    removeDuplicates(nums)
