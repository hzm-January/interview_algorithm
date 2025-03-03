# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> list[int]:
        """ 迭代法 中序遍历 """
        stack = [(root, False)]
        min_diff = float('inf')
        prev = None
        while stack:
            top, vis = stack.pop()
            if vis:
                if prev is not None:
                    min_diff = min(min_diff, abs(top.val - prev))
                prev = top.val
                continue
            if top.right: stack.append((top.right, False))
            stack.append((top, True))
            if top.left: stack.append((top.left, False))
        return min_diff

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> list[int]:
        """ 迭代法 中序遍历 """
        stack = []
        prev = None
        min_diff = float('inf')
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            top = stack.pop()
            if prev is not None:
                min_diff = min(min_diff, abs(top.val - prev))
            prev = top.val
            p = top.right

        return min_diff

    def getMinimumDifference3(self, root: Optional[TreeNode]) -> list[int]:
        """ 迭代法 空指针 """
        stack = [root]
        prev = None
        min_diff = float('inf')
        while stack:
            cur = stack.pop()
            if cur:
                # 当前节点的左右子节点还未被访问
                if cur.right: stack.append(cur.right)
                stack.append(cur)
                stack.append(None)
                if cur.left: stack.append(cur.left)
            else:
                # 当前节点为None，说明下一个栈顶元素的左右节点已经被访问过，可以进行处理了
                top = stack.pop()
                if prev is not None:
                    min_diff = min(min_diff, abs(top.val - prev))
                prev = top.val
        return min_diff

    def getMinimumDifference4(self, root: Optional[TreeNode]) -> list[int]:
        """ 递归法 中序遍历 """

        def inorder(node, prev, min_diff):
            if not node:
                return
            inorder(node.left, prev, min_diff)
            if prev[0] is not None:
                min_diff[0] = min(min_diff[0], abs(node.val - prev[0]))
            prev[0] = node.val
            inorder(node.right, prev, min_diff)

        prev = [None]
        min_diff = [float('inf')]
        inorder(root, prev, min_diff)
        return min_diff[0]


if __name__ == "__main__":
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)

    root = TreeNode(4)
    root.left = TreeNode(5)
    root.right = TreeNode(7)

    print(Solution().getMinimumDifference(root))
    print(Solution().getMinimumDifference2(root))
    print(Solution().getMinimumDifference3(root))
    print(Solution().getMinimumDifference4(root))
