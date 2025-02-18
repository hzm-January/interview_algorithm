# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next: return False
    p, q = head, head.next
    while q!=p:
        # q!=p前提下，q或q.next说明已到达终点，证明无环
        if not q or not q.next: return False # 只要快指针到达终点，终止运行。
        p = p.next
        q = q.next.next
    return True

def hasCycle2(head: Optional[ListNode]) -> bool:
    if not head or not head.next: return False
    seen = set()
    p = head
    while p:
        if p in seen: return True
        seen.add(p)
        p = p.next
    return False



