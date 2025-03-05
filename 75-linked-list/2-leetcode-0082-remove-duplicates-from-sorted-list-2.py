# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            prev：最后一个不重复元素
            cur: 当前处理元素，判断并处理不是重复元素后再添加到prev后面
        """
        if not head: return head
        dummy = ListNode(-1, head)
        prev = dummy
        cur = dummy.next
        flag = False  # 标记 当前cur 是否是重复元素
        while cur:
            if not cur.next:  #
                if not flag:  # 如果当前cur不是重复元素，添加到结果集
                    prev.next = cur
                break
            if cur.val != cur.next.val: # 如果当前元素与下一个元素不重复
                if not flag: # 当前元素不是重复元素
                    prev.next = cur
                    prev = prev.next
                cur = cur.next
                flag = False
            else: # 当前元素与下一个元素相同
                cur.next = cur.next.next # 删除下一个元素
                flag = True # 标记当前元素为重复元素
        if flag:  # 如果cur是重复元素，将最后一个不重复元素的next设置为None
            prev.next = None

        return dummy.next
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            prev：最后一个不重复元素
            cur: 当前处理元素，判断并处理不是重复元素后再添加到prev后面
        """
        if not head: return head
        dummy = ListNode(-1, head)
        prev = dummy
        cur = dummy.next
        flag = False  # 标记 当前cur 是否是重复元素
        while cur.next: # 处理到最后一个元素
            if cur.val != cur.next.val: # 当前元素与下一个元素不重复
                if not flag: # 当前元素不是重复元素
                    prev.next = cur
                    prev = prev.next
                cur = cur.next
                flag = False
            else: # 当前元素与下一个元素相同
                cur.next = cur.next.next # 删除下一个元素
                flag = True # 标记当前元素为重复元素
        if flag:  # cur是重复元素，将最后一个不重复元素prev的next设置为None
            prev.next = None
        else: # cur不是重复元素，将其添加到prev后面
            prev.next = cur
        return dummy.next

    def deleteDuplicates3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            cur 下一个元素和下下个元素判断是否相等重复，如果出现重复，一直找到下一个不重复的第一个元素，将其链接到cur后面
            值得学习：只用一个指针，处理下一个和下下个元素
        """
        if not head: return head
        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next and cur.next.next: # 值得学习，只用一个指针
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val==x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
