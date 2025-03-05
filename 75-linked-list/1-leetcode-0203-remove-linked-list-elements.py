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
        sentinel = ListNode(-1, head)
        prev = sentinel
        p = prev.next
        while p:
            if p.val == val:
                prev.next = p.next
            else:
                prev = p
            p = p.next
        return sentinel.next

    def removeElements3(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
            迭代法 优化
            从前往后处理
        """
        sentinel = ListNode(-1, head)
        p = sentinel
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            p = p.next
        return sentinel.next

    def removeElements3(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
            迭代法 无哨兵
            从前往后处理
        """
        p = head
        # 处理头结点：找到第一个值不为val的节点
        while p and p.val == val:
            p = p.next
        head = p  # 更新head为第一个不为val的节点
        # 处理之后的节点
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return head

    def removeElements3_2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
            迭代法 无哨兵
            从前往后处理
        """
        # 处理头结点：找到第一个值不为val的节点，更新head为第一个不为val的节点
        while head and head.val == val:
            head = head.next
        # 处理之后的节点
        p = head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return head

    def removeElements2(self, head, val):
        """
            递归法
            从后往前处理
        """

        def backtrack(head, val):
            if head == None:
                return None
            head.next = backtrack(head.next, val)  # 值得学习，一直递归到最后一个节点
            return head.next if head.val == val else head
