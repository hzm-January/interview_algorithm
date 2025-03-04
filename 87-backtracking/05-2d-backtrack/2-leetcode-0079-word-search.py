from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:  # 当前字符等于字符串最后一个字符
                return True
            visited.add((i, j)) # 标记已访问，不能往回走
            for dx, dy in directions:
                newi, newj = i + dx, j + dy
                if newi < 0 or newi >= n or newj < 0 or newj >= m: continue
                if (newi, newj) in visited: continue
                if check(newi, newj, k + 1):
                    return True
            visited.remove((i,j)) # 回溯
            return False

        for i in range(n):
            for j in range(m):
                if check(i, j, 0):
                    return True

        return False
if __name__ == '__main__':
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCCED"
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCB"
    print(Solution().exist(board, word))
