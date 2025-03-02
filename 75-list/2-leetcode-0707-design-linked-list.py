"""
    值得学习
    边界条件的确定：卡尔版-代入极端情况看看是否符合条件，例如1,0等

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
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
        if self.size == 0: # 如果链表为空进行添加后，更新尾节点
            self.tail = newNode
        self.size = self.size + 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        self.size = self.size + 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        newNode = ListNode(val)
        if index == 0: # 在链表头添加
            self.addAtHead(val)
            return
        if index == self.size: # 在链表尾添加
            self.addAtTail(val)
            return
        # 在链表中间添加
        p = self.head
        for i in range(index):
            p = p.next
        newNode.next = p.next
        p.next = newNode
        self.size = self.size + 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        p = self.head
        for i in range(index):
            p = p.next
        p.next = p.next.next
        if index == self.size - 1:  # 如果删除的尾部
            self.tail = p
        self.size = self.size - 1
        if self.size == 0 and self.tail != self.head:  # 如果删除后链表变为空
            self.tail = self.head

    def show(self):
        p = self.head
        i = 0
        while p:
            i += 1
            p = p.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
