# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            if p.val != q.val: return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)

    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(p, q):
            queue = [(p, q)]
            while queue:
                size = len(queue)
                for i in range(size):
                    p, q = queue.pop(0)
                    if p.val != q.val: return False
                    if ((not p.left and q.left)
                            or (p.left and not q.left)
                            or (not p.right and q.right)
                            or (p.right and not q.right)):
                        return False
                    if p.left and q.left: queue.append((p.left, q.left))
                    if p.right and q.right: queue.append((p.right, q.right))
            return True
        if not p and not q: return True
        if not p or not q: return False
        return bfs(p, q)