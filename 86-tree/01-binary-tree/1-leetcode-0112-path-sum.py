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
            dfs
            易错测试样例 [1,2],target=1 ->False，因为1不是叶子结点
        """

        def dfs(node: Optional[TreeNode], sum):
            if not node: return False
            if not node.left and not node.right:  # 必须是叶子结点，测试样例[1,2] target 1
                if sum + node.val == targetSum:
                    return True
                else:
                    return False
            dfsleft = dfs(node.left, sum + node.val)
            dfsright = dfs(node.right, sum + node.val)
            return dfsleft or dfsright

        if not root: return False
        return dfs(root, 0)

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
            dfs - 写法优化
            易错测试样例 [1,2],target=1 ->False，因为1不是叶子结点
        """

        def dfs(node: Optional[TreeNode], sum):
            if not node: return False
            if not node.left and not node.right:  # 必须是叶子结点，测试样例[1,2] target 1
                return sum + node.val == targetSum
            return dfs(node.left, sum + node.val) or dfs(node.right, sum + node.val)

        if not root: return False
        return dfs(root, 0)

    def hasPathSum3(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
            dfs
            target-- 写法
        """

        def dfs(node: Optional[TreeNode], sum):
            if not node: return False
            if not node.left and not node.right:  # 必须是叶子结点，测试样例[1,2] target 1
                return sum == node.val
            return dfs(node.left, sum - node.val) or dfs(node.right, sum - node.val)

        if not root: return False
        return dfs(root, targetSum)

    def hasPathSum4(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
            dfs 卡尔 通俗易懂版
            target-- 写法
        """

        def dfs(node: Optional[TreeNode], sum):
            if not node: return False
            if not node.left and not node.right:  # 必须是叶子结点，测试样例[1,2] target 1
                return sum == node.val
            if node.left:
                sum -= node.val
                if dfs(node.left, sum): return True
                sum += node.val
            if node.right:
                sum -= node.val
                if dfs(node.right, sum): return True
                sum += node.val
            return False

        if not root: return False
        return dfs(root, targetSum)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.right = TreeNode(3)
    s = Solution()
    # ans = s.hasPathSum(root, 1)
    ans = s.hasPathSum4(root, 1)
    print(ans)
