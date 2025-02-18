from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])

        ans = []
        cur = 0
        while cur < 2:
            for i in range(cur, m - 1 - cur):
                ans.append(matrix[cur][i])
            for i in range(cur, n - 1 - cur):
                ans.append(matrix[i][m - 1 - cur])
            for i in range(m - 1 - cur, cur, -1):
                ans.append(matrix[n - 1 - cur][i])
            for i in range(n - 1 - cur, cur, -1):
                ans.append(matrix[i][cur])
            cur += 1

        return ans


if __name__ == '__main__':
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    s = Solution()
    print(s.spiralOrder(matrix))
