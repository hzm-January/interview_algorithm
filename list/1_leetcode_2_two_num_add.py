# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        p, q, carry = l1, l2, 0
        head = ListNode(-1)
        pre = head
        while p or q or carry != 0:
            if p:
                ip = p.val
            else:
                ip = 0
            if q:
                iq = q.val
            else:
                iq = 0
            sum = ip + iq + carry
            pre.next = ListNode(sum % 10)
             
            pre = pre.next
            if p:
                p = p.next
            if q:
                q = q.next
        return head.next
