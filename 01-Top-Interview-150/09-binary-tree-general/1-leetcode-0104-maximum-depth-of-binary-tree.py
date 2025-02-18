# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ 深度优先搜索 """

        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return max(left, right) + 1

        return dfs(root)

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        """ 广度优先搜索 """

        def bfs(node):
            queue = [node]
            ans = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.pop(0)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                ans += 1
            return ans
        if root is None: return 0
        return bfs(root)