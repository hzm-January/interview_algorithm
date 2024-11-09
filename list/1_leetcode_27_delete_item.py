class Solution:
    def removeElement(self, nums, val: int) -> int:
        p, q = 0, 0
        while q < len(nums):
            if nums[q] != val:
                nums[p] = nums[q]
                p += 1
            q += 1
        return p


if __name__ == '__main__':
    solution = Solution()
    # case 1
    # nums = [3, 2, 2, 3]
    # val = 3
    # case 2
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    n = solution.removeElement(nums, val)
    print(n)
    print(' '.join(map(str, nums[:n])))
