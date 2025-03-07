# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """ 图 深度优先搜索 """
        if not node:
            return None

        #
        visited = {}

        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            newNode = Node(node.val)
            visited[node] = newNode
            newNode.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            return newNode

        return dfs(node)

    def cloneGraph3(self, node: Optional['Node']) -> Optional['Node']:
        """ 图 深度优先搜索 """
        # if not node: # 可以不用加，在dfs中node为None是会返回
        #     return None

        #
        visited = {}

        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            newNode = Node(node.val)
            visited[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode

        return dfs(node)

    def cloneGraph2(self, node: Optional['Node']) -> Optional['Node']:
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}

        def dfs2(node):
            if not node:
                return node
            # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
            if node in visited:
                return visited[node]
            # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
            clone_node = Node(node.val, [])
            # 哈希表存储
            visited[node] = clone_node
            # 遍历该节点的邻居并更新克隆节点的邻居列表
            if node.neighbors:
                clone_node.neighbors = [dfs2(n) for n in node.neighbors]
            return clone_node

        return dfs2(node)

    def cloneGraph4(self, node: Optional['Node']) -> Optional['Node']:
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}

        def dfs2(node):
            if not node: return None
            # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
            clone_node = Node(node.val, [])
            # 哈希表存储
            visited[node] = clone_node
            # 遍历该节点的邻居并更新克隆节点的邻居列表
            for neighbor in node.neighbors:
                if neighbor in visited:
                    # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
                    newNode = visited[neighbor]
                else:
                    newNode = dfs2(neighbor)
                clone_node.neighbors.append(newNode)
            return clone_node

        return dfs2(node)

    def cloneGraph4_2(self, node: Optional['Node']) -> Optional['Node']:
        """ 广度优先遍历 """
        visited = {}

        def dfs2(node):
            if not node: return None
            # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
            clone_node = Node(node.val, [])
            # 哈希表存储
            visited[node] = clone_node
            # 遍历该节点的邻居并更新克隆节点的邻居列表
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dfs2(neighbor)
                clone_node.neighbors.append(visited[neighbor])

            return clone_node

        return dfs2(node)

    def cloneGraph5(self, node: Optional['Node']) -> Optional['Node']:
        """ 广度优先遍历 """
        if not node: return node
        visited = {}
        queue = [node] # 队列记录的是旧节点
        visited[node] = Node(node.val) # visited记录的是旧节点对应的新节点
        while queue:
            curNode = queue.pop(0)
            for neighbor in curNode.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = Node(neighbor.val)
                visited[curNode].neighbors.append(visited[neighbor])
        return visited[node]
