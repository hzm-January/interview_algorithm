from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0,temperatures[0])]
        n = len(temperatures)
        ans = [0] * n
        for j in range(1, n):
            temp = temperatures[j]
            while stack and temp > stack[-1][1]:
                i, top = stack.pop()
                ans[i]=j-i
            stack.append((j,temp))
        return ans

if __name__ == '__main__':
    # temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # temperatures = [30, 40, 50, 60]
    temperatures = [30, 60, 90]
    print(Solution().dailyTemperatures(temperatures))