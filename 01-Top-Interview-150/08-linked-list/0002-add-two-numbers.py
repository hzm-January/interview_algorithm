from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(-1)
    prev = head
    extra = 0
    while l1 and l2:
        sum = l1.val + l2.val + extra
        extra = sum // 10
        prev.next = ListNode(sum % 10)
        prev = prev.next
        l1 = l1.next
        l2 = l2.next
    while l1:
        sum = l1.val + extra
        extra = sum // 10
        prev.next = ListNode(sum % 10)
        prev = prev.next
        l1 = l1.next
    while l2:
        sum = l2.val + extra
        extra = sum // 10
        prev.next = ListNode(sum % 10)
        prev = prev.next
        l2 = l2.next
    if extra:
        prev.next = ListNode(extra)
    return head.next


if __name__ == '__main__':
    head = ListNode(5)
    head.next = ListNode(3)
    head.next.next = ListNode(1)

    head2 = ListNode(6)
    head2.next = ListNode(6)

    ans = addTwoNumbers(head, head2)

    while ans:
        print(ans.val)
        ans = ans.next