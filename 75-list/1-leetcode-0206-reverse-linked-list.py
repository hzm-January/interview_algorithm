# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        prev = None
        while p.next:
            tmp = p.next
            p.next = prev
            prev = p
            p = tmp
        p.next = prev
        return p
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        prev = None
        while p:
            tmp = p.next
            p.next = prev
            prev = p
            p = tmp
        return prev