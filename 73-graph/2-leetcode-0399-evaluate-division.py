from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """ 并查集 """
        map = {}

        father = [i for i in range(27)]
        weight = [1.0 for i in range(27)]

        # find 递归写法
        def find(x):
            # 寻找x所在集合的根节点
            if x != father[x]:
                tmp = father[x]
                father[x] = find(father[x])
                weight[x] *= weight[tmp]
            return father[x]

        # find 迭代写法
        # def find(x):
        #     # 寻找x所在集合的根节点
        #     b = x
        #     a = x
        #     w = weight[x]
        #     while x != father[x]:
        #         x = father[x]
        #         w *= weight[x]
        #     tmp_w2 = w
        #     while a != father[a]:
        #         tmp_w = weight[a]
        #         weight[a] = w
        #         w /= tmp_w
        #         tmp= a
        #         a = father[a]
        #         father[tmp]=x
        #     weight[b] = tmp_w2
        #     return father[x]

        def union(a, b, val):
            af = find(a)
            bf = find(b)
            if af != bf:
                father[af] = bf
            weight[af] = weight[b] * val / weight[a]

        id = 0
        for i, (s1, s2) in enumerate(equations):
            if s1 not in map:
                map[s1] = id
                id += 1
            if s2 not in map:
                map[s2] = id
                id += 1
            union(map[s1], map[s2], values[i])
            # print(i,num1,num2)

        # 查询
        ans = []
        for s1, s2 in queries:
            if s1 not in map or s2 not in map:
                ans.append(-1.0)
                continue
            num1, num2 = map[s1], map[s2]
            n1f, n2f = find(num1), find(num2)
            if n1f == n2f:
                ans.append(weight[num1] / weight[num2])
            else:
                ans.append(-1.0)

        # print(weight)
        # print(father)
        # print(exist)
        return ans

    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """ 建图 dfs 搜索 """
        graph = {}
        for i, (s1, s2) in enumerate(equations):
            if s1 not in graph:
                graph[s1] = {}
            if s2 not in graph:
                graph[s2] = {}

            graph[s1][s2] = values[i]
            graph[s2][s1] = 1.0 / values[i]

        print(graph)
        visited = {}
        ans = []

        def dfs(s1, s2, weight):
            # 带返回值，防止错误：s1,s2都在图中，但是不在同一个集合，没有s1到s2的路径，这时需要给结果集中添加-1.0
            if s1 not in graph or s2 not in graph:
                ans.append(-1.0)
                return True
            if s1 == s2:
                ans.append(weight)
                return True
            visited[s1] = True
            result = False
            for key, val in graph[s1].items():
                if key in visited: continue
                result = dfs(key, s2, weight * val)
                if result: return True
            return result

        for i, (s1, s2) in enumerate(queries):
            visited = {}
            if not dfs(s1, s2, 1.0):
                ans.append(-1.0)

        return ans

    def calcEquation3(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """ 建图 bfs 搜索 """
        graph = {}
        for i, (s1, s2) in enumerate(equations):
            if s1 not in graph:
                graph[s1] = {}
            if s2 not in graph:
                graph[s2] = {}

            graph[s1][s2] = values[i]
            graph[s2][s1] = 1.0 / values[i]

        print(graph)
        visited = {}
        ans = []

        def bfs(s1, s2):
            queue = [(s1, 1.0)]
            while queue:
                node,weight = queue.pop(0)
                visited[node] = True
                if node not in graph:
                    ans.append(-1.0)
                    return True
                if node==s2:
                    ans.append(weight)
                    return True
                for key, val in graph[node].items():
                    if key in visited: continue
                    queue.append((key, val*weight))
            return False

        for i, (s1, s2) in enumerate(queries):
            visited = {}
            if not bfs(s1, s2):
                ans.append(-1.0)

        return ans

if __name__ == '__main__':
    # equations = [["a", "b"], ["b", "c"]]
    # values = [2.0, 3.0]
    # queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    equations = [["a", "b"], ["c", "d"]]
    values = [1.0, 1.0]
    queries = [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]

    print(Solution().calcEquation(equations, values, queries))
    print(Solution().calcEquation2(equations, values, queries))
    print(Solution().calcEquation3(equations, values, queries))
