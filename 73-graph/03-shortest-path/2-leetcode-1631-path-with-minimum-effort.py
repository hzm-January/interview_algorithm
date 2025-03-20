from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
            超时代码
            超时原因：使用数组，没有使用最小堆
            Dijkstra 最短路径
        """
        n, m = len(heights), len(heights[0])
        # dist = [(float('inf'), 0, 0)] * (n * m)
        dist = [(float('inf'), r, c) for r in range(n) for c in range(m)]
        visited = set()
        print(dist)

        def find_mid():
            minDx, minDy, minDist = -1, -1, float('inf')
            for i, (d, x, y) in enumerate(dist):
                if (x, y) in visited: continue  # 已访问的顶点不再访问
                if d < minDist:
                    minDist, minDx, minDy = d, x, y
            return minDx, minDy, minDist

        def check(x, y):
            if 0 <= x < n and 0 <= y < m: return True
            return False

        def dijkstra(start, end):
            dist[start] = (0, start // m, start % m)
            for i in range(n * m):  # 总共要收集n个节点
                # 1 找到dist中最小值
                minDx, minDy, minDist = find_mid()
                print(minDx, minDy, minDist)
                # 2 标记minDist顶点已被访问
                visited.add((minDx, minDy))
                if minDx * m + minDy == end: break  # 已找到终点
                # 3 访问minDist顶点的邻接点
                for nxt_x, nxt_y in [(minDx - 1, minDy), (minDx, minDy - 1), (minDx + 1, minDy), (minDx, minDy + 1)]:
                    if (nxt_x, nxt_y) in visited: continue
                    if not check(nxt_x, nxt_y): continue  # 越界访问
                    if max(minDist, abs(heights[nxt_x][nxt_y] - heights[minDx][minDy])) < dist[nxt_x * m + nxt_y][
                        0]:  # 更新为更短路径
                        dist[nxt_x * m + nxt_y] = (
                            max(minDist, abs(heights[nxt_x][nxt_y] - heights[minDx][minDy])), nxt_x, nxt_y)
                        # dist[nxt_x * n + nxt_y][0] = minDist + heights[nxt_x][nxt_y]
            print(dist)
            print(visited)
            return int(dist[m * n - 1][0])

        return dijkstra(0, n * m - 1)


    def minimumEffortPath2(self, heights: List[List[int]]) -> int:
        """
            Dijkstra 最短路径
        """
        import heapq
        n, m = len(heights), len(heights[0])
        q = [(0, 0, 0)]
        dist = [float('inf')] * (n * m)
        visited = set()

        def check(x, y):
            if 0 <= x < n and 0 <= y < m: return True
            return False

        def dijkstra(start, end):
            dist[start] = 0
            # 使用堆时，必须写while q--6482次，不能写for i in range(n*m)--6443次，少执行了很多次，堆中很多元素没有处理，剩余在了堆中
            # 原来使用dist数组记录数值，每次从dist数组中以O(n)时间复杂度寻找最小值，在更新最短路径时，没有往dist数组中新添加元素
            # 使用堆时，每次更新最短路径时，需要将新更新的最短路径添加到堆中，处理次数不是元素个数，而是往堆中添加元素的个数
            # 本质原因：顶点可能重复入堆，如果第k次计算当前顶点距离更小，更新该顶点最短距离，会重新入队，等待下次更新
            while q:  # 总共要收集n个节点，注意使用堆时这里的写法, 一定要写为while q
                # 1 找到dist中最小值
                minDist, minDx, minDy  = heapq.heappop(q)
                print(minDx, minDy, minDist)
                # 2 标记minDist顶点已被访问
                visited.add((minDx, minDy))
                if minDx * m + minDy == end: break  # 已找到终点
                # 3 访问minDist顶点的邻接点
                for nxt_x, nxt_y in [(minDx - 1, minDy), (minDx, minDy - 1), (minDx + 1, minDy), (minDx, minDy + 1)]:
                    if (nxt_x, nxt_y) in visited: continue
                    if not check(nxt_x, nxt_y): continue  # 越界访问
                    curHeightDiffAbs = abs(heights[nxt_x][nxt_y] - heights[minDx][minDy])
                    if max(minDist, curHeightDiffAbs) < dist[nxt_x * m + nxt_y]:  # 更新为更短路径
                        dist[nxt_x * m + nxt_y] = max(minDist, curHeightDiffAbs)
                        heapq.heappush(q, (int(dist[nxt_x * m + nxt_y]), nxt_x, nxt_y))
                        # dist[nxt_x * n + nxt_y][0] = minDist + heights[nxt_x][nxt_y]
            print(dist)
            print(visited)
            return int(dist[m * n - 1])

        return dijkstra(0, n * m - 1)
    def minimumEffortPath3(self, heights: List[List[int]]) -> int:
        """
            Dijkstra 最短路径
        """
        import heapq
        n, m = len(heights), len(heights[0])
        q = [(0, 0, 0)]
        dist = [float('inf')] * (n * m)
        seen = set()

        def check(x, y):
            if 0 <= x < n and 0 <= y < m: return True
            return False

        def dijkstra(start, end):
            dist[start] = 0
            while q:  # 总共要收集n个节点
                # 1 找到dist中最小值
                d, x, y  = heapq.heappop(q)
                iden = x*m+y
                if iden in seen: continue
                # 2 标记minDist顶点已被访问
                seen.add(iden)
                if x * m + y == end: break  # 已找到终点
                # 3 访问minDist顶点的邻接点
                for nx, ny in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                    if not check(nx, ny): continue  # 越界访问
                    curHeightDiffAbs = abs(heights[nx][ny] - heights[x][y])
                    if max(d, curHeightDiffAbs) < dist[nx * m + ny]:  # 更新为更短路径
                        dist[nx * m + ny] = max(d, curHeightDiffAbs)
                        heapq.heappush(q, (int(dist[nx * m + ny]), nx, ny))
                        # dist[nx * n + ny][0] = d + heights[nx][ny]
            # print(dist)
            # print(seen)
            return int(dist[m * n - 1])

        return dijkstra(0, n * m - 1)
if __name__ == '__main__':
    # heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    # heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]

    print(Solution().minimumEffortPath(heights))
    print(Solution().minimumEffortPath2(heights))
    # ab = [(1.0,1.0,1),(2.0,3,4.9)]
    # for i,(a,b,c) in enumerate(ab):
    #     print(i,a,b,c)
