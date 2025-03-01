from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """ 回溯 卡尔版 通俗易懂 """
        tmp = [['.'] * n for _ in range(n)]
        ans = []

        def backtrack(row):  # 1 参数列表及返回值
            if row == n:  # 2 终止条件
                ans.append([''.join(t) for t in tmp])
                return
            # 单层搜索逻辑  搜索当前行的所有列
            for col in range(n):
                if not check(row, col): continue
                tmp[row][col] = 'Q'
                backtrack(row + 1)  # 回溯行
                tmp[row][col] = '.'

        def check(row, col):
            # 检查列
            for i in range(row):
                if tmp[i][col] == 'Q':
                    return False
            # 检查行（回溯按照行，所以，一定不存在一行中有多个元素的情况）
            # 检查对角线
            p, q = row - 1, col - 1
            while p >= 0 and q >= 0:
                if tmp[p][q] == 'Q':
                    return False
                p -= 1
                q -= 1
            # 检查对角线
            p, q = row - 1, col + 1
            while p >= 0 and q <= n - 1:
                if tmp[p][q] == 'Q':
                    return False
                p -= 1
                q += 1
            return True

        backtrack(0)
        return ans

    def solveNQueens2(self, n: int) -> List[List[str]]:
        """ 回溯 三个hash表 check """
        tmp = [['.'] * n for _ in range(n)]
        ans = []
        hash_col = [0] * n  # 列hash，因为按照行回溯，所以一定不存在两个元素出现在同一行的情况
        hash_diag1 = [0] * (n << 1)  # 正对角线hash
        hash_diag2 = [0] * (n << 1)  # 副对角线hash

        def backtrack(row):  # 1 参数列表及返回值
            if row == n:  # 2 终止条件
                ans.append([''.join(t) for t in tmp])
                return
            # 单层搜索逻辑  搜索当前行的所有列
            for col in range(n):
                if not check(row, col): continue
                hash_diag2[col + row] = 1
                hash_diag1[col - row] = 1
                hash_col[col] = 1
                tmp[row][col] = 'Q'
                backtrack(row + 1)  # 回溯行
                tmp[row][col] = '.'
                hash_col[col] = 0
                hash_diag1[col - row] = 0
                hash_diag2[col + row] = 0

        def check(row, col):
            if hash_col[col] or hash_diag1[col - row] or hash_diag2[col + row]:
                return False
            return True

        backtrack(0)
        return ans

    def solveNQueens3(self, n: int) -> List[List[str]]:
        """ 回溯 卡尔版 通俗易懂 """
        tmp = [['.'] * n for _ in range(n)]
        hash =[-1]*n # 标记第i行，被那一列占用
        ans = []

        def generateBoard():
            board = list()
            for i in range(n):
                tmp[i][hash[i]] = "Q"
                board.append("".join(tmp[i]))
                tmp[i][hash[i]] = "."
            return board
        def backtrack(row, columns, diagonals1, diagonal2):  # 1 参数列表及返回值
            if row == n:  # 2 终止条件
                # ans.append([''.join(t) for t in tmp])
                ans.append(generateBoard())
                return
            # 单层搜索逻辑  搜索当前行的所有列
            availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonal2))  # 获取n列中可用位置
            while availablePositions:  # 尝试所有可用位置
                # x&(-x) 获取最低位的1，可用位置。例如1010其补码位0110,1010&0110=0010
                position = availablePositions & (~availablePositions)
                # 删除最低位的1，即当前可用位置，尝试其他可用位置，例如1010，减1为1001，则1010&1001=1000
                availablePositions = availablePositions & (availablePositions - 1)
                # 将2进制pos转换为列索引，例如：1000-1=0111，bin(0111)='0b111'，'0b111'.count(1)=3，即1000标识的索引位置为3
                # bin将二进制数转换为字符串，前面添加了0b标识
                column = bin(position-1).count('1')
                # tmp[row][column] = 'Q'
                hash[row] = column
                backtrack(row + 1, columns | position, (diagonals1 | position) << 1, (diagonal2 | position) >> 1)
                # tmp[row][column] = '.'

        backtrack(0, 0, 0, 0)
        return ans

if __name__ == "__main__":
    print(Solution().solveNQueens(4))
    print(Solution().solveNQueens2(4))
    print(Solution().solveNQueens3(4))
