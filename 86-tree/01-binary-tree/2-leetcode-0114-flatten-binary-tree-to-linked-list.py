# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        ans = []

        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        p = root
        for i in range(1, len(ans)):
            p.right = TreeNode(ans[i])
            p.left = None
            p = p.right

    def flatten2(self, root: Optional[TreeNode]) -> None:

        # 迭代法 前序遍历
        def preOrder(node):
            stack = [root]
            prev = None
            while stack:
                cur = stack.pop()
                if prev:
                    prev.right = cur
                    prev.left = None
                if cur.left: stack.append(cur.left)
                if cur.right: stack.append(cur.right)
                prev = cur

        return preOrder(root)

    def flatten3(self, root: Optional[TreeNode]) -> None:
        """ 前序节点 """
        cur = root # 该题直接用root处理也可以，这里重新定义一个cur，是为了看的时候不混淆
        while cur:
            if cur.left:  # 左子树非空
                # 寻找左子树中最后一个节点
                p = cur.left
                while p.right:
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
