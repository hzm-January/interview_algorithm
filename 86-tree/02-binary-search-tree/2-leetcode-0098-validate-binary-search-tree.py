# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """ 中序遍历 非递归写法1 """
        stack = []
        prev = None
        p=root
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if prev and prev.val>=p.val:
                return False
            prev=p
            p = p.right
        return True