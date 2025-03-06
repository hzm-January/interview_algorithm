from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """ 网格dfs """
        n, m = len(grid), len(grid[0])
        curArea = [0]
        maxArea = 0

        def inArea(i, j):
            return 0 <= i < n and 0 <= j < m

        def backtrack(i, j):
            if not inArea(i, j):
                return
            if grid[i][j] != 1:
                return
            grid[i][j] = 2
            curArea[0] += 1
            backtrack(i + 1, j)
            backtrack(i - 1, j)
            backtrack(i, j + 1)
            backtrack(i, j - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1: continue
                curArea = [0]
                backtrack(i, j)
                maxArea = max(maxArea, curArea[0])
        return maxArea

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        stack = []
        maxArea = 0

        def inArea(i, j):
            return 0 <= i < n and 0 <= j < m

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1: continue
                stack.append((i, j))
                curArea = 0
                while stack:
                    cur_i, cur_j = stack.pop()
                    if not inArea(cur_i, cur_j): continue
                    if grid[cur_i][cur_j] != 1: continue
                    grid[cur_i][cur_j] = 2
                    curArea += 1
                    stack.append((cur_i + 1, cur_j))
                    stack.append((cur_i - 1, cur_j))
                    stack.append((cur_i, cur_j + 1))
                    stack.append((cur_i, cur_j - 1))
                maxArea = max(maxArea, curArea)
        return maxArea


if __name__ == '__main__':
    # grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    #         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    # grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    # print(Solution().maxAreaOfIsland(grid))
    print(Solution().maxAreaOfIsland2(grid))
