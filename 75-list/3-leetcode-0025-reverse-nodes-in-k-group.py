# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """ 新链表保存结果 """
        if not head or not head.next: return head
        dummy = ListNode(-1)
        new_tail = dummy
        prev = head  # 一组左端点的前一个节点
        tail = head
        while prev and tail.next:
            # 找到一组的右端点
            for i in range(k-1):
                tail = tail.next  # 控制tail为空
                if not tail:
                    break
            if not tail: return dummy.next
            # 反转从prev.next到tail
            p = prev
            next_start = tail.next
            prev_local = tail.next
            while p != next_start:  # 包含最后一组刚好到tail
                tmp = p.next
                p.next = prev_local
                prev_local = p
                p = tmp
            # 将反转后的子链表接到之前处理好的链表的末尾
            new_tail.next = prev_local
            new_tail = prev
            tail = next_start
            prev = next_start
        return dummy.next
    def reverseKGroup2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """ 原链表反转 """
        dummy = ListNode(-1, head)
        prev = dummy  # 一组左端点的前一个节点
        tail = dummy
        while tail.next:
            # 找到一组的右端点
            for i in range(k):
                tail = tail.next  # 控制tail为空
                if not tail: return dummy.next
            # 反转从prev.next到tail
            p = prev.next
            nextPrev = prev.next
            prev_local = tail.next  # 反转操作的第一个节点要指向下一组的开头，当最后不够一组时，直接接上原始剩余即可
            nextStart = tail.next # tail是当前组最后一个元素，在反转处理的最后一个操作会被修改tail.next
            while p != nextStart:  # 包含最后一组刚好到tail
                tmp = p.next
                p.next = prev_local
                prev_local = p
                p = tmp
            # 将反转后的子链表接到之前处理好的链表的末尾
            prev.next = prev_local
            prev = nextPrev
            tail = nextPrev
        return dummy.next

    def show(self,head):
        p= head
        while p:
            print(p.val)
            p = p.next


if __name__ == '__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    k = 2
    # new_head = Solution().reverseKGroup(head, k)
    new_head = Solution().reverseKGroup2(head, k)
    p = new_head
    while p:
        print(p.val)
        p = p.next
    print(new_head)
