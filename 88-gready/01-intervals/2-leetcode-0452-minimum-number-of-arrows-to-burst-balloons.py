from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (-x[0], x[1]))
        print(points)
        pre_left = points[0][1] + 1  # 上一个区间的左端点，初始值赋值为左端点最大的区间的右端点+1
        ans = 0
        for point in points:
            cur_right = point[1]
            if cur_right < pre_left:  # 这里必须是小于，不能是小于等于，例[2,3] [1,2]，只选择[2,3]即可选中2，没有必要再选择2也在的区间[1,2]
                ans += 1
                pre_left = point[0]  # pre_left=cur_left
        return ans

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], -x[0]))
        print(points)
        ans = 0
        pre_right = points[0][0] - 1  # 上一个区间的右端点，初始化为第一个区间的左端点-1
        for point in points:
            cur_left = point[0]  #
            if cur_left > pre_right:  # 当前左端点大于上一个区间的右端点
                ans += 1
                pre_right = point[1]  # 更新 pre_right
        return ans

    def findMinArrowShots3(self, points: List[List[int]]) -> int:
        """ 卡尔版 """
        points.sort(key=lambda x: (x[1]))
        print(points)
        ans = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:  # 当前区间左端点大于上一个区间右端点
                ans += 1
            else:  # 当前区间左端点小于等于上一个区间右端点
                # 重复区间取右端点较小
                # 例：[1,3] [2,4] [3,5]
                points[i][1] = min(points[i][1], points[i - 1][1])  # 更新当前区间端点为与上个区间右端点相比的较大值
        return ans


if __name__ == '__main__':
    # points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    # points = [[10, 16], [2, 8], [2,7], [1, 6], [7, 12]]
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(Solution().findMinArrowShots(points))
    print(Solution().findMinArrowShots2(points))
    print(Solution().findMinArrowShots3(points))
