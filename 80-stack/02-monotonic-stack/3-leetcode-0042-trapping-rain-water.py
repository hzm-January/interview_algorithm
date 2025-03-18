from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
            单调栈
            当前位置储水量 ans[i] = min(left_great,right_great)-height[i]

            1 从栈低到栈顶，递减
            2 元素左侧第一个比自己大的元素即为栈中自己的前一个元素
            3 元素右侧第一个比自己大的元素即为当前想要加入栈中的元素
            4 当前能接雨水量=max(min(左第一个高-右第一个高)-当前高度, 0  )*宽度

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
                # 必须有max(..,0)，考虑一种情况：一座山，当前处理节点为左边坡上一点，该点有高度，且左侧比自己高的高度不存在，右侧比自己高的元素存在
                # 按照当前逻辑代码，min(leftHeight=0, rightHeight=height[j])-curHeight = 0-curHeight <0
                sum += max(min(left_height, right_height) - cur_height, 0) * (right - left - 1)
            stack.append(i)
        return sum

    def trap2(self, height: List[int]) -> int:
        """
            单调栈
            当前位置储水量 ans[i] = min(left_greatest,right_greatest)-height[i]

            1 正序遍历，找到后一个较高柱子
            2 逆序遍历，找到前一个较高柱子
            3 遍历：当前能接雨水量=(min(左第一个高-右第一个高)-当前高度)*宽度
            4 累加结果

            注意：二刷发现一个易错点：单调栈，逻辑中，出栈时处理出栈节点，而不是出栈时处理当前节点。
                例如：统计右第一个高时，从1到n-1遍历，栈顶节点j<当前节点i时，弹出栈顶节点j，
                        此时，处理的是栈顶节点j，j的右侧第一个比自己高的节点是当前节点i。
                    统计左第一个高时，从n-2到0遍历，当前节点i>栈顶节点j，弹出栈顶节点j，
                        此时，处理的是栈顶节点j，j的左侧第一个比自己高的节点是当前节点i。
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
