def removeDuplicates_1(nums: list[int]) -> int:
    """ double pointer solution """
    """
        数组中相邻两个值比较大小，内存读取友好
        考虑一种情况：第一个数值到第10000个数值都相同，接下来第一个数字和第10001个数值比较，内存读取可能并不友好。
    """
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
    nums = [1, 1, 1, 2, 2, 3, 3, 3]
    # removeDuplicates(nums)
    removeDuplicates_1(nums)
