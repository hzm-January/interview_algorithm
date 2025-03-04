class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = [0]
        col_occ = {}
        diag1_occ = {}
        diag2_occ = {}

        def check(row, col):
            # 检查列
            if col in col_occ and col_occ[col] == 1: return False
            # 检查正对角线
            if col - row in diag1_occ and diag1_occ[col - row]: return False
            # 检查副对角线
            if col + row in diag2_occ and diag2_occ[col + row]: return False
            # 符合条件
            return True

        def backtrack(row):  # 1 参数列表与返回值
            if row >= n:  # 2 终止条件
                ans[0] += 1
                return
            # 3 单层搜索逻辑
            for col in range(n):
                # 搜索当前行的所有列
                if check(row, col):
                    col_occ[col] = 1
                    diag1_occ[col - row] = 1
                    diag2_occ[col + row] = 1
                    backtrack(row + 1)
                    diag2_occ[col + row] = 0
                    diag1_occ[col - row] = 0
                    col_occ[col] = 0

        backtrack(0)
        # print(ans)
        # print(col_occ)
        # print(diag1_occ)
        # print(diag2_occ)
        return ans[0]

    def totalNQueens2(self, n: int) -> int:
        ans = [0]

        def backtrack(row, cols, diag1, diag2):  # 1 参数列表与返回值
            if row >= n:  # 2 终止条件
                ans[0] += 1  # 能走过n行(0~n-1)的都是答案
                return
            # 合并列、主对角线和副对角线的占用情况，得到一个表示所有被占用的位置的掩码
            # 取反操作，得到一个表示所有可用位置的掩码
            # 生成一个低n位全为1的掩码，表示所有可能的列位置。与其 & 将可用位置的掩码限制在n列范围内（取反操作后前面会有很多1，需要截断）
            availPos = ((1 << n) - 1) & (~(cols | diag1 | diag2))
            # 3 单层搜索逻辑
            while availPos:  # 尝试所有可能情况
                curPos = availPos & (-availPos)  # 获取最低位的1，表示当前可用的列，只保留最低位的 1，其余位都为 0

                # col = bin(curPos-1).count('1') # curPos将最低位的1修改为0，并将其之后的0全部变为1，count 之后的1
                # diag1,diag2移动方向与实际方向相反，因为棋盘的序号标记（从左往右）和二进制数中对序号的标记（从右往左）正好相反
                backtrack(row + 1, cols | curPos, (diag1 | curPos) << 1, (diag2 | curPos) >> 1)

                # availPos-1 最低位的 1 变为 0，并将更低位的所有 0 变为 1
                availPos = availPos & (availPos - 1)  # 移除最低位的1，表示下次迭代尝试下一个位置（单层搜索所有可能情况）

        backtrack(0, 0, 0, 0)
        return ans[0]


if __name__ == '__main__':
    print(Solution().totalNQueens(4))
    print(Solution().totalNQueens2(4))
