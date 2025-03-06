# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def backtrack(preLeft, preRight, inLeft, inRight):  # 1 参数列表与返回值
            # 区间统一：左闭右闭
            # 2 终止条件
            if preLeft > preRight:
                return None
            # 3 单层搜索逻辑
            curRootVal = preorder[preLeft]  # 当前根节点
            curRoot = TreeNode(curRootVal)
            # 在中序序列中找到当前根节点
            i = inLeft
            while i <= inRight and inorder[i] != curRootVal: i += 1
            # 递归构建左右子树
            curRoot.left = backtrack(preLeft + 1, preLeft + (i - inLeft), inLeft, i - 1)
            curRoot.right = backtrack(preLeft + (i - inLeft) + 1, preRight, i + 1, inRight)
            return curRoot

        return backtrack(0, len(preorder) - 1, 0, len(inorder) - 1)

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def backtrack(preLeft, preRight, inLeft, inRight):  # 1 参数列表与返回值
            # 区间统一：左闭右闭
            # 2 终止条件
            if preLeft > preRight:
                return None
            # 3 单层搜索逻辑
            curRootVal = preorder[preLeft]  # 当前根节点
            curRoot = TreeNode(curRootVal)
            # 在中序序列中找到当前根节点
            i = hash[curRootVal]
            # 递归构建左右子树
            curRoot.left = backtrack(preLeft + 1, preLeft + (i - inLeft), inLeft, i - 1)
            curRoot.right = backtrack(preLeft + (i - inLeft) + 1, preRight, i + 1, inRight)
            return curRoot
        hash = {element:i for i, element in enumerate(inorder)}
        return backtrack(0, len(preorder) - 1, 0, len(inorder) - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
