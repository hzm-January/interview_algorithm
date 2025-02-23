from collections import deque
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        # 求中间部分最大子数组和
        cur_sum = nums[0]  # 当前累计和
        max_sum = nums[0]  # 最大子数组和
        leftMax = [0] * n  # 最大前缀和
        leftMax[0] = nums[0]
        leftSum = nums[0]  # 前缀和
        for i in range(1, n):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
            leftSum += nums[i]
            leftMax[i] = max(leftMax[i - 1], leftSum)
        # 求两边最大子数组和
        # 从右往左，固定后缀子数组，寻找最大前缀子数组
        rightSum = 0
        for i in range(n - 1, 0, -1):
            rightSum += nums[i]
            max_sum = max(max_sum, rightSum + leftMax[i - 1])
        return max_sum

    def maxSubarraySumCircular2(self, nums: List[int]) -> int:
        """ 取反 """
        n = len(nums)
        pre_min, min_ans = nums[0], nums[0]
        pre_max, max_ans = nums[0], nums[0]
        sum = nums[0]
        for i in range(1, n):
            pre_min = min(nums[i], nums[i] + pre_min)
            pre_max = max(nums[i], nums[i] + pre_max)
            min_ans = max(min_ans, pre_min)
            max_ans = max(max_ans, pre_max)
            sum += nums[i]
        if max_ans < 0:
            return max_ans
        else:
            return max(max_ans, sum - min_ans)

    def maxSubarraySumCircular3(self, nums: List[int]) -> int:
        """ 前缀和 + 单调栈 """
        n = len(nums)
        # 前缀和
        sum = [0] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            sum[i] = sum[i - 1] + nums[(i - 1) % n]
        #
        q = deque()  # 单调栈，q[0]是窗口内的最小值
        q.append(0)
        ans = nums[0]
        for i in range(1, 2 * n + 1):
            # i-q[0]==n合法，例如 n+1-1==n 时，sum[n+1]表示0~n的和，nums[n]==nums[0]，sum[1]表示nums[0]
            # 则sum[n+1]-sum[1]表示的是从nums中从1到n的和，nums[n]==nums[0]，没有重复元素
            while q and i - q[0] > n:
                q.popleft()  # 超过窗口长度，队首出队
            ans = max(ans, sum[i] - sum[q[0]])  # 更新结果
            while q and sum[q[-1]] > sum[i]:  # 更新单调栈
                q.pop()
            q.append(i)
        return ans

    def maxSubarraySumCircular4(self, nums: List[int]) -> int:
        """
            前缀和 + 单调栈
            省略前缀和的单独计算
        """
        n = len(nums)
        # 前缀和
        pre = nums[0]  # 前缀和
        q = deque()  # 单调栈，q[0]是窗口内的最小值
        q.append((0, nums[0]))
        ans = nums[0]
        for i in range(1, 2 * n + 1):
            # i-q[0]==n合法，例如 n+1-1==n 时，sum[n+1]表示0~n的和，nums[n]==nums[0]，sum[1]表示nums[0]
            # 则sum[n+1]-sum[1]表示的是从nums中从1到n的和，nums[n]==nums[0]，没有重复元素
            while q and i - q[0][0] > n:
                q.popleft()  # 超过窗口长度，队首出队
            pre += nums[(i - 1) % n]  # 更新前缀和
            ans = max(ans, pre - q[0][1])  # 更新结果
            while q and q[-1][1] > pre:  # 更新单调栈
                q.pop()
            q.append((i, pre))

        return ans


if __name__ == '__main__':
    # nums = [1, -2, 3, -2]
    # nums = [5, -3, 5]
    nums = [-3, -2, -3]
    print(Solution().maxSubarraySumCircular(nums))
    # print(Solution().maxSubarraySumCircular2(nums))
    # print(Solution().maxSubarraySumCircular3(nums))
    print(Solution().maxSubarraySumCircular4(nums))
