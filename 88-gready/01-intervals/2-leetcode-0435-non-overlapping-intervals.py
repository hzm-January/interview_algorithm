from typing import List

"""
    
    贪心：让原始多个区间尽可能重叠
    排序让相邻区间尽可能凑在一起，在遍历的时候，容易判断区间是否重叠
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """ 贪心思路1：优先取左端点较大者 """
        n = len(intervals)
        intervals.sort(key=lambda x: (-x[0], x[1]))
        print(intervals)
        ans = 1
        pre_left = intervals[0][0]
        for i in range(1, n):
            if intervals[i][1] <= pre_left:
                ans += 1
                pre_left = intervals[i][0]
        return n - ans

    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        """ 贪心思路2： 优先取右端点较小者 """
        n = len(intervals)
        intervals.sort(key=lambda x: (x[1], -x[0]))
        print(intervals)
        pre_right = intervals[0][1]
        ans = 1
        for i in range(1, n):
            if intervals[i][0] >= pre_right:
                ans += 1
                pre_right = intervals[i][1]
        return n - ans

    def eraseOverlapIntervals3(self, intervals: List[List[int]]) -> int:
        """ 左端点从大到小 """
        n = len(intervals)
        intervals.sort(key=lambda x: -x[0])
        print(intervals)
        ans = 1
        for i in range(1, n):
            if intervals[i][1] <= intervals[i - 1][0]:
                ans += 1
            else:
                intervals[i][0] = max(intervals[i][0], intervals[i - 1][0])

        return n - ans

    def eraseOverlapIntervals3_2(self, intervals: List[List[int]]) -> int:
        """ 左端点从大到小 直接统计区间个数  """
        n = len(intervals)
        intervals.sort(key=lambda x: -x[0])
        print(intervals)
        ans = 0  # 区间个数
        for i in range(1, n):
            if intervals[i][1] > intervals[i - 1][0]:
                ans += 1
                intervals[i][0] = max(intervals[i][0], intervals[i - 1][0])
        return ans

    def eraseOverlapIntervals4(self, intervals: List[List[int]]) -> int:
        """ 卡尔版 左端点从小到大  """
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        ans = 1  # 区间个数
        for i in range(1, n):
            if intervals[i][0] <= intervals[i - 1][1]:  # 有重叠
                intervals[i][0] = max(intervals[i][0], intervals[i - 1][0])
            else:  # 无重叠
                ans += 1
        return n - ans


if __name__ == '__main__':
    # intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
    print(Solution().eraseOverlapIntervals(intervals))
    print(Solution().eraseOverlapIntervals2(intervals))
    print(Solution().eraseOverlapIntervals3(intervals))
