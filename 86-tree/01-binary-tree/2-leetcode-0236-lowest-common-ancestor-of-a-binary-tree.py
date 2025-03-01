# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def LCA(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root
            left = LCA(root.left, p, q)
            right = LCA(root.right, p, q)
            if left and right: # 左右都不空，当前节点就是公共祖先，返回当前节点
                return root
            # 左右有一个空，返回不空的那个，左右都空，返回一个空
            # 如果q在p的子树中，q就是公共祖先 ，那么会一直返回q
            return left if left else right

        return LCA(root, p, q)
