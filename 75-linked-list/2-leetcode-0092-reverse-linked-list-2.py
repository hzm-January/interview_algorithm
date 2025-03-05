# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        dummy = ListNode(-1, head)
        p = dummy.next
        prev = dummy
        left_prev = dummy  # left的前序节点
        while p:
            if i == left:  # 左边界，找到并记录 left的前序节点left_prev
                left_prev = prev
            if i < left or i > right:  # 不在反转范围，i>right可以直接终止执行，因为反转并拼接完成是在原链表上直接修改的，right后无需再处理
                prev = p  # 记录
                p = p.next  # 迭代
            else:  # 在反转范围内，反转
                tmp = p.next
                p.next = prev
                prev = p
                p = tmp

            if i == right:  # 右边界，将反转完成的子链表接到 left的前序节点left_prev后
                tmp = left_prev.next
                left_prev.next = prev
                tmp.next = p  # 并将left的下一个节点指定到right的下一个节点，此时p指向的就是right的下一个节点
            i += 1
        return dummy.next

    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """ 头插法 只处理反转区间 """
        dummy = ListNode(-1, head)
        prev = dummy # left的前序节点
        for i in range(1, left):
            prev = prev.next

        cur = prev.next
        for _ in range(left, right): # 头插操作只需要right-left次，例如4-2=2次
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = prev.next
            prev.next = tmp
        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # head = Solution().reverseBetween(head, 2, 4)
    head = Solution().reverseBetween2(head, 2, 4)

    p = head
    while p:
        print(p.val)
        p = p.next
