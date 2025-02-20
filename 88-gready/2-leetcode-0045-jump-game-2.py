from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """ 贪心 通俗易懂版 """
        n = len(nums)
        if n == 1: return 0  # 如果数组元素个数为0，不用跳，因为初始就在数组的第一个节点，一定可以访问到数组所有节点（此时数组只有一个节点）
        cur_dist = 0  # 当前覆盖最远下标
        next_dist = 0  # 下一步覆盖最远下标
        ans = 0  # 结果
        for i in range(n):
            next_dist = max(next_dist, i + nums[i])
            if i == cur_dist:  # 以访问到当前覆盖最远下标
                cur_dist = next_dist  # 更新当前覆盖最远下标 = 下一次覆盖最远下标
                ans += 1  # 因为上一行更新了最远下标，所以跳一步
                # 下面两行不能删，测试样例 [2,3,1,1,4]只需要2步刚好可到末尾，
                # 如果删除下面两行，跳完第2步，最远访问到4，i==n-1的时候更新cur_dist=next_dist=4+4，ans+1，这一步不能更新，因为已经到终点了。
                # 如果删除下面两行，且测试样例刚好能跳到最后一个元素的情况，会在已经访问到最后一个元素的情况下，再多跳一步。这是错误的。
                if cur_dist >= n - 1:  # 如果当前已经覆盖了数组最后一个元素，不用跳，往前访问一定可以到达
                    break
        return ans

    def jump2(self, nums: List[int]) -> int:
        """ 贪心 统一处理版 只跳到倒数第二步 """
        n = len(nums)  # 该写法还避免了处理[0]，只有一个元素的特殊情况。因为遍历最远下标为n-1，这种特殊情况不进遍历逻辑，直接返回ans=0正确
        cur_dist = 0  # 当前覆盖最远下标
        next_dist = 0  # 下一步覆盖最远下标
        ans = 0  # 结果
        # 点睛之笔 跳到倒数第二步
        # 跳到倒数第二步，如果刚好当前最远是倒数第二步，还没有到结尾，又因为题目告知一定能跳完，那么ans一定要还要加1
        # 跳到倒数第二步，如果当前最远覆盖远于倒数第二步，则ans不用更新，一定能访问完。
        for i in range(n - 1):
            next_dist = max(next_dist, i + nums[i])
            if i == cur_dist:  # 以访问到当前覆盖最远下标
                cur_dist = next_dist  # 更新当前覆盖最远下标 = 下一次覆盖最远下标
                ans += 1  # 因为上一行更新了最远下标，所以跳一步
        return ans

    def jump3(self, nums: List[int]) -> int:
        """ 贪心 逻辑通顺版 """
        n = len(nums)
        if n == 1: return 0
        cur_dist = nums[0]
        ans = 0
        i = 0
        while i <= n - 1:
            if cur_dist >= n - 1:  # 当前覆盖范围已经包含了最后一个元素
                ans += 1  # 再跳一步到最后一个元素
                break  # 结束

            # 当前覆盖范围还不能覆盖到最后一个元素
            # 寻找当前覆盖范围中，下一步能覆盖的最远范围
            next_dist_i = i
            next_dist = cur_dist
            for j in range(i + 1, min(cur_dist + 1, n)):
                if nums[j] + j > next_dist:
                    next_dist = nums[j] + j
                    next_dist_i = j
            # 更新最远覆盖范围，和该覆盖范围起始遍历位置
            if next_dist == cur_dist:  # 当前覆盖范围内，最大下一步覆盖范围 小于等于 当前覆盖范围远
                i = cur_dist  # 更新下标到当前覆盖范围最远处
                cur_dist = cur_dist + nums[cur_dist]  # 更新下一步覆盖范围为当前覆盖范围最远处+该处能跳的最远距离，上面已经处理过cur_dist>=n-1，这里不会越界
            else:  # 当前覆盖范围内，最大下一步覆盖范围 大于 当前覆盖范围
                i = next_dist_i  # 更新下标到下一步覆盖范围的起点
                cur_dist = next_dist  # 更新下一步覆盖为新找到的最远覆盖范围

            # 例：[3,1,9,5,4]，上一次覆盖范围是[3,1,9,5]，该覆盖范围内最远覆盖范围为[位置2的9,.....,位置11]，
            # 那么这里的ans+=1就是跳到位置2处，位置2是更新完的最远覆盖范围的起跳位置
            # 例：[1,2]，上一次覆盖范围是[1,2]，该覆盖范围内最远覆盖范围为[位置1],位置2,位置3]，
            # 那么这里的ans+=1就是跳到位置1处，位置1是更新完的最远覆盖范围的起跳位置
            ans += 1  # 跳到当前覆盖范围的起始遍历位置，即上一次最远覆盖范围内最远覆盖范围的起跳位置
        return ans

    def jump4(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        for i in range(n):
            for j in range(0, i + 1):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]


if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]
    # nums = [2, 3, 0, 1, 4]
    # nums = [0]
    # nums=[2,1]
    # nums=[1,2]
    # nums=[2,3,1]
    nums = [1, 1, 0]
    # print(Solution().jump(nums))
    # print(Solution().jump3(nums))
    print(Solution().jump4(nums))
