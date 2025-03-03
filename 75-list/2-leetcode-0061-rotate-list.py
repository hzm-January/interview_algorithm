# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        dummy = ListNode(-1, head)
        # 统计链表长度
        n = 0
        p = dummy.next
        while p:
            p = p.next
            n += 1
        # 如果移动位数是链表长度的倍数，相当于不移动，直接返回原始值
        if k % n == 0: return dummy.next
        # 快慢指针
        slow, fast = dummy, dummy
        for i in range(k % n):
            fast = fast.next
        # if not fast: return dummy.next #改行可省略，该情况属于k%n==0的情况，在上面已做处理
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        tmp = slow.next
        slow.next = None
        fast.next = dummy.next
        dummy.next = tmp
        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head = Solution().rotateRight(head, 1)
    while head:
        print(head.val)
        head = head.next
