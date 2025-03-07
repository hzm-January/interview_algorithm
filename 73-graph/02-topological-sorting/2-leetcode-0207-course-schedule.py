import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ 广度优先 写法优化 """
        # 1 建图
        graph = {}
        inDegree = {}
        for c1, c2 in prerequisites:
            if c1 not in graph:
                graph[c1] = []
            if c2 not in graph:
                graph[c2] = []
            graph[c2].append(c1)  # c2是前导课程，完成c2之后才能完成c1
            inDegree[c1] = inDegree.get(c1, 0) + 1
            if c2 not in inDegree:
                inDegree[c2] = 0

        print(graph)
        print(inDegree)
        # 2 拓扑排序
        queue = []
        cnt = 0
        for k, v in inDegree.items():
            if v == 0:
                queue.append(k)  # 入度为0，入队

        while queue:
            node = queue.pop(0)  # 队首出队
            for c in graph[node]:
                inDegree[c] -= 1
                if inDegree[c] == 0:
                    queue.append(c)
            graph[node] = []
            cnt += 1  # 该写法中cnt没用，因为indegree使用字典存储，且上面的逻辑没有对numCourses的每一个值都进行indegree=0的初始化。
            # 例如：极端例子，numCourses=1, prerequisites=[]
        result = True
        for k, v in graph.items():
            if len(v) != 0:
                result = False

        return result

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ 广度优先 写法优化 """
        # 1 建图
        graph = collections.defaultdict(list)
        inDegree = [0] * numCourses
        for c1, c2 in prerequisites:
            graph[c2].append(c1)  # c2是前导课程，完成c2之后才能完成c1
            inDegree[c1] += 1

        # 2 拓扑排序
        queue = collections.deque([i for i, d in enumerate(inDegree) if d == 0])
        visited = 0
        while queue:
            node = queue.popleft()  # 队首出队
            visited += 1
            for c in graph[node]:
                inDegree[c] -= 1
                if inDegree[c] == 0:
                    queue.append(c)
            graph[node] = []

        return visited == numCourses

    def canFinish3(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        edges = collections.defaultdict(list)
        for c1, c2 in prerequisites:
            edges[c2].append(c1)

        visited = [0] * numCourses

        def dfs(c):
            # if visited[c]==1: return False  #可以注释掉，不适用改行也能AC
            visited[c] = 1
            result = True
            for e in edges[c]:
                if visited[e] == 1:
                    return False
                if visited[e] == 2:
                    continue
                result = dfs(e)
                if not result: return False
            visited[c] = 2
            return result

        result = True
        for c in range(numCourses):
            if visited[c]: continue
            result = dfs(c)
            if not result: break
        return result


if __name__ == '__main__':
    numCourses, prerequisites = 2, [[1, 0], [0, 1]]
    # numCourses, prerequisites = 2, [[1, 0]]
    # numCourses, prerequisites = 1, []
    print(Solution().canFinish(numCourses, prerequisites))
    print(Solution().canFinish2(numCourses, prerequisites))
    print(Solution().canFinish3(numCourses, prerequisites))
