# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        if not root: return ans[0]

        def dfs(node, s):
            if node.left is None and node.right is None:
                ans[0] += int(s)
                return
            if node.left: dfs(node.left, s + str(node.left.val))
            if node.right: dfs(node.right, s + str(node.right.val))

        dfs(root, str(root.val))
        return ans[0]

    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
        """ DFS 带返回值 """
        def dfs(node, sum):
            if not node:
                return 0

            sum = sum * 10 + node.val # 值得学习，每深一层乘以10
            if node.left is None and node.right is None:
                return sum
            else:
                return dfs(node.left, sum) + dfs(node.right, sum)

        return dfs(root, 0)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().sumNumbers(root))
