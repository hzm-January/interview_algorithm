from typing import List

"""
    注意：题目已知区间是左端点从小到大排列，后续的所有处理都按照左端点有序进行，不能参考右端点有序处理。例如：寻找插入点的时候，必须从后往前遍历，寻找第一个右端点<新区间左端点的区间
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        if n == 0:
            ans.append(newInterval)
            return ans
        # 从后向前遍历，找到第一个右端点大于新插入区间的左端点的区间，index指向该区间的下一个区间，准备合并
        # 必须从后往前遍历，找第一个右端点<新区间左端点，这样找到的区间，后续不需要处理左端点，因为左端点已有序，再加入一定与前一个区间无重叠
        # 假设从前往后遍历，找第一个左端点>新区间右端点，这样找到的区间，不但要处理右端点，还要处理左端点，因为不知道新加入的左端点与前一个区间是否有重叠
        index = n
        for i in range(n-1,-1,-1):
            if intervals[i][1] < newInterval[0]:
                break
            index = i

        # 将index之前的区间全部添加到结果集中
        for i in range(index):
            ans.append(intervals[i])

        # Case 1 newInterval左端点比最后一个区间的右端点大，直接添加在末尾
        if index == n:
            intervals.append(newInterval)
            return intervals
        # Case 2 index=0 第一个区间
        # Case 2 中间插入
        if intervals[index][0] > newInterval[1]:  # 插入 无重叠
            intervals[index:index] = [newInterval]
            return intervals
        if intervals[index][1] >= newInterval[1] and intervals[index][0]<= newInterval[0]:  # 被包含
            return intervals

        # 与 index 位置区间合并
        intervals[index] = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]
        ans.append(intervals[index])

        for i in range(index + 1, n): # 往后遍历，更新右端点
            if ans[-1][1] >= intervals[i][0]:  # 有重叠
                # 合并
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])

        return ans


if __name__ == '__main__':
    intervals, newInterval = [[1, 3], [6, 9]], [2, 5]
    # intervals, newInterval = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    # intervals, newInterval = [[1, 5]], [0, 3]
    # intervals, newInterval = [[2,5],[6,7],[8,9]], [0, 1]
    # intervals, newInterval = [[3, 6], [9, 9], [11, 13], [14, 14], [16, 19], [20, 22], [23, 25], [30, 34], [41, 43],
    #                           [45, 49]], [29, 32]
    print(Solution().insert(intervals, newInterval))
