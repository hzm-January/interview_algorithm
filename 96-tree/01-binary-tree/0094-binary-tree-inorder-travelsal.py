# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ 回溯 """
        def traverse(cur, ans): # 1 参数列表与返回值
            if not cur: return # 2 终止条件
            # 3 单层搜索逻辑
            if cur.left: traverse(cur.left, ans)
            ans.append(cur.val)
            if cur.right: traverse(cur.right, ans)
        ans =[]
        traverse(root, ans)
        return ans

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """ 迭代 """
        stack,ans=[],[]
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans

    def inorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        """ 迭代 统一写法版 """
        stack,ans=[],[]
        cur = root
        while cur or stack:
            while cur: # 访问 中，左，右
                stack.append(cur)
                cur = cur.left
            cur = stack.pop() # 处理 左，中，右
            ans.append(cur.val) # 处理 左，中，右
            cur = cur.right # 访问右
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.inorderTraversal(root))
    print(s.inorderTraversal2(root))
    print(s.inorderTraversal3(root))