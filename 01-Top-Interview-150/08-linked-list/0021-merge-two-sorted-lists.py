# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    head = ListNode(-1)
    prev = head
    p, q = list1, list2
    while p and q:
        if p.val < q.val:
            prev.next = q
            q=q.next
        else:
            prev.next = p
            p=p.next
        prev = prev.next
    prev.next = p if p else q
    return head.next


def show(l: ListNode):
    p = l
    while p:
        print(p.val)
        p = p.next


if __name__ == '__main__':
    head = ListNode(5)
    head.next = ListNode(3)
    head.next.next = ListNode(1)

    head2 = ListNode(4)
    head2.next = ListNode(2)

    ans = mergeTwoLists(head, head2)

    while ans:
        print(ans.val)
        ans = ans.next
