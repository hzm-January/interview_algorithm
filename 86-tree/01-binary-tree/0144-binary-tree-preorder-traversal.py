# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ 递归写法 1 """

        def pre_traverse(root, ans):  # 1 回溯函数参数列表和返回值
            if not root:  # 2 终止条件
                return
            # 3 单层搜索逻辑
            ans.append(root.val)
            pre_traverse(root.left, ans)
            pre_traverse(root.right, ans)

        ans = []  # 结果保存数组
        pre_traverse(root, ans)
        return ans

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """
            非递归写法 栈 通俗易懂版
        """
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            if not node: continue
            ans.append(node.val)
            if node.right: stack.append(node.right)  # 先进右，后出右
            if node.left: stack.append(node.left)  # 后进左，先出左
        return ans

    def preorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        """
            非递归 统一写法
        """
        stack, ans = [], []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)  # 访问中，左
                ans.append(cur.val)  # 处理中，左 # 处理右
                cur = cur.left
            cur = stack.pop()  # 访问右
            cur = cur.right
        return ans

    def preorderTraversal4(self, root: Optional[TreeNode]) -> List[int]:
        """
            非递归 统一写法 空指针
        """
        stack, ans = [root], []
        while stack:
            cur = stack.pop()  # 访问cur，此时左右子树都还未处理
            if cur:
                if cur.right: stack.append(cur.right)  # 访问右子树
                if cur.left: stack.append(cur.left)  # 访问左子树
                stack.append(cur)
                stack.append(None)  # 标记cur，表示cur的左右子树已访问待处理，此时先处理中
            else:
                ans.append(stack.pop().val)  # 弹出None后，处理cur
        return ans

    def preorderTraversal5(self, root: Optional[TreeNode]) -> List[int]:
        stack, ans = [(root, False)], []
        while stack:
            cur, vis = stack.pop()
            if vis:
                ans.append(cur.val)
                continue
            if cur.right: stack.append((cur.right, False))
            if cur.left: stack.append((cur.left, False))
            stack.append((cur, True))
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
    print(s.preorderTraversal(root))
    print(s.preorderTraversal2(root))
    print(s.preorderTraversal3(root))
    print(s.preorderTraversal4(root))
    print(s.preorderTraversal5(root))
