# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

'''
最大贡献 Gain: max(自己，自己+左边，自己+右边）
最大路径和 Sum:  max(自己，自己+左边，自己+右边，自己 + 左边 + 右边）
最大路径和是用最大贡献求出，即最大路径和=左最大贡献+自己+右最大贡献
如果最大贡献包含（左边+自己+右边），那么计算最大路径和时会计算为两条路径的和。
例如：以下树的最大路径和为1+10+(15+20)，路径为1->10->15->20
但如果最大贡献包含（左边+自己+右边），那么最大路径和将变为1+10+(15+20+7)，即两条路径9->10->15->20->15->7（错误），因为15与7之间没有边可到达

        10(gain 10+35, sum 9+10+35)
      /    \
     9      20(gain 15+20, sum 15+20+7)
           /  \
          15   7
'''

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def maxGain(node):
            nonlocal maxSum
            if not node:
                return 0
            # 大于0的才算贡献值
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            # 当前节点的最大路径 = leftGain + rightGain + node.val
            maxSum = max(maxSum, leftGain + rightGain + node.val)
            # 当前节点的最大贡献值 = max(leftGain, rightGain) + node.val
            return max(leftGain, rightGain) + node.val


        maxGain(root)
        return int(maxSum)
