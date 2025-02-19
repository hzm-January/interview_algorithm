# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        易错测试样例 [1,2]

        """


        def dfs(node: Optional[TreeNode], sum):
            if not node:
                if sum == targetSum:
                    return True
                else:
                    return False
            dfsleft = dfs(node.left, sum + node.val)
            dfsright = dfs(node.right, sum + node.val)
            return dfsleft or dfsright
        if not root: return False
        return dfs(root, 0)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s = Solution()
    ans = s.hasPathSum(root, 3)
    print(ans)