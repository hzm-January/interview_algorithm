# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cnt):
            if node is None:
                return 0
            return dfs(node.left, cnt) + dfs(node.right, cnt) + 1
        return dfs(root, 0)

    def countNodes2(self, root: Optional[TreeNode]) -> int:
        def count(node):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            if left==right:
                # 左子树一定是满二叉树，因为节点已经填充到右子树了，左子树必定已经填满了。所以左子树的节点总数我们可以直接得到
                return count(node.right)+(1<<left)
            else:
                # 此时最后一层不满，但倒数第二层已经满了，可以直接得到右子树的节点个数。
                return count(node.left)+(1<<right)

        def depth(node):
            d = 0
            while node:
                d+=1
                node = node.left
            return d
        return count(root)