# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """ 这种写法不能通过测试样例 """
        ans = []

        def bfs(node):
            queue = [node]
            while queue:
                size = len(queue)
                mean = 0.0
                for i in range(size):
                    node = queue.pop(0)
                    mean += node.val / size  # 避免累计和过大。这种写法不能通过一个测试样例
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                ans.append(mean)

        if not root: return []
        bfs(root)
        return ans

    def averageOfLevels2(self, root: Optional[TreeNode]) -> List[float]:
        """ 广度优先遍历 """
        ans = []

        def bfs(node):
            queue = [node]
            while queue:
                size = len(queue)
                sum = 0.0
                for i in range(size):
                    node = queue.pop(0)  # 处理节点
                    sum += node.val  # 处理节点
                    if node.left: queue.append(node.left)  # 访问节点
                    if node.right: queue.append(node.right)  # 访问节点
                ans.append(sum / size)

        if not root: return []
        bfs(root)
        return ans

    def averageOfLevels3(self, root: Optional[TreeNode]) -> List[float]:
        """ 深度优先遍历 """
        ans = dict()

        def dfs(node, level):
            if not node:
                return
            from operator import add
            ans[level] = tuple(map(add, ans.get(level, (0, 0)), (node.val, 1)))
            if node.left: dfs(node.left, level + 1)
            if node.right: dfs(node.right, level + 1)
        dfs(root, 0)
        return [sum / size for (sum, size) in ans.values()]

if __name__ == '__main__':
    print((1,1)+(3,2))
    from operator import add
    print(tuple(map(add,(1,1),(3,2))))

    arr = [(1,2),(3,4)]
    for (a,b)in arr:
        print(a,b)
        print(a/b)

    print('-'*10)
    dic = {'1':(1,2),'2':(3,4)}
    for (a,b) in dic.values():
        print(a,b)
        print(a/b)