# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:


    def __init__(self, root: Optional[TreeNode]):
        self.tree = []
        self.inorder2(root)
        self.index = -1

    def inorder(self, node):
        """ 二叉树 递归 中序遍历 """
        if not node:
            return
        self.inorder(node.left)
        self.tree.append(node.val)
        self.inorder(node.right)

    def inorder2(self, node):
        """ 二叉树 迭代 中序遍历 """
        stack = []
        cur = node
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            self.tree.append(cur.val)
            cur = cur.right



    def next(self) -> int:
        self.index +=1
        return self.tree[self.index]

    def hasNext(self) -> bool:
        return 0<=self.index+1<len(self.tree)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()