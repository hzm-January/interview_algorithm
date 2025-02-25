""" 堆实现 """


class Heap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def build(self, nums: list[int]):
        """ 建堆 """
        n = len(nums)
        for i in range((n - 1) // 2, -1, -1):  # 从最后一个非叶子节点开始
            # 从上往下堆化
            self.heapifyT2B(nums, i)
        print(1, nums)
        self.heap[:] = nums

    def deleteTop(self):
        """ 删除堆顶元素 """
        delVal = self.heap[0]
        if self.__len__() == 1:
            return self.heap.pop()
        self.heap[0] = self.heap.pop()  # 将最后一个元素放在堆顶
        # 从上往下堆化
        self.heapifyT2B(self.heap, 0)
        return delVal

    def heapifyT2B(self, nums: list[int], p: int):
        """ 从上往下堆化 """
        n = len(nums)
        while p * 2 < n:
            maxVal = nums[p * 2]
            if p * 2 + 1 < n:
                maxVal = max(nums[p * 2], nums[p * 2 + 1])
            if nums[p] >= maxVal: break
            if maxVal == nums[p * 2]:
                nums[p], nums[p * 2] = nums[p * 2], nums[p]
                p = p * 2
            else:
                nums[p], nums[p * 2 + 1] = nums[p * 2 + 1], nums[p]
                p = p * 2 + 1
        print('堆化', nums)

    def insert(self, val: int):
        """ 插入元素 """
        self.heap.append(val)
        # 新添加的最后一个元素，从下往上堆化
        self.heapifyB2T(self.__len__() - 1)

    def heapifyB2T(self, p):
        """ 从下往上堆化 """
        while p > 0:
            if self.heap[(p - 1) // 2] > self.heap[p]: break
            self.heap[p], self.heap[(p - 1) // 2] = self.heap[(p - 1) // 2], self.heap[p]
            p = (p - 1) // 2


if __name__ == "__main__":
    heap = Heap()
    nums = [5, 3, 6, 4, 2, 1]
    heap.build(nums)
    print(heap.heap)
    print('------------ delete --------------')
    for i in range(len(nums)):
        print(heap.deleteTop())
    print('------------ insert --------------')
    heap.insert(4)
    heap.insert(2)
    heap.insert(6)
    print(heap.heap)
    heap.insert(3)
    heap.insert(5)
    heap.insert(1)
    print(heap.heap)
