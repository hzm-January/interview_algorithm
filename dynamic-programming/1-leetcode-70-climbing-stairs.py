class Solution:
    def climbStairs(self, n: int) -> int:
        p, q, r = 0, 0, 1
        for i in range(1, n + 1):
            p = q
            q = r
            r = p + q
        return r


if __name__ == '__main__':
    s = Solution()
    k = s.climbStairs(2)
    print(k)
