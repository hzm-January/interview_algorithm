import time
from typing import List
import math

from mpmath.visualization import blue_orange_colors


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """ 
            回溯 
        """
        n, m = len(board), len(board[0])  # 题目已知board长度等于9，方阵
        col_occ = [[0] * 10 for _ in range(n)]  # 列占用
        row_occ = [[0] * 10 for _ in range(m)]  # 行占用
        local_size = 3
        local_n, local_m = math.ceil(n / local_size), math.ceil(m / local_size)  # 局部矩阵的个数
        local_occ = [[[0] * (n + 1) for _ in range(local_m)] for _ in range(local_n)]  # 3x3占用
        space = []

        # 预处理棋盘占用情况
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    row_occ[i][int(board[i][j])] = 1
                    col_occ[j][int(board[i][j])] = 1
                    local_occ[i // local_size][j // local_size][int(board[i][j])] = 1
                else:
                    space.append((i, j))

        def check(row, col, k):
            if col_occ[col][k]: return False
            if row_occ[row][k]: return False
            if local_occ[row // local_size][col // local_size][k]: return False
            return True

        def backtrack(pos):
            if pos == len(space):
                return True
            row, col = space[pos]
            for k in range(1, 10):
                if check(row, col, k):
                    col_occ[col][k] = 1
                    row_occ[row][k] = 1
                    local_occ[row // local_size][col // local_size][k] = 1
                    board[row][col] = str(k)
                    if backtrack(pos + 1): return True
                    board[row][col] = '.'
                    local_occ[row // local_size][col // local_size][k] = 0
                    row_occ[row][k] = 0
                    col_occ[col][k] = 0
            return False  # 单层搜索1~9没有找到答案

        backtrack(0)
        # print(board)

    def solveSudoku2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """ 
            回溯 
        """
        n, m = len(board), len(board[0])  # 题目已知board长度等于9，方阵
        col_occ = [[0] * 10 for _ in range(n)]  # 列占用
        row_occ = [[0] * 10 for _ in range(m)]  # 行占用
        local_size = 3
        local_n, local_m = math.ceil(n / local_size), math.ceil(m / local_size)  # 局部矩阵的个数
        local_occ = [[[0] * (n + 1) for _ in range(local_m)] for _ in range(local_n)]  # 3x3占用
        spaces = []
        success = [False]
        # 预处理棋盘占用情况
        for i in range(n):
            for j in range(m):
                if board[i][j] != '.':
                    row_occ[i][int(board[i][j])] = 1
                    col_occ[j][int(board[i][j])] = 1
                    local_occ[i // local_size][j // local_size][int(board[i][j])] = 1
                else:
                    spaces.append((i, j))

        print('col_occ', col_occ)
        print('row_occ', row_occ)
        print('local_occ', local_occ)

        def check(row, col, k):
            if col_occ[col][k]: return False
            if row_occ[row][k]: return False
            if local_occ[row // local_size][col // local_size][k]: return False
            return True

        def backtrack(pos: int):
            if pos == len(spaces):
                success[0] = True
                return
            row, col = spaces[pos]
            for k in range(1, 10):
                if check(row, col, k):
                    col_occ[col][k] = 1
                    row_occ[row][k] = 1
                    local_occ[row // local_size][col // local_size][k] = 1
                    board[row][col] = str(k)
                    backtrack(pos + 1)
                    if success[0]:
                        return
                    board[row][col] = '.'
                    local_occ[row // local_size][col // local_size][k] = 0
                    row_occ[row][k] = 0
                    col_occ[col][k] = 0

        backtrack(0)

    def solveSudoku3(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """ 
            回溯 
        """
        n, m = len(board), len(board[0])  # 题目已知board长度等于9，方阵
        col_occ = [0] * n  # 列占用
        row_occ = [0] * n  # 行占用
        local_size = 3
        local_n, local_m = math.ceil(n / local_size), math.ceil(m / local_size)  # 局部矩阵的个数
        local_occ = [[0] * local_m for _ in range(local_n)]  # 3x3占用
        spaces = []
        success = [False]

        def flip(row, col, digit):  # 反转二进制位
            row_occ[row] ^= (1 << digit)
            col_occ[col] ^= (1 << digit)
            local_occ[row // local_size][col // local_size] ^= (1 << digit)

        # 预处理棋盘占用情况
        for i in range(n):
            for j in range(m):
                if board[i][j] != '.':
                    digit = int(board[i][j]) - 1  # 数字1~9，用二进制从右往左的0~8位表示
                    flip(i, j, digit)  # 记录当前数字在当前行、列和局部矩阵中出现过
                else:
                    spaces.append((i, j))

        print('col_occ', col_occ)
        print('row_occ', row_occ)
        print('local_occ', local_occ)

        def backtrack(pos: int):
            if pos == len(spaces):
                success[0] = True
                return
            row, col = spaces[pos]
            availPos = ~(row_occ[row] | col_occ[col] | local_occ[row // local_size][col // local_size]) & ((1 << n) - 1)
            while availPos:
                curPos = availPos & (-availPos)  # 取出最低位的1
                digit = bin(curPos).count('0') - 1  # 获取数字，0b100 统计0个数3个，去掉标识二进制开头的0b中的0，则digital=2
                flip(row, col, digit)
                board[row][col] = str(digit + 1)
                backtrack(pos + 1)
                if success[0]:
                    return
                board[row][col] = '.'
                flip(row, col, digit)
                availPos = availPos & (availPos - 1)  # 将最后一位1置为0，单层搜索逻辑

        backtrack(0)


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # board = [[".", ".", ".", ".", ".", ".", ".", ".", "."], [".", "9", ".", ".", "1", ".", ".", "3", "."],
    #          [".", ".", "6", ".", "2", ".", "7", ".", "."], [".", ".", ".", "3", ".", "4", ".", ".", "."],
    #          ["2", "1", ".", ".", ".", ".", ".", "9", "8"], [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #          [".", ".", "2", "5", ".", "6", "4", ".", "."], [".", "8", ".", ".", ".", ".", ".", "1", "."],
    #          [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    # start = time.time()
    Solution().solveSudoku(board)
    # end = time.time()
    # print('time: ', end - start)
    # print(board)
    # Solution().solveSudoku2(board)
    # end2 = time.time()
    # print('time: ', end2 - end)
    # print(board)
    # Solution().solveSudoku3(board)
    print(board)
