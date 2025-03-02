class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """ 大整数 """
        p, q = len(a) - 1, len(b) - 1
        carry = 0
        ans = []
        while p >= 0 and q >= 0:
            sum = int(a[p]) + int(b[q]) + carry
            cur = sum % 2
            ans.insert(0, str(cur))
            carry = sum // 2
            p -= 1
            q -= 1
        while p >= 0:
            sum = int(a[p]) + carry
            cur = sum % 2
            ans.insert(0, str(cur))
            carry = sum // 2
            p -= 1
        while q >= 0:
            sum = int(b[q]) + carry
            cur = sum % 2
            ans.insert(0, str(cur))
            carry = sum // 2
            q -= 1
        if carry: ans.insert(0, str(carry))
        return ''.join(ans)

    def addBinary2(self, a: str, b: str) -> str:
        """ 大整数 写法优化 """
        if len(a) < len(b):
            a = '0'*(len(b)-len(a)) + a
        if len(b) < len(a):
            b = '0'*(len(a)-len(b)) + b
        p, q = len(a) - 1, len(b) - 1
        carry = 0
        ans = ''
        while p >= 0 and q >= 0:
            sum = int(a[p]) + int(b[q]) + carry
            cur = sum % 2
            ans = str(cur) + ans
            carry = sum // 2
            p -= 1
            q -= 1
        if carry: ans = str(carry) + ans
        return ans


if __name__ == '__main__':
    a, b = '11', '1'
    # a, b = '1010', '1011'
    print(Solution().addBinary(a, b))
    print(Solution().addBinary2(a, b))
