# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ 回溯 """

        def traverse(cur, ans):  # 1 回溯函数参数列表与返回值
            if not cur: return  # 2 终止条件
            # 3 单层搜索逻辑
            if cur.left: traverse(cur.left, ans)
            if cur.right: traverse(cur.right, ans)
            ans.append(cur.val)

        ans = []
        traverse(root, ans)
        return ans

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """ 非递归 迭代"""
        stack, ans = [root], []
        while stack:
            cur = stack.pop()
            if not cur: continue
            ans.append(cur.val)
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)
        ans.reverse()
        return ans

    def postorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        """ 迭代 """
        stack, ans = [], []
        cur = root
        prev = None
        while cur or stack:
            while cur: # 访问 中，左， 右
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]
            if cur.right and cur.right!=prev: # right 已经处理过
                cur = cur.right
            else:
                ans.append(cur.val) # 处理 左，右， 中
                stack.pop()
                prev = cur
                cur = None
        return ans

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    s = Solution()
    print(s.postorderTraversal(root))
    print(s.postorderTraversal2(root))
    print(s.postorderTraversal3(root))
