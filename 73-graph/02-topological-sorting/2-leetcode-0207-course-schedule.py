from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
                inDegree[c2]=0


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
            graph[node]=[]
            cnt += 1
        return cnt == numCourses


if __name__ == '__main__':
    # numCourses, prerequisites = 2, [[1, 0], [0, 1]]
    numCourses, prerequisites = 2, [[1, 0]]
    print(Solution().canFinish(numCourses, prerequisites))
