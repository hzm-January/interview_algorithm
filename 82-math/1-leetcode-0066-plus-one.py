from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        for i in range(n - 1, -1, -1):
            cur = digits[i] + carry
            if i == n - 1: cur += 1
            digits[i] = cur % 10
            carry = cur // 10
        if carry != 0:
            digits.insert(0, carry)
        return digits


if __name__ == '__main__':
    # digits = [1, 2, 3]
    # digits = [-1]
    # digits = [4, 3, 2, 1]
    digits=[9]
    print(Solution().plusOne(digits))
