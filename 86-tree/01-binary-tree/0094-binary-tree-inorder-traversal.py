# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ 回溯 """

        def traverse(cur, ans):  # 1 参数列表与返回值
            if not cur: return  # 2 终止条件
            # 3 单层搜索逻辑
            if cur.left: traverse(cur.left, ans)
            ans.append(cur.val)
            if cur.right: traverse(cur.right, ans)

        ans = []
        traverse(root, ans)
        return ans

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """ 迭代 """
        stack, ans = [], []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans

    def inorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        """ 迭代 统一写法版 """
        stack, ans = [], []
        cur = root
        while cur or stack:
            while cur:  # 访问 中，左，右
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()  # 处理 左，中，右
            ans.append(cur.val)  # 处理 左，中，右
            cur = cur.right  # 访问右
        return ans

    def inorderTraversal4(self, root: Optional[TreeNode]) -> List[int]:
        """ 迭代法 卡尔版 统一写法 空指针 """
        stack, ans = [root], []
        while stack:
            cur = stack.pop()
            if cur:
                # 当前节点的左右子节点还未被访问
                # 右子树入栈
                if cur.right: stack.append(cur.right)
                stack.append(cur)
                stack.append(None)  # 标记cur，表示cur的左右子节点已经入栈
                # 左子树入栈
                if cur.left: stack.append(cur.left)
            else:
                # 当前节点为None，说明下一个栈顶元素的左右节点已经被访问过，可以进行处理了
                ans.append(stack.pop().val)  # 处理当前节点
        return ans

    def inorderTraversal5(self, root: Optional[TreeNode]) -> List[int]:
        """ 迭代法 卡尔版 统一写法 bool标记 """
        stack, ans = [(root, False)], []
        while stack:
            cur, vis = stack.pop()
            if vis: # 当前节点的左右子树已被处理
                ans.append(cur.val) # 处理当前节点
                continue # 防止重复处理左右子树
            if cur.right: stack.append((cur.right, False)) # 访问右子树
            stack.append((cur, True)) # 访问当前节点
            if cur.left: stack.append((cur.left, False)) # 访问左子树
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
    print(s.inorderTraversal(root))
    print(s.inorderTraversal2(root))
    print(s.inorderTraversal3(root))
    print(s.inorderTraversal4(root))
    print(s.inorderTraversal5(root))
