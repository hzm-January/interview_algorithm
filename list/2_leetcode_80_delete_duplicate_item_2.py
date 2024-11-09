class Solution:
    # def removeDuplicates(self, nums) -> int:
    #     p, q, c = 0, 1, 1
    #     while q < len(nums):
    #         if nums[q] != nums[p]:
    #             p += 1
    #             nums[p] = nums[q]
    #             c = 1
    #         elif c < 2:
    #             p += 1
    #             nums[p] = nums[q]
    #             c += 1
    #         q += 1
    #     return p + 1

    def removeDuplicates(self, nums) -> int:
        if len(nums) <= 2: return len(nums)
        p, q = 2, 2
        while q < len(nums):
            if nums[q] != nums[p - 2]:
                nums[p] = nums[q]
                p += 1
            q += 1
        return p


if __name__ == '__main__':
    solution = Solution()
    # case 1
    # nums = [1, 1, 1, 2, 2, 3]
    # case 2
    # nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

    # case 3
    # nums = [0, 1]

    # case 4
    nums = [0]
    n = solution.removeDuplicates(nums)
    print(n)
    print(' '.join(map(str, nums[:n])))
