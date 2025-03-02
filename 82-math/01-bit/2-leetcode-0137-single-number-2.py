from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cur_bit_sum = sum([(num << i) for num in nums])
            if cur_bit_sum % 3:
                if i == 31:  # python中最高位是符号位，要单独处理
                    ans -= (1 << i) # 例如：1010-10000
                else:
                    ans |= (1 << i)  # 将第i位赋值为1
        return ans
