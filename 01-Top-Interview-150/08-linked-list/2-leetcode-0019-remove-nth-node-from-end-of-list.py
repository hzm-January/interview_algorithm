# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 快慢指针 """
        if not head: return head
        p, q = head, head
        for i in range(n):
            q = q.next
        if not q:
            # 要删除的是头结点
            head = head.next
            return head
        while q.next:
            p = p.next
            q = q.next
        tmp = p.next
        p.next = tmp.next
        return head

    def removeNthFromEnd_2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 快慢指针 """
        dummy = ListNode(0, head)  # 哨兵节点
        p, q = dummy, dummy.next
        for i in range(n):
            q = q.next
        while q:
            p = p.next
            q = q.next
        p.next = p.next.next
        return dummy.next

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 栈 """
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
        global cur
        for i in range(n):
            cur = stack.pop(-1)
        if not stack:
            head = head.next
            return head
        prev = stack[-1]
        prev.next = cur.next
        return head

    def removeNthFromEnd2_2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 栈 优化写法 """
        stack = []
        dummy = ListNode(0, head)  # 哨兵节点
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop(-1)
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next

    def show(self, head):
        p = head
        while p:
            print(p.val)
            p = p.next

    def removeNthFromEnd3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLength(head: Optional[ListNode]) -> int:
            if not head: return 0
            p = head
            length = 0
            while p:
                length += 1
                p = p.next
            return length
        dummy = ListNode(0, head)
        l = getLength(dummy)
        p = dummy
        for i in range(l - n - 1):
            p = p.next
        p.next = p.next.next
        return dummy.next


if __name__ == '__main__':
    head, n = ListNode(1), 1
    s = Solution()
    # head = s.removeNthFromEnd(head, n)
    # head = s.removeNthFromEnd2(head, n)
    head = s.removeNthFromEnd3(head, n)
    s.show(head)
