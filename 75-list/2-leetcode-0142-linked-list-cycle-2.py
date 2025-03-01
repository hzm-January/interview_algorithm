# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 快慢指针 """
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if slow == fast:
                break  # 相遇
        if not fast:
            return None
        k = head
        while k != fast:
            k = k.next
            fast = fast.next
        return k

    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 快慢指针 优化 """
        slow, fast = head, head
        while fast:
            slow = slow.next # 慢指针走一步
            fast = fast.next
            if not fast:
                return None
            fast = fast.next # 快指针走两步
            if slow == fast:
                # 有环相遇
                slow = head
                while slow != fast: # 快慢指针每次都走一步，直到相遇就是环入口
                    slow = slow.next
                    fast = fast.next
                return slow # 证明有环且fast==slow==入环点
        # 如果fast为空，证明无环，返回None。
        return None

    def detectCycle3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ visited """
        visited=set()
        while head:
            if head in visited: # 当前节点之前已被访问过
                return head
            visited.add(head)
            head = head.next
        return None
