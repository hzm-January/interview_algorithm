# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ 层序遍历 双端队列 反转数组 """
        if not root: return []
        ans = []
        queue = [root]
        level = 0
        while queue:
            size = len(queue)
            cur_level_ans = []
            for _ in range(size):
                node = queue.pop(0)
                cur_level_ans.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if level % 2 == 0:
                ans.append(cur_level_ans)
            else:
                ans.append(cur_level_ans[::-1])
            level += 1

        return ans

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            层序遍历 双端队列
            优化 数组反转 的复杂度，在元素添加时就规定顺序
        """
        if not root: return []
        ans = []
        queue = [root]
        level = 0
        while queue:
            size = len(queue)
            cur_level_ans = []
            for _ in range(size):
                node = queue.pop(0)
                if level % 2 == 0:
                    cur_level_ans.append(node.val)
                else:
                    cur_level_ans.insert(0, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(cur_level_ans)
            level += 1

        return ans


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))
