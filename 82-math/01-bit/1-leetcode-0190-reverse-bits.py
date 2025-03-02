class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + ((n >> i) & 1)
        return res


if __name__ == '__main__':
    s = Solution()
    s.reverseBits(1)
    s.reverseBits(2)
