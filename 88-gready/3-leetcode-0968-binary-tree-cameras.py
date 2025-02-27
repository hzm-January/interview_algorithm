# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
            贪心：叶子节点的父节点安装摄像头

            节点状态：
            0 无覆盖
            1 有摄像头
            2 有覆盖

            状态转移
            case1 左有覆盖 2，且右有覆盖 2 -> 父节点 无覆盖 0
            case2 左右至少一个摄像头 1 -> 父节点 有覆盖 2
            case3 左右至少一个无覆盖 0 -> 父节点 摄像头 1
            case4 根节点需单独处理

            空节点 返回 有覆盖

        :param root:
        :return:
        """
        if root is None: return 0
        ans = [0]

        def dfs(root):
            if not root:
                return 2
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 2 and right == 2:
                root.val = 0
            if left == 1 or right == 1:
                root.val = 2
            if left == 0 or right == 0:
                ans[0] += 1
                root.val = 1
            return root.val

        dfs(root)
        print(root.val)
        if root.val == 0:  # 根节点无监督
            root.val = 1
            ans[0] += 1
        return ans[0]


if __name__ == '__main__':
    # root = TreeNode(0)
    # root.left = TreeNode(0)
    # root.left.left = TreeNode(0)
    # root.left.right = TreeNode(0)

    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.left.left = TreeNode(0)
    root.left.left.left.right = TreeNode(0)
    print(Solution().minCameraCover(root))
