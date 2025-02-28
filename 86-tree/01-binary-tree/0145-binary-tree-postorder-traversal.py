# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ 回溯 """

        def traverse(cur, ans):  # 1 回溯函数参数列表与返回值
            if not cur: return  # 2 终止条件
            # 3 单层搜索逻辑
            if cur.left: traverse(cur.left, ans)
            if cur.right: traverse(cur.right, ans)
            ans.append(cur.val)

        ans = []
        traverse(root, ans)
        return ans

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """ 非递归 栈 迭代"""
        stack, ans = [root], []
        while stack:
            cur = stack.pop()
            if not cur: continue
            ans.append(cur.val)
            if cur.left: stack.append(cur.left)  # 先进左，后出左
            if cur.right: stack.append(cur.right)  # 后进右，先出右
        ans.reverse()
        return ans

    def postorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        """ 迭代 """
        stack, ans = [], []
        cur = root
        prev = None  # 记录上一个访问的节点
        while cur or stack:
            while cur:  # 访问 中，左， 右
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]
            # Case 1 当前节点右子节点为空，那么处理当前节点（出栈，加入结果集）
            # Case 2 当前节点右子节点已访问，即上一次处理的节点就是stack[-1]的右子树遍历逻辑完成，其右子节点已出栈，并记录在prev中，那么处理当前节点（出栈，加入结果集）
            if not cur.right or cur.right == prev:
                ans.append(cur.val)  # 处理 左，右， 中
                stack.pop()
                prev = cur  # 标记已访问，防止重复进入右子树
                cur = None  # 防止重复进入左子树
            else:  # 右子树不为空，且上一次访问的节点不是右子节点
                cur = cur.right  # 访问右子树

        return ans

    def postorderTraversal4(self, root: Optional[TreeNode]) -> List[int]:
        """ 迭代 卡尔版 bool 标记法 """
        stack, ans = [(root, False)], []  # 多加一个参数，False 为默认值，表示左右子节点还未访问
        while stack:
            cur, vis = stack.pop()  # 多加一个 visited 参数，使“迭代统一写法”成为一件简单的事
            if vis:  # visited 为 True，表示该节点和两个儿子位次之前已经安排过了，现在可以收割节点了
                ans.append(cur.val)
                continue
            # visited 当前为 False, 表示初次访问本节点，此次访问的目的是“把自己和两个儿子在栈中安排好位次”
            # 后序遍历是'左右中'，节点自己最先入栈，最后出栈。
            # 同时，设置 visited 为 True，表示下次再访问本节点时，允许收割。
            stack.append((cur, True))
            if cur.right: stack.append((cur.right, False))  # 右儿子位置居中
            if cur.left: stack.append((cur.left, False))  # 左儿子最后入栈，最先出栈
        return ans

    def postorderTraversal5(self, root: Optional[TreeNode]) -> List[int]:
        """迭代法 卡尔版 统一写法 空指针 """
        stack, ans = [root], []
        while stack:
            cur = stack.pop()
            if cur:
                stack.append(cur)  # 访问当前节点
                stack.append(None)  # 标记当前节点，表示已经访问了左右子树
                # 访问左右子树
                if cur.right: stack.append(cur.right)  # 访问右子树
                if cur.left: stack.append(cur.left)  # 访问左子树
            else:
                ans.append(stack.pop().val)  # 处理当前节点
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    s = Solution()
    print(s.postorderTraversal(root))
    print(s.postorderTraversal2(root))
    print(s.postorderTraversal3(root))
    print(s.postorderTraversal4(root))
    print(s.postorderTraversal5(root))
