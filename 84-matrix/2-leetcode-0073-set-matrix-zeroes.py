from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """ 两个标记数组 """
        n, m = len(matrix), len(matrix[0])
        row, col = set(), set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        print(row)
        print(col)
        for r in row:
            matrix[r] = [0] * m
        for c in col:
            for i in range(n):
                matrix[i][c] = 0

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """ 两个标记数组 写法2 """
        n, m = len(matrix), len(matrix[0])
        row, col = set(), set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(n):
            for j in range(m):
                if i in row or j in col:
                    matrix[i][j] = 0

    def setZeroes3(self, matrix: List[List[int]]) -> None:
        """ 两个标记变量 使用第0行和第0列记录第i列和第j行是否含0 """
        n, m = len(matrix), len(matrix[0])
        r0_zero, c0_zero = 0, 0
        r0_zero = any(matrix[0][j] == 0 for j in range(m))
        c0_zero = any(matrix[i][0] == 0 for i in range(n))
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if r0_zero:
            for j in range(m):
                matrix[0][j] = 0
        if c0_zero:
            for i in range(n):
                matrix[i][0] = 0

    def setZeroes4(self, matrix: List[List[int]]) -> None:
        """ 一个标记变量 """
        n, m = len(matrix), len(matrix[0])
        is_zero = any(matrix[i][0] == 0 for i in range(n))
        for i in range(n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(n-1,-1,-1):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if is_zero:
            for i in range(n):
                matrix[i][0] = 0
if __name__ == '__main__':
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    # matrix = [[0, 0, 3]]
    # Solution().setZeroes(matrix)
    # Solution().setZeroes2(matrix)
    # Solution().setZeroes3(matrix)
    Solution().setZeroes4(matrix)
    print(matrix)
