import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ 拓扑排序 bfs """
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        queue = collections.deque([i for i, u in enumerate(indegree) if u == 0])
        ans = []
        while queue:
            v = queue.popleft()
            for u in graph[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    queue.append(u)
            graph[v] = []
            ans.append(v)

        return ans if len(ans) == numCourses else []
    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ 拓扑排序 dfs """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        ans = []
        visited = [0]*numCourses
        def dfs(node):
            visited[node]=1
            for u in graph[node]:
                if visited[u]==2:continue
                if visited[u]==1:
                    return False
                if not dfs(u):
                    return False
            visited[node]=2
            # 所有子节点有处理完成后，结点加入结果集（注意这里与BFS的思想相反）
            ans.append(node)
            return True

        for i in range(numCourses):
            if visited[i]==0:
                if not dfs(i):
                    return []
        ans.reverse()
        return ans

