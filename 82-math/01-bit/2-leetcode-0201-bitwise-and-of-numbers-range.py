class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
            位移
            1 找到公共前缀，右移 n 位
                00001001->0000100->000010->00001
                00001100->0000110->000011->00001
            2 左移 n 位
                00001000<-0000100<-000010<-00001
        """
        cnt = 0
        while left != right:  # 右移cnt次后，相等
            left >>= 1
            right >>= 1
            cnt += 1
        while cnt > 0:  # 左移cnt次
            left <<= 1
            cnt -= 1
        return left

    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1  # 将right最低一位1置为0
        return right


if __name__ == '__main__':
    print(Solution().rangeBitwiseAnd(5, 7))
    print(Solution().rangeBitwiseAnd2(5, 7))
