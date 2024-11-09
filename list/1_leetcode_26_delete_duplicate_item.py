class Solution:
    def removeDuplicates(self, nums) -> int:
        p, q = 0, 1
        while q < len(nums):
            if nums[q] != nums[p]:
                p += 1
                nums[p] = nums[q]
            q += 1
        return p + 1


if __name__ == '__main__':
    solution = Solution()
    # case 1
    # nums = [1, 1, 2]
    # case 2
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    # case 3
    # nums = [0, 1]

    # case 4
    nums = [0]
    n = solution.removeDuplicates(nums)
    print(n)
    print(' '.join(map(str, nums)))
