from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: (-x[0], x[1]))
        ans = [intervals[0]]
        for i in range(1, n):
            top = ans[-1]
            if intervals[i][1] < ans[-1][0]:  # 没有重合，直接添加
                ans.append(intervals[i])
            else: # 有重合
                while top[0] >= intervals[i][0] and top[1] <= intervals[i][1]:  # 重合，并且包含
                    ans.pop()
                    if not ans: break
                    top = ans[-1]
                if intervals[i][1] >= top[0]:  # 有重合，但不是包含
                    if ans: ans.pop()
                    ans.append([min(intervals[i][0], top[0]), max(intervals[i][1], top[1])])  # 合并
                else:  # 没有重合，直接添加
                    ans.append(intervals[i])
        return ans

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] <= ans[-1][1]: # 当前区间与上一个区间 有重叠
                # 因为左端点从小到大排序，所以先添加区间的左端点一定小于等于后添加区间的左端点，所以不需处理左端点
                ans[-1][1] = max(ans[-1][1], intervals[i][1]) # 在已添加上一个区间的右端点上，合并区间
            else: # 当前区间与上一个区间 没有重叠
                ans.append(intervals[i])
        return ans

    def merge3(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        ans = [intervals[0]]
        for i in range(1, n):
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans

if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 4], [4, 5]]
    # intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    # intervals = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]
    print(Solution().merge(intervals))
