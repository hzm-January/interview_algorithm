# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: Optional[TreeNode]) -> int:
    return -1


if __name__ == '__main__':
    root = None
    ans = rob(root)
    print(ans)
