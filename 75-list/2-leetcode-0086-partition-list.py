# Definition for singly-linked list.
from jedi.inference.helpers import get_int_or_none


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """ 链表 插入排序 """
        dummy = ListNode(-1, head)
        lessHead = ListNode(-1)
        greaterHead = ListNode(-1)
        lessTail = lessHead
        greaterTail = greaterHead
        cur = dummy.next
        while cur:
            tmp = cur.next
            cur.next = None
            if cur.val < x:
                lessTail.next = cur
                lessTail = lessTail.next
            else:
                greaterTail.next = cur
                greaterTail = greaterTail.next
            cur = tmp
        lessTail.next = greaterHead.next
        return lessHead.next




if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5, ListNode(2))

    head = Solution().partition(head, 3)
    while head:
        print(head.val)
        head = head.next
