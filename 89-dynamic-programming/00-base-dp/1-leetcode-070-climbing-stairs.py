class Solution:
    def climbStairs(self, n: int) -> int:
        p, q, r = 0, 0, 1
        for i in range(1, n + 1):
            p = q
            q = r
            r = p + q
        return r

    def climbStairs2(self, n: int) -> int:
        if n < 3: return n
        p, q, r = 1, 2, 3
        for i in range(3, n + 1):
            r = p + q
            p = q
            q = r
        return r
    def climbStairs3(self, n: int) -> int:
        if n < 3: return n
        p, q, r = 0, 1, 2
        for i in range(3, n + 1):
            p = q
            q = r
            r = p + q
        return r

if __name__ == '__main__':
    s = Solution()
    # k = s.climbStairs(2)
    k = s.climbStairs2(2)
    print(k)
