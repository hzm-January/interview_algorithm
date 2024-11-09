class Solution:
    def rob(self, nums) -> int:
        p, q, r = 0, 0, 0
        for i in range(0, len(nums)):
            r = max(p + nums[i], q)
            p = q
            q = r
        return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([2, 7, 9, 3, 1]))
