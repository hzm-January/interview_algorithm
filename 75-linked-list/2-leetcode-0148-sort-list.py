# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 链表归并排序 自底向上 """

        def merge(head1, head2):
            dummy = ListNode(-1, None)
            tail = dummy
            p, q = head1, head2
            while p and q:
                if p.val <= q.val:
                    tail.next = p
                    p = p.next
                else:
                    tail.next = q
                    q = q.next
                tail = tail.next
            if p:
                tail.next = p
            if q:
                tail.next = q
            return dummy.next

        if not head: return head
        # 统计链表中节点总数
        n = 0
        p = head
        while p:
            p = p.next
            n += 1

        # 归并排序 自底向上
        dummy = ListNode(-1, head)
        size = 1
        while size < n:  # 外层控制：每次迭代的子数组长度
            prev, cur = dummy, dummy.next
            while cur:  # 内层控制：每次归并逻辑要扫过整个链表，cur从head到tail
                # 找到[left,mid]
                head1 = cur
                for i in range(1, size):
                    if not cur.next:
                        break
                    cur = cur.next
                head2 = cur.next
                cur.next = None  # 前一段切断

                # 找到[mid,right]
                cur = head2
                for i in range(1, size):
                    if not cur or not cur.next:
                        break
                    cur = cur.next

                succ = None  # 下一对归并子数组的开始节点
                if cur:
                    succ = cur.next
                    cur.next = None  # 第二段切断

                sorted = merge(head1, head2)

                # 将已经排好序的链表接在prev后面
                prev.next = sorted
                # 找到下一个prev，即当前归并排序子数组最后一个节点
                while prev.next:
                    prev = prev.next
                # 更新游标
                cur = succ  # 下一对归并子数组的开始节点
            size <<= 1
        return dummy.next

    def sortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 迭代法 归并排序 自顶向下  """

        def merge(head1, head2):
            dummy = ListNode(-1, None)
            p, q, tail = head1, head2, dummy
            while p and q:
                if p.val <= q.val:
                    tail.next = p
                    p = p.next
                else:
                    tail.next = q
                    q = q.next
                tail = tail.next
            if p:
                tail.next = p
            if q:
                tail.next = q
            return dummy.next

        def sort(head, tail): # 处理head~tail-1
            if not head: return head
            if head.next == tail:  # 当前链表只有一个子节点
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast!=tail:
                    fast = fast.next
            # 此时慢指针指向链表中点的节点
            mid = slow
            return merge(sort(head, mid), sort(mid, tail))

        return sort(head, None)


if __name__ == '__main__':
    head = ListNode(4, None)
    head.next = ListNode(2, None)
    head.next.next = ListNode(1, None)
    head.next.next.next = ListNode(3, None)

    # head = Solution().sortList(head)
    head = Solution().sortList2(head)

    while head:
        print(head.val)
        head = head.next
