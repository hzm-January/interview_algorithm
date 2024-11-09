# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        ret = []
        q = collections.deque
        q.append(root)
        while q:
            tmp = []
            for _ in range(len(q)):
                now = q.popleft()
                tmp.append(now.val)
                if now.left: q.appendleft(now.left)
                if now.right: q.appendleft(now.right)
            ret.append(tmp)
        return ret
