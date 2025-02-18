# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """ 广度优先遍历 """
        ans = []

        def bfs(node):
            queue = [node]
            while queue:
                size = len(queue)
                for i in range(size):
                    node = queue.pop(0)
                    if i == size - 1:
                        ans.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)

        if not root: return []
        bfs(root)
        return ans

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans_dic = dict()
        stack = [(root, 0)]
        max_level = 0  # 定义为0，默认root存在，上面必须处理root为空的情况
        while stack:
            node, level = stack.pop()
            if not node: continue
            max_level = max(max_level, level)
            ans_dic.setdefault(level, node.val)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))
        ans = []
        for i in range(max_level + 1):
            ans.append(ans_dic[i])
        return ans

    def rightSideView3(self, root: Optional[TreeNode]) -> List[int]:
        """ 深度优先遍历 """
        ans_dic = dict()
        stack = [(root, 0)]
        max_level = -1  # 定义为-1，简化了root=None的情况
        while stack:
            node, level = stack.pop()
            if not node: continue
            max_level = max(max_level, level)
            ans_dic.setdefault(level, node.val)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))
        return [ans_dic[i] for i in range(max_level + 1)]
