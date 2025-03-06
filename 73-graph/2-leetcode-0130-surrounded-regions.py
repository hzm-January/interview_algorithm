from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n, m = len(board), len(board[0])

        def inArea(i, j):
            return 0 <= i < n and 0 <= j < m

        def backtrack(i, j):
            if not inArea(i, j): return
            # 遇到X或A终止
            # 值得学习，这里判断，如果不是接下来处理的状态，全部跳过，写等于，可能要写两个条件=='X'或=='A'
            # 有时候可能漏写了等于的条件，进入无限递归
            if board[i][j] != 'O': return
            board[i][j] = 'A'
            backtrack(i + 1, j)
            backtrack(i - 1, j)
            backtrack(i, j + 1)
            backtrack(i, j - 1)

        for i in range(m):
            if board[0][i] != 'O': continue  # 遇到X或A跳过
            backtrack(0, i)
        for i in range(m):
            if board[n - 1][i] != 'O': continue  # 遇到X或A跳过
            backtrack(n - 1, i)
        for i in range(n):
            if board[i][0] != 'O': continue  # 遇到X或A跳过
            backtrack(i, 0)
        for i in range(n):
            if board[i][m - 1] != 'O': continue  # 遇到X或A跳过
            backtrack(i, m - 1)
        print(board)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'


if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    Solution().solve(board)
    print(board)
