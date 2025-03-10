from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """ 最短路径 BFS """

        def id2rc(idx):
            r, c = (idx - 1) // n, (idx - 1) % n
            if r % 2 == 1:
                c = n - 1 - c  # 奇数行列从右往左
            return n - 1 - r, c  # 行从下到上

        n, m = len(board), len(board[0])
        visited=set()
        visited.add(1)
        import collections
        q = collections.deque([(1, 0)])  # (顶点编号，步数)
        while q:
            idx, step = q.popleft()
            for i in range(1, 6 + 1):
                newId = idx + i
                if newId > n*n: break # 终止探索，继续从队列中弹出元素访问

                newR, newC = id2rc(newId)

                if board[newR][newC] != -1:  # 有梯子，直接跳到梯子端点
                    newId = board[newR][newC]

                # step+=1 # 注意易错点，step+1不能放在这里，因为有可能当前newId之前被访问过，这种情况不能被再次访问，这里step+=1在这种情况下又访问了已访问的顶点一次
                if newId==n*n: # 已访问到目标顶点
                    return step+1 # 不再入队，直接返回，相当于剪枝

                # visited判断必须放在梯子判断的后面，测试样例：[[1,1,-1],[1,1,1],[-1,1,1]]
                # 值得学习：其本质意义是 要判断加入队列的那个元素是否之前被访问过，当有梯子时，梯子的尽头才是要被放入队列的元素
                if newId in visited: continue  # 已访问过，不再加入队列，即不再被访问

                visited.add(newId)
                q.append((newId, step+1)) # 入队，等待访问
        return -1

if __name__ == '__main__':
    board = [[1,1,-1],[1,1,1],[-1,1,1]]
    print(Solution().snakesAndLadders(board))