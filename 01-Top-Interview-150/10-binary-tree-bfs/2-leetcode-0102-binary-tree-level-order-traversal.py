# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def bfs(node):
            queue = [node]
            while queue:
                size = len(queue)
                tmp = []
                for i in range(size):
                    node = queue.pop(0)
                    tmp.append(node.val) # 处理节点
                    if node.left:
                        queue.append(node.left) #  访问节点
                    if node.right:
                        queue.append(node.right) # 访问节点
                ans.append(tmp)
        if not root: return []
        bfs(root)
        return ans
