# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """ 递归中序遍历 """
        cnt = [0]
        ans = [-1]

        def inorder(root):
            if not root or ans[-1] != -1:  # ans[-1]!=-1是剪枝，没有也能AC，只是耗时长
                return  # ans[-1] != -1 剪枝的是 找到结果后 return 上层再执行inorder(root.right)
            inorder(root.left)
            cnt[0] += 1
            if cnt[0] == k:
                ans[0] = root.val
                return
            inorder(root.right)

        inorder(root)
        return ans[0]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    print(Solution().kthSmallest(root, 1))
