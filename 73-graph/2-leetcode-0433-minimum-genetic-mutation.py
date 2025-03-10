from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """ bfs """
        # if endGene not in bank: return -1 # 省略可AC
        # if startGene == endGene: return 0 # 省略可AC
        queue = [(startGene, 0)]  # step=0
        while queue:
            curNode, step = queue.pop(0)
            for i, c in enumerate(curNode):
                for f in 'ACGT':
                    if c == f: continue
                    cur = curNode[:i] + f + curNode[i + 1:]
                    if cur not in bank: continue  # 不合法
                    if cur == endGene: return step + 1
                    bank.remove(cur)
                    queue.append((cur, step + 1))
        return -1

    def minMutation2(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """ bfs bank预处理 """

        def diffOne(s: str, t: str):
            return sum([x != y for x, y in zip(s, t)]) == 1

        # 1 bank预处理 - 根据bank建图
        n = len(bank)
        adj = [[] for _ in range(n)]
        endIndex = -1
        for i in range(n):
            if bank[i] == endGene:
                endIndex = i
            for j in range(i + 1, n):
                if not diffOne(bank[i], bank[j]): continue
                adj[i].append(j)
                adj[j].append(i)
        if endIndex == -1: return -1  # 答案不存在于bank中
        # 2 bfs搜索
        from collections import deque
        q = [i for i, b in enumerate(bank) if diffOne(b, startGene)]
        vis = set(q)
        step = 1
        while q:
            tmp = q
            q = []
            for cur in tmp:
                if cur == endIndex: return step
                for nxt in adj[cur]:  # 遍历邻接顶点
                    if nxt in vis: continue  # 已访问过
                    vis.add(nxt)
                    q.append(nxt)
            step += 1  # 处理完当前顶点
        return -1

    def minMutation2_2(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """ bfs bank预处理 """

        def diffOne(s: str, t: str):
            return sum([x != y for x, y in zip(s, t)]) == 1

        # 1 bank预处理 - 根据bank建图
        n = len(bank)
        adj = [[] for _ in range(n)]
        endIndex = -1
        for i in range(n):
            if bank[i] == endGene:
                endIndex = i
            for j in range(i + 1, n):
                if not diffOne(bank[i], bank[j]): continue
                adj[i].append(j)
                adj[j].append(i)
        if endIndex == -1: return -1  # 答案不存在于bank中
        # 2 bfs搜索
        from collections import deque
        q = deque([i for i, b in enumerate(bank) if diffOne(b, startGene)])
        vis = set(q)
        step = 1
        while q:  # 按照二叉树的层序遍历，因为需要记录层结束，当遍历完一层时，说明当前字符修改了一个字符，step+=1
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur == endIndex: return step
                for nxt in adj[cur]:  # 遍历邻接顶点
                    if nxt in vis: continue  # 已访问过
                    vis.add(nxt)
                    q.append(nxt)
            step += 1  # 处理完当前顶点
        return -1

    def minMutation2_3(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """ 无权单源最短路径 bank预处理建图 """

        def diffOne(s: str, t: str):
            return sum([x != y for x, y in zip(s, t)]) == 1

        # 1 bank预处理 - 根据bank建图
        n = len(bank)
        adj = [[] for _ in range(n)]
        endIndex = -1
        for i in range(n):
            if bank[i] == endGene:
                endIndex = i
            for j in range(i + 1, n):
                if not diffOne(bank[i], bank[j]): continue
                adj[i].append(j)
                adj[j].append(i)
        if endIndex == -1: return -1  # 答案不存在于bank中
        # 2 bfs搜索
        from collections import deque
        q = deque([i for i, b in enumerate(bank) if diffOne(b, startGene)])
        dist = [1 if diffOne(b, startGene) else -1 for b in bank] # 距离数组
        while q:
            cur = q.popleft()
            if cur == endIndex: return dist[cur] # 已找到目标节点
            for nxt in adj[cur]:
                if dist[nxt] != -1: continue # 已访问过
                dist[nxt] = dist[cur] + 1 # 距离+1
                q.append(nxt)
        return -1


if __name__ == '__main__':
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(Solution().minMutation2_2(startGene, endGene, bank))
    print(Solution().minMutation2_3(startGene, endGene, bank))
