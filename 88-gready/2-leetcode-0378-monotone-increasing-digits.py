class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        """ 暴力解法  超时 """

        def check(num):
            pre = 9
            while num:
                remainder = num % 10
                if remainder > pre:
                    return False
                num //= 10
                pre = remainder
            return True

        tmp = n
        while tmp >= 0:
            if check(tmp):
                return tmp
            tmp -= 1

    def monotoneIncreasingDigits2(self, n: int) -> int:
        """ 贪心 数字处理 """
        ns = [int(c) for c in str(n)]
        flag = len(ns)
        for i in range(len(ns) - 1, 0, -1):
            if ns[i - 1] > ns[i]:
                ns[i - 1] -= 1
                flag = i
        if flag < len(ns): ns[flag:] = [9] * (len(ns) - flag)
        return int(''.join(map(str, ns)))

    def monotoneIncreasingDigits3(self, n: int) -> int:
        """ 贪心 字符数组处理 """
        ns = [c for c in str(n)]
        # print(ns)
        flag = len(ns)
        for i in range(len(ns) - 1, 0, -1):
            if int(ns[i - 1]) > int(ns[i]):
                ns[i - 1] = str(int(ns[i - 1]) - 1)
                flag = i
        if flag < len(ns): ns[flag:] = ['9'] * (len(ns) - flag)
        return int(''.join(ns))


if __name__ == '__main__':
    print(Solution().monotoneIncreasingDigits(123))
    print(Solution().monotoneIncreasingDigits(332))
    print(Solution().monotoneIncreasingDigits2(332))
