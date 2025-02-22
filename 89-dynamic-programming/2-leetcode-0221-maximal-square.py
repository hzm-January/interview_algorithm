from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
            动态规划  通俗易懂版
            1 dp数组定义：matrix[i][j]位置处左，左上，上，三个方向构成的只含1的正方形长度为dp[i][j]
            2 递推公式：取左，左上，上，三个方向上最小值
            3 dp初始化：第1行和第1列按照matrix中的值初始化
            4 遍历顺序：从上到下，从左往右
            5 打印
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        max_area = 0
        # 初始化
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
            max_area = max(max_area, dp[i][0])
        for j in range(m):
            dp[0][j] = int(matrix[0][j])
            max_area = max(max_area, dp[0][j])
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '0': continue  # 可以将初始化放在这里
                if matrix[i][j - 1] == '0' or matrix[i - 1][j] == '0' or matrix[i - 1][j - 1] == '0':
                    dp[i][j] = 1  # 这个判断条件可以去掉，以内如果周围有0，那么下面的递推公式min最小一定取0，再加1跟这里的等于1一样
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                max_area = max(max_area, dp[i][j])
            # import numpy
            # print(numpy.array(dp))
        return max_area ** 2

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        """ 动态规划  写法优化 """
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        max_area = 0
        for i in range(0, n):
            for j in range(0, m):
                if matrix[i][j] == '0': continue
                if i == 0 or j == 0:
                    dp[i][j] = 1  # 将dp初始化放在这里
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                max_area = max(max_area, dp[i][j])
            # import numpy
            # print(numpy.array(dp))
        return max_area ** 2


if __name__ == '__main__':
    # matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
    #           ["1", "0", "0", "1", "0"]]

    matrix = [["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["0", "0", "1", "1", "1"]]
    import numpy

    print(numpy.array(matrix))
    print(Solution().maximalSquare(matrix))
