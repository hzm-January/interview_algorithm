from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """ 原地旋转 """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - 1 - i):  # 遍历到倒数第二个数，因为在遍历第一个数的时候处理了倒数第一个数
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp

    def rotate2(self, matrix: List[List[int]]) -> None:
        import copy
        tmp = copy.deepcopy(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][n-1-i] = tmp[i][j]



if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(matrix)
    print(matrix)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate2(matrix)
    print(matrix)

