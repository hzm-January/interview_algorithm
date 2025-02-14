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

    # 遍历顺序：从后到前，最后的结果保存在根节点中，即dp[0]
    for i in range(3, len(ans)):
        dp[i] = max(dp[(i - 1) // 2], dp[((i - 1) // 2 - 1) // 2] + ans[i])
        print(i, dp[:len(ans)])

    return max(dp)


def rob2(root: Optional[TreeNode]) -> int:
    """
        树形dp
        dp = [0,0] 表示不偷当前层时最大金额dp[0]，偷当前层时最大金额dp[1]
        最终结果保存于根节点，所以需要后序遍历
    """
    def _rob(cur: Optional[TreeNode]) -> list[int]:
        if not cur: return [0, 0]  # 当前节点为空，偷当前节点和不偷当前节点最大金额都为0
        left = _rob(cur.left)
        right = _rob(cur.right)
        val_0 = max(left[0], left[1]) + max(right[0], right[1])  # 不偷当前节点，左右子节点可偷可不偷
        val_1 = cur.val + left[0] + right[0]  # 偷当前节点，左右子节点都不能偷
        return [val_0, val_1]

    ans = _rob(root)
    return max(ans[0], ans[1])


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    # ans = rob(root)
    ans = rob2(root)
    print(ans)
