# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ 深度优先搜索 """
        def dfs(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)

        dfs(root)
        return root

    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ 广度优先搜索 """
        def bfs(node):
            queue = [node]
            while queue:
                size = len(queue)
                for i in range(size):
                    node = queue.pop(0)
                    node.left, node.right = node.right, node.left
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
        if not root: return None
        bfs(root)
        return root

