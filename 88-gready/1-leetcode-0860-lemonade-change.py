from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
            贪心
            局部最优：尽可能使用更大的面额找零
        """
        balance = {}
        denominations = [20, 10, 5]
        for bill in bills:
            change = bill - 5
            # 找零
            if change > 0:
                for denom in denominations:
                    cnt = change // denom
                    if cnt == 0: continue
                    remain = balance.get(denom, 0)
                    if remain < cnt and denom == 5: return False  # 找不开
                    if remain == 0:
                        continue
                    if remain < cnt:
                        balance[denom] = 0
                        change -= denom * remain
                        continue
                    balance[denom] = remain - cnt
                    # if balance[denom] < 0: return False  # 找不开
                    change -= denom * cnt
            # 收钱
            balance[bill] = balance.get(bill, 0) + 1
            print(balance)
        return balance.get(5, 0) >= 0

    def lemonadeChange2(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for bill in bills:
            change = bill - 5
            if change > 0:
                twenty_need = change // 20
                if twenty_need > 0 and twenty > 0:
                    min_cnt = min(twenty_need, twenty)
                    twenty -= min_cnt
                    change -= 20 * min_cnt
                if change == 0: continue
                ten_need = change // 10
                if ten_need > 0 and ten > 0:
                    min_cnt = min(ten_need, ten)
                    ten -= min_cnt
                    change -= 10 * min_cnt
                if change == 0: continue
                five_need = change // 5
                if five<five_need: return False
                if five_need > 0 and five > 0:
                    min_cnt = min(five_need, five)
                    five -= min_cnt
                    change -= 5 * min_cnt
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
            elif bill == 20:
                twenty += 1
        return True

    def lemonadeChange3(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for bill in bills:
            if bill == 5:
                five+=1
            elif bill == 10:
                if five==0: return False
                five-=1
                ten+=1
            elif bill == 20:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                    twenty+=1
                elif five>3:
                    five-=3
                    twenty+=1
                else:
                    return False
        return True



if __name__ == '__main__':
    # nums = [5, 5, 5, 10, 20]
    nums = [5, 5, 10, 10, 20]
    # nums = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]
    # print(Solution().lemonadeChange(nums))
    # print(Solution().lemonadeChange2(nums))
    print(Solution().lemonadeChange3(nums))
