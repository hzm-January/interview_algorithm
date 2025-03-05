class LinkedNode:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.tail = LinkedNode()
        self.head = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # key不在cache中
        if key not in self.cache:
            return -1
        # key在cache中
        node = self.cache[key]
        self.removeNode(node)
        self.addToHead(node)
        return self.cache[key].val

    def removeNode(self, node):
        # 将key对应的node添加到表头
        # 1 抽离出node prev<->next
        prev = node.prev  # prev
        next = node.next  # next
        prev.next = next  # prev->next
        next.prev = prev  # prev<-next


    def addToHead(self, node):
        # 2 头结点插入node h<->h1 h<->new<->h1
        next = self.head.next # h1
        node.next = next  # new->h1
        if next: # h1 is Not None
            next.prev = node  # new<-h1
        self.head.next = node  # h->new
        node.prev = self.head  # h<-new

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.addToHead(node)
            return
        # 新建节点
        node = LinkedNode(key, value)
        # 插入头部
        # self.removeNode(node)
        self.addToHead(node)
        self.cache[key] = node
        # 检查缓存大小是否超限
        if len(self.cache) <= self.capacity:
            return
        # print('+'*50)
        # self.show()
        # print('+'*50)
        # 超限
        self.removeTail()

    def removeTail(self):
        # 1 删除表尾 t2<->t1<->t t2<->t
        tail = self.tail.prev  # t1
        prev = tail.prev  # t2
        prev.next = self.tail  # t2->t
        self.tail.prev = prev  # t2<-t
        self.cache.pop(tail.key)

    def show(self):
        p = self.head.next
        left = []
        while p and p!=self.tail:
            left.append(p.val)
            p = p.next
        q = self.tail.prev
        right = []
        while q and q!=self.head:
            right.insert(0,q.val)
            q=q.prev
        print('left',left)
        print('right',right)
        print('capacity',self.capacity)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.show()
    print('-'*50)
    val = cache.get(1)
    print(1, val)
    cache.show()
    print('-'*50)
    cache.put(3, 3)
    cache.show()
    print('-'*50)
    val=cache.get(2)
    print(val)
    print('-' * 50)
    cache.put(4, 4)
    cache.show()
    val = cache.get(1)
    print(val)
    val = cache.get(3)
    print(val)
    val = cache.get(4)
    print(val)