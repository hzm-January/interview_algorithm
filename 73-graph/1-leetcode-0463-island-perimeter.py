from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        def inArea(i, j):
            return 0 <= i < n and 0 <= j < m

        def backtrack(i, j):
            if not inArea(i, j):
                return 1
            if grid[i][j] == 0:
                return 1
            if grid[i][j] == 2:
                return 0
            grid[i][j] = 2  # 标记已访问
            return backtrack(i + 1, j) + backtrack(i - 1, j) + backtrack(i, j + 1) + backtrack(i, j - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return backtrack(i, j)
        return ans

    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cords =[(0,1),(0,-1),(1,0),(-1,0)]
        ans = 0
        for i in range(n):
            for j in range(m):
                for k in range(4):
                    if grid[i][j] == 0:continue
                    x= i+cords[k][0]
                    y= j+cords[k][1]
                    if x<0 or x>=n or y<0 or y>=m or grid[x][y] == 0:
                        ans+=1
        return ans


if __name__ == '__main__':
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    # grid = [[1]]
    # grid = [[1,0]]
    # print(Solution().islandPerimeter(grid))
    print(Solution().islandPerimeter2(grid))