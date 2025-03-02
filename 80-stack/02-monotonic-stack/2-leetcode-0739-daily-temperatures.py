from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ 单调栈 """
        stack = [(0, temperatures[0])]
        n = len(temperatures)
        ans = [0] * n
        for j in range(1, n):
            temp = temperatures[j]
            while stack and temp > stack[-1][1]:
                i, top = stack.pop()
                ans[i] = j - i
            stack.append((j, temp))
        return ans

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        """ 单调栈 优化 """
        stack = [0]
        n = len(temperatures)
        ans = [0] * n
        for j in range(1, n):
            while stack and temperatures[j] > temperatures[stack[-1]]:
                i = stack.pop()
                ans[i] = j - i
            stack.append(j)
        return ans


if __name__ == '__main__':
    # temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # temperatures = [30, 40, 50, 60]
    temperatures = [30, 60, 90]
    print(Solution().dailyTemperatures(temperatures))
    print(Solution().dailyTemperatures2(temperatures))
