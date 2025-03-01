class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        p = self.head
        for i in range(index + 1):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if self.size == 0 and self.tail is None:
            self.tail = newNode
        self.size = self.size + 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.size == 0 and self.tail is None:
            self.head.next = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.size = self.size + 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        newNode = ListNode(val)
        if index==0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.tail.next = newNode
            self.tail = self.tail.next
        else:
            p = self.head
            for i in range(index):
                p = p.next
            newNode.next = p.next
            p.next = newNode
        self.tail = newNode
        self.size = self.size + 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        p = self.head
        for i in range(index):
            p = p.next
        p.next = p.next.next
        if index==0 and self.size==1 and self.tail:
            self.tail = None
        self.size = self.size - 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
