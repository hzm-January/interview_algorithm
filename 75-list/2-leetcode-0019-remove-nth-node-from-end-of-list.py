# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy.next
        i = 0
        while fast:
            fast = fast.next
            i += 1
            # 找到倒数第n+1个节点，即倒数第n个节点的前序节点
            # 倒数第n+1个节点到末尾的空节点，总共需要走n+1步
            if i >= n + 1:
                slow = slow.next
        if not slow.next: return head
        slow.next = slow.next.next
        return dummy.next
