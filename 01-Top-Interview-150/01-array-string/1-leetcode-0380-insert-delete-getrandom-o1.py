import random


class RandomizedSet:
    """
        hash表：O(1) 插入，O(1) 删除
        变长数组：O(1) 查找
    """
    def __init__(self):
        self._index_dict=dict()
        self._data_list = []

    def insert(self, val: int) -> bool:
        if val in self._index_dict: # 元素在集合中
            return False
        # 元素不在集合中，插入
        self._data_list.append(val)
        self._index_dict[val] = len(self._data_list) - 1
        return True


    def remove(self, val: int) -> bool:
        if val not in self._index_dict:
            return False

        index = self._index_dict[val] # 取出被删除元素索引
        self._index_dict.pop(val) # 索引字典中删除需要删除的元素

        if index==len(self._data_list)-1: # 删除最后一个元素
            self._data_list.pop()
            return True

        last = self._data_list[-1] # 取出最后一个元素
        self._data_list[index] = last # 使用最后一个元素替换被删除元素
        self._data_list.pop() #

        if not self._data_list: # 如果数组列表已空，说明现在删除的是最后一个元素，不能再用最后一个元素替换
            return False
        self._index_dict[last] = index # 字典中更新替换者的索引值
        return True

    def getRandom(self) -> int:
        return random.choice(self._data_list)


class RandomizedSet2:
    """
        hash表：O(1) 插入，O(1) 删除
        变长数组：O(1) 查找
        写法优化
    """
    def __init__(self):
        self._index_dict=dict()
        self._data_list = []

    def insert(self, val: int) -> bool:
        if val in self._index_dict: # 元素在集合中
            return False
        # 元素不在集合中，插入
        self._data_list.append(val)
        self._index_dict[val] = len(self._data_list) - 1
        return True


    def remove(self, val: int) -> bool:
        if val not in self._index_dict:
            return False

        index = self._index_dict.pop(val) # 取出被删除元素索引，索引字典中删除需要删除的元素

        if index==len(self._data_list)-1: # 删除最后一个元素
            self._data_list.pop()
            return True

        last = self._data_list.pop() # 取出最后一个元素，删除最后一个元素，因为上面已经判断处理过index==len(self._data_list)-1，所以这里一定有index!=len(self._data_list)-1
        self._data_list[index] = last # 使用最后一个元素替换被删除元素
        self._index_dict[last] = index # 字典中更新替换者的索引值
        return True

    def getRandom(self) -> int:
        return random.choice(self._data_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    r = RandomizedSet()
    # print(r.remove(0))
    # print(r._data_list)
    # print(r._index_dict)
    # print(r.remove(0))
    print(r.insert(0))
    print('-------------- insert 0 -------------')
    print(r._data_list)
    print(r._index_dict)
    # print(r.getRandom())
    print('-------------- remove 0 -------------')
    print(r.remove(0))
    print(r._data_list)
    print(r._index_dict)
    print('-------------- insert 0 -------------')
    print(r.insert(0))
    print(r._data_list)
    print(r._index_dict)
