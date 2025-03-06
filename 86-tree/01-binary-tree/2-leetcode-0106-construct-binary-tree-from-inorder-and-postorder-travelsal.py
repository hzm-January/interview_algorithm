# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def backtrack(inLeft, inRight, postLeft, postRight):
            if postLeft > postRight:  # 2 终止条件
                return None
            # 当前根节点
            curRootVal = postorder[postRight]
            curRoot = TreeNode(curRootVal)
            # 在中序中寻找根节点
            i = inLeft
            while i<=inRight and inorder[i]!=curRootVal:i+=1
            # 回溯
            curRoot.left = backtrack(inLeft, i - 1, postLeft, postLeft + (i - inLeft) -1)
            curRoot.right = backtrack(i + 1, inRight, postLeft + (i - inLeft) , postRight - 1)
            return curRoot
        return backtrack(0, len(inorder)-1, 0, len(postorder) - 1)

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def backtrack(inLeft, inRight, postLeft, postRight):
            if postLeft > postRight:  # 2 终止条件
                return None
            # 当前根节点
            curRootVal = postorder[postRight]
            curRoot = TreeNode(curRootVal)
            # 在中序中寻找根节点
            i = inorder.index(curRootVal)
            # 回溯
            curRoot.left = backtrack(inLeft, i - 1, postLeft, postLeft + (i - inLeft)-1)
            curRoot.right = backtrack(i + 1, inRight, postLeft + (i - inLeft) , postRight - 1)
            return curRoot

        return backtrack(0, len(inorder) - 1, 0, len(postorder) - 1)
    def buildTree3(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def backtrack(inLeft, inRight, postLeft, postRight):
            if postLeft > postRight:  # 2 终止条件
                return None
            # 当前根节点
            curRootVal = postorder[postRight]
            curRoot = TreeNode(curRootVal)
            # 在中序中寻找根节点
            i = hash[curRootVal]
            # 回溯
            curRoot.left = backtrack(inLeft, i - 1, postLeft, postLeft + (i - inLeft)-1)
            curRoot.right = backtrack(i + 1, inRight, postLeft + (i - inLeft), postRight - 1)
            return curRoot
        hash={element:i for i, element in enumerate(inorder)}
        return backtrack(0, len(inorder) - 1, 0, len(postorder) - 1)


