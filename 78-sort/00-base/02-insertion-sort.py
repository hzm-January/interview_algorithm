def insertionSort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)): # 选择一个未排序区间的元素
        j = i - 1
        tmp = nums[i]
        while j >= 0 and nums[j] > tmp: # 搜索合适的插入位置
            nums[j+1]=nums[j]
            j-=1
        nums[j + 1] = tmp
    return nums

if __name__ == "__main__":
    # nums = [5, 4, 3, 2, 1]
    # nums = [3, 2, 1, 5, 6]
    nums = [3, 6, 5, 2, 1]
    print(insertionSort(nums))
