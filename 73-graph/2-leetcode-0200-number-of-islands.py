from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def inArea(row, col):
            return 0 <= row < n and 0 <= col < m

        def backtrack(row, col):
            if not inArea(row, col):  return # base case1 超界
            if grid[row][col] != '1': return # base case2 结点无效
            grid[row][col] = '2' # 标记结点已被访问过
            backtrack(row + 1, col)
            backtrack(row - 1, col)
            backtrack(row, col + 1)
            backtrack(row, col - 1)

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '1':continue
                ans+=1
                backtrack(i, j)
        return ans



if __name__ == '__main__':
    # grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(grid))
