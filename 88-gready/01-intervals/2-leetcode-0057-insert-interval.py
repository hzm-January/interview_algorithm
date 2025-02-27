from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        pre = 0
        index = -1
        for i in range(n - 1, -1, -1):
            if intervals[i][1] < newInterval[0]:  # 第一个右端点小于 newInterval左端点
                index = i
                break
        if index == n - 1:
            intervals.append(newInterval)
            return intervals

        # 与 index+1 位置区间合并
        index = index + 1
        intervals[index] = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]
        i = index
        while i < n:
            if intervals[i-1][1] > intervals[i][0]:
                # 合并
                intervals[i - 1][1]=max(intervals[i-1][1], intervals[i][1])


