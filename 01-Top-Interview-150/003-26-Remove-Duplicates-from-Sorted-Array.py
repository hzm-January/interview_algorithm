def removeDuplicates_1(nums: list[int]) -> int:
    """ single pointer solution """
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    print(nums)
    return j


def removeDuplicates(nums: list[int]) -> int:
    """ double pointer solution """
    if len(nums) == 1: return 1
    p, q = 1, 1
    while q < len(nums):
        if nums[p - 1] != nums[q]:
            nums[p] = nums[q]
            p += 1
        q += 1

    print(nums)
    return p


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 3, 3]
    # removeDuplicates(nums)
    removeDuplicates_1(nums)
