# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def rob(root: Optional[TreeNode]) -> int:
#     """
#         数组存储树
#         122/124 个测试样例通过，只有2个测试样例不通过
#         失败原因，ans[pos] = cur.val 数组下标越界。
#         可能原因：ans = [-1]*(10**5+10) 10**5+10 长度太少。但是10**6+10会超时
#         失败测试样例：
#         [79,99,77,null,null,null,69,null,60,53,null,73,11,null,null,null,
#         62,27,62,null,null,98,50,null,null,90,48,82,null,null,null,55,64,
#         null,null,73,56,6,47,null,93,null,null,75,44,30,82,null,null,null,
#         null,null,null,57,36,89,42,null,null,76,10,null,null,null,null,null,
#         32,4,18,null,null,1,7,null,null,42,64,null,null,39,76,null,null,6,
#         null,66,8,96,91,38,38,null,null,null,null,74,42,null,null,null,10,
#         40,5,null,null,null,null,28,8,24,47,null,null,null,17,36,50,19,63,
#         33,89,null,null,null,null,null,null,null,null,94,72,null,null,79,25,
#         null,null,51,null,70,84,43,null,64,35,null,null,null,null,40,78,null,
#         null,35,42,98,96,null,null,82,26,null,null,null,null,48,91,null,null,
#         35,93,86,42,null,null,null,null,
#         0,61,null,null,67,null,53,48,null,null,82,30,null,97,null,null,null,1,null,null]
#
#     """
#     # 树层序遍历
#     if not root: return 0
#     ans = [-1]*(10**5+10)
#     max_pos = [0]
#     def tree_traversal(cur: Optional[TreeNode], pos):
#         if not cur:
#             return
#         max_pos[0] = max(max_pos[0], pos)
#         ans[pos] = cur.val
#         tree_traversal(cur.left, 2 * pos + 1)
#         tree_traversal(cur.right, 2 * pos + 2)
#     tree_traversal(root, 0)
#     # print('maxpos',max_pos)
#     # print(ans[:max_pos[0]+1])
#     dp = [[0, 0] for _ in range(10 ** 5 + 10)]
#
#     # 遍历顺序：从后到前，最后的结果保存在根节点中，即dp[0]
#     for i in range(max_pos[0], -1, -1):
#         if ans[i] == -1:
#             dp[i] = [0, 0]
#             ans[i] = 0
#             continue
#         dp[i][0] = max(dp[2 * i + 1][0], dp[2 * i + 1][1]) + max(dp[2 * i + 2][0], dp[2 * i + 2][1])
#         dp[i][1] = dp[2 * i + 1][0] + dp[2 * i + 2][0] + ans[i]
#         # print(dp[:len(ans)])
#     return max(dp[0])


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


# 将链表存储的二叉树转换为数组存储
def tree_to_array(root):
    if not root:
        return []

    result = []
    from collections import deque
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # 去除末尾多余的 None
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.right = TreeNode(1)
    root.right.left = TreeNode(2)
    ans = rob(root)
    print('rob', ans)
    ans = rob2(root)
    print('rob2', ans)
    print(tree_to_array(root))
