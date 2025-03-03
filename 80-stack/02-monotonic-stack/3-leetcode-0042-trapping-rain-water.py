from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
            单调栈
            当前位置储水量 ans[i] = min(left_great,right_great)-height[i]
        """
        n = len(height)
        stack = [0]
        sum = 0
        for i in range(1, n):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop()
                cur_height = height[cur]
                left = 0
                if stack:
                    left = stack[-1]
                left_height = height[left]
                right = i
                right_height = height[i]
                sum += max(min(left_height, right_height) - cur_height, 0) * (right - left - 1)
            stack.append(i)
        return sum

    def trap2(self, height: List[int]) -> int:
        """
            单调栈
            当前位置储水量 ans[i] = min(left_greatest,right_greatest)-height[i]
        """
        n = len(height)
        right = [0] * n
        stack = [0]
        for i in range(1, n):
            # 左遍历和右遍历只能有一个有等号，
            # 如果两个都不加等号会把凹区域积水统计两次，
            # 如果两个都加等号凹区域没有统计
            while stack and height[i] >= height[stack[-1]]: # 右边有多个连续同样高度的，只统计一次，剩余都为与当前高度相同的高度在后续求和时会变为0
                top = stack.pop()
                right[top] = i
            stack.append(i)

        left = [0] * n
        stack = [n - 1]
        for i in range(n - 2, -1, -1):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                left[top] = i
            stack.append(i)

        sum = 0
        for i in range(n):
            sum += ((max(min(height[left[i]], height[right[i]]), height[i]) - height[i])
                    * max((right[i] - left[i] - 1), 0))
        return sum


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [4, 2, 3]
    print(Solution().trap(height))
    print(Solution().trap2(height))
