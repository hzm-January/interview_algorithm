# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: Optional[TreeNode]) -> int:
    """ 
        错误代码
    """
    # 树层序遍历
    if not root: return 0
    queue, ans = [root], []
    while queue:
        size = len(queue)
        for i in range(size - 1, -1, -1):
            node = queue.pop(0)
            ans.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    print(ans)
    dp = [0] * (10 ** 4 + 10)

    dp[0] = root.val
    dp[1] = max(root.val, root.left.val)
    dp[2] = max(root.val, root.right.val)
    for i in range(3, len(ans)):
        dp[i] = max(dp[(i - 1) // 2], dp[((i - 1) // 2 - 1) // 2] + ans[i])
        print(i, dp[:len(ans)])

    return max(dp)



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    ans = rob(root)
    print(ans)
