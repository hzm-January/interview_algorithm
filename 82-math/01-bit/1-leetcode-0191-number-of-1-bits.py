class Solution:
    def hammingWeight(self, n: int) -> int:
        """ 库函数 """
        return bin(n).count('1')

    def hammingWeight2(self, n: int) -> int:
        """ 依次取出二进制所有位 """
        ans = 0
        while n:
            ans += n & 1
            n = n >> 1
        return ans

    def hammingWeight3(self, n: int) -> int:
        """ 循环检查 二进制位 """
        ans = 0
        for i in range(32):
            if n & (1 << i):
                ans += 1
        return ans

    def hammingWeight4(self, n: int) -> int:
        cnt = 0
        while n:
            n&=n-1
            cnt+=1
        return cnt


