from typing import List


class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     """
    #         错误代码
    #         该代码遵循-循环不变量
    #         即：从左到右，从上到下，从右到左，从下到上，都遵循左闭右开，处理头不处理尾。
    #         这种方法可能在方阵中可以正确使用，卡尔讲的 螺旋矩阵2。
    #         测试样例[[3,1,2]]：从左往右3,1，从上到下不添加，从右往左2,1，从下到上不添加。
    #         而且在方阵中方便处理奇数行奇数列情况，但在 螺旋矩阵1 这种非方阵中，无法正确处理奇数行奇数列的情况。
    #     """
    #     n, m = len(matrix), len(matrix[0])
    #     ans = []
    #     cur = 0
    #     level = m // 2 + m % 2
    #     while cur < level:
    #         for i in range(cur, m - 1 - cur):
    #             ans.append(matrix[cur][i])
    #         for i in range(cur, n - 1 - cur):
    #             ans.append(matrix[i][m - 1 - cur])
    #         for i in range(m - 1 - cur, cur, -1):
    #             ans.append(matrix[n - 1 - cur][i])
    #         for i in range(n - 1 - cur, cur, -1):
    #             ans.append(matrix[i][cur])
    #         cur += 1
    #     # 这里没想好怎么处理
    #     if n>1 and m>1 and n%2==1 and m%2==1: ans.append(matrix[n//2][m//2])
    #     return ans

    def spiralOrder3(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        ans = []
        col_begin, col_end = 0, len(matrix[0]) - 1  # 记录行的开头与结尾
        row_begin, row_end = 0, len(matrix) - 1  # 记录列的开头与结尾

        while True:
            # 从左往右
            for i in range(col_begin, col_end + 1):
                ans.append(matrix[row_begin][i])
            row_begin += 1
            if row_begin > row_end:
                break

            # 从上往下
            for i in range(row_begin, row_end + 1):
                ans.append(matrix[i][col_end])
            col_end -= 1
            if col_end < col_begin:
                break

            # 从右往左
            for i in range(col_end, col_begin - 1, -1):
                ans.append(matrix[row_end][i])
            row_end -= 1
            if row_end < row_begin:
                break

            # 从下往上
            for i in range(row_end, row_begin - 1, -1):
                ans.append(matrix[i][col_begin])
            col_begin += 1
            if col_begin > col_end:
                break

        return ans

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        ans = []
        cur = 0
        cnt = 0
        level = m // 2 + m % 2 # 非方阵，只需根据列数处理奇偶情况
        while cur < level:
            for i in range(cur, m - cur):
                if cnt >= n * m: break
                ans.append(matrix[cur][i])
                cnt+=1
            for i in range(cur + 1, n - 1 - cur):
                if cnt >= n * m: break
                ans.append(matrix[i][m - 1 - cur])
                cnt += 1
            for i in range(m - 1 - cur, cur - 1, -1):
                if cnt >= n * m: break
                ans.append(matrix[n - 1 - cur][i])
                cnt += 1
            for i in range(n - 2 - cur, cur, -1):
                if cnt >= n * m: break
                ans.append(matrix[i][cur])
                cnt += 1
            cur += 1
        return ans


if __name__ == '__main__':
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    matrix = [[6, 9, 7]]
    s = Solution()
    # print(s.spiralOrder(matrix))
    print(s.spiralOrder2(matrix))
    print(s.spiralOrder3(matrix))
