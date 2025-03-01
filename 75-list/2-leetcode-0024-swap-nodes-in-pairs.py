# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        p = dummy.next
        prev = dummy
        while p and p.next:
            tmp = p.next
            p.next = tmp.next
            tmp2 = tmp.next
            tmp.next = p
            prev.next = tmp
            prev = p
            p = tmp2
        return dummy.next
    def show(self,head):
        p = head
        while p:
            print(p.val)
            p = p.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    Solution().swapPairs(head)


