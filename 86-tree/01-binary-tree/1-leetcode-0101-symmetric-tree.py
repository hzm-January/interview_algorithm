# Definition for a binary tree node.
from typing import Optional

"""
    对称二叉树
    该题不能使用【层序遍历】，考虑一种情况：叶子节点都是其父节点的右子节点，且改成中节点组成的数组满足回文，但这一层并不是对称的，因为对称要求左子节点对应右子节点
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            return node1.val == node2.val and dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

        return dfs(root, root)

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        root1, root2 = root, root
        queue = [root1,root2]
        while queue:
            node1, node2 = queue.pop(0), queue.pop(0)
            if not node1 and not node2: continue # 队列中，相邻两值都为空
            if not node1 or not node2: return False # 有一个空一个不空
            if node1.val != node2.val: return False # 相邻两值不相等
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(4)
    print(Solution().isSymmetric(root))
    print(Solution().isSymmetric2(root))
