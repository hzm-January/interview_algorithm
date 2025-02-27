from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        pre = 0
        index = n
        ans = []
        for i in range(n):
            if intervals[i][1] > newInterval[0]:  # 第一个右端点大于 newInterval左端点
                index = i
                break
            ans.append(intervals[i])

        # Case 1 newInterval左端点比最后一个区间的右端点大，直接添加在末尾
        if index == n:
            intervals.append(newInterval)
            return intervals
        # Case 2 中间插入
        if intervals[index][1] > newInterval[1]:  # 被包含
            return intervals
        if intervals[index][0] > newInterval[1]:  # 插入 无重叠
            intervals[index - 1:index - 1] = [newInterval]
            return intervals

        # 与 index 位置区间合并
        intervals[index] = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]
        ans.append(intervals[index])

        for i in range(index + 1, n):
            if ans[-1][1] > intervals[i][0]:  # 有重叠
                # 合并
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])

        return ans


if __name__ == '__main__':
    # intervals = [[1, 3], [6, 9]]
    # newInterval = [2, 5]
    intervals, newInterval = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    print(Solution().insert(intervals, newInterval))
