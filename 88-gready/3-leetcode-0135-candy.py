from typing import List

"""
    分糖果 
    思路：先确定一个方向，再确定另一个方向，前后两次遍历取较大
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 从前到后
        candyF2E = [1]
        for i in range(1, len(ratings)):
            curCandy = 1
            if ratings[i] > ratings[i - 1]:
                curCandy += candyF2E[-1]
            candyF2E.append(curCandy)
        print(candyF2E)
        # 从后到前
        sum = candyF2E[-1]
        for i in range(len(ratings) - 2, -1, -1):
            curCandy = 1
            if ratings[i] > ratings[i + 1]:
                curCandy += candyF2E[i + 1]
            candyF2E[i] = max(candyF2E[i], curCandy)
            sum += candyF2E[i]
        print(candyF2E)

        return sum
    def candy2(self, ratings: List[int]) -> int:
        # 从前到后
        candyF2E = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candyF2E[i] = candyF2E[i-1]+1
        print(candyF2E)
        # 从后到前
        sum = candyF2E[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candyF2E[i] = max(candyF2E[i], candyF2E[i+1]+1)
            sum += candyF2E[i]
        print(candyF2E)

        return sum


if __name__ == '__main__':
    # ratings = [1, 0, 2]
    ratings = [1, 2, 2]
    # print(Solution().candy(ratings))
    print(Solution().candy2(ratings))
