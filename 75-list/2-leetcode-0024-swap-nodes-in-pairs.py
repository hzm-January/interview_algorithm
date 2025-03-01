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
        # 1-2-3-4
        # 2-1-3-4
        while p and p.next:
            # backup2 1x2 1-3
            tmp = p.next
            p.next = tmp.next
            # backup3 2x3 2-1
            tmp2 = tmp.next
            tmp.next = p
            # prev-2
            prev.next = tmp
            # update prev==1
            prev = p
            # update p==3
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


