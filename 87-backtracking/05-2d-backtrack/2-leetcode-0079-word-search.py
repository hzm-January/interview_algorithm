from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False

            for dx, dy in directions:
                newi, newj = i + dx, j + dy
                if newi < 0 or newi >= n or newj < 0 or newj >= m: continue
                if (newi, newj) in visited: continue
                if check(newi, newj, k + 1):
                    result = True
                    break
            return result

        for i in range(n):
            for j in range(m):
                if check(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i, j in directions:
        print(i, j)
