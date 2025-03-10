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

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy
        i = 0
        while fast:
            fast = fast.next
            i += 1
            # 找到倒数第n+1个节点，即倒数第n个节点的前序节点
            # 倒数第n+1个节点到末尾的空节点，总共需要走n+1步
            # 让快指针多走一步到None
            if i > n + 1:
                slow = slow.next
        if not slow.next: return head
        slow.next = slow.next.next
        return dummy.next

    def removeNthFromEnd3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy
        for i in range(n + 1): # TODO：值得学习，用步数，控制链表的迭代
            fast = fast.next # 从0到n，先走了n+1步，1是最后要遍历到倒数第n个节点的前一个节点
        while fast:
            fast = fast.next
            slow = slow.next
        if not slow.next: return head
        slow.next = slow.next.next
        return dummy.next
