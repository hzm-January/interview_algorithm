# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
            迭代法
            从前往后处理
        """
        sentinel=ListNode(-1,head)
        prev = sentinel
        p = prev.next
        while p:
            if p.val==val:
                prev.next=p.next
            else:
                prev = p
            p = p.next
        return sentinel.next

    def removeElements2(self, head, val):
        """
            递归法
            从后往前处理
        """
        def backtrack(head, val):
            if head==None:
                return None
            head.next = backtrack(head.next, val) # 值得学习，一直递归到最后一个节点
            return head.next if head.val==val else head