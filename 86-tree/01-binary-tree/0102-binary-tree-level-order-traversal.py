# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1 定义队列
        queue = []
        if root: queue.append(root)  # 将根节点添加到队列
        ans = []
        while queue:
            size = len(queue)  # 更新记录当前层节点数
            tmp = []
            while size:
                node = queue.pop(0)  # 处理节点
                tmp.append(node.val)  # 处理节点
                if node.left: queue.append(node.left)  # 访问节点，将当前节点的子节点添加到队列
                if node.right: queue.append(node.right)  # 访问节点，将当前节点的子节点添加到队列
                size -= 1
            ans.append(tmp)
        return ans

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1 定义队列
        queue = []
        if root: queue.append(root)  # 将根节点添加到队列
        ans = []
        while queue:
            size = len(queue)  # 更新记录当前层节点数
            tmp = []
            for i in range(size):
                node = queue.pop(0)  # 处理节点
                tmp.append(node.val)  # 处理节点
                if node.left: queue.append(node.left)  # 访问节点，将当前节点的子节点添加到队列
                if node.right: queue.append(node.right)  # 访问节点，将当前节点的子节点添加到队列
            ans.append(tmp)
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.levelOrder(root))
