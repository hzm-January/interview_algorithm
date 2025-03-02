# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 指针法 """
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
        """ 指针法 """
        p = head
        prev = None
        # 1-2-3-4
        while p:  # p==2 prev==1
            # backup3 2x3 2-1
            tmp = p.next
            p.next = prev
            # update prev==2
            prev = p
            # update p==3
            p = tmp
        return prev

    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 递归法 """

        def backtrack(prev, cur):
            if cur == None: return prev
            tmp = cur.next
            cur.next = prev
            return backtrack(cur,tmp)

        return backtrack(None,head)
