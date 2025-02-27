from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        if n == 0:
            ans.append(newInterval)
            return ans
        index = n
        for i in range(n):
            if intervals[i][1] >= newInterval[0]:  # 第一个右端点大于 newInterval左端点
                index = i
                break
            ans.append(intervals[i])

        # Case 1 newInterval左端点比最后一个区间的右端点大，直接添加在末尾
        if index == n:
            if intervals[-1][1] == newInterval[0]:
                intervals[-1][1] = newInterval[1]
            else:
                intervals.append(newInterval)
            return intervals
        # Case 2 中间插入
        if intervals[index][0] > newInterval[1]:  # 插入 无重叠
            intervals[index:index] = [newInterval]
            return intervals
        if intervals[index][1] > newInterval[1] and index != 0:  # 被包含
            return intervals

        # 与 index 位置区间合并
        intervals[index] = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]
        ans.append(intervals[index])

        for i in range(index + 1, n):
            if ans[-1][1] >= intervals[i][0]:  # 有重叠
                # 合并
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])

        return ans


if __name__ == '__main__':
    # intervals, newInterval = [[1, 3], [6, 9]], [2, 5]
    # intervals, newInterval = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    # intervals, newInterval = [[1, 5]], [0, 3]
    # intervals, newInterval = [[2,5],[6,7],[8,9]], [0, 1]
    intervals, newInterval = [[3, 6], [9, 9], [11, 13], [14, 14], [16, 19], [20, 22], [23, 25], [30, 34], [41, 43],
                              [45, 49]], [29, 32]
    print(Solution().insert(intervals, newInterval))
