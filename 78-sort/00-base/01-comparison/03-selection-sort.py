def selectionSort(nums:list[int])->list[int]:
    n = len(nums)
    for i in range(n): # 已排序区间的最后一个元素的下一个位置，该位置从0开始（初始默认所有元素都未排序）
        min_idx = i
        for j in range(i+1, n): # 未排序区间寻找最小值
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[min_idx], nums[i] = nums[i], nums[min_idx] # 未排序区间的最小值放在已排序区间的最后一个元素的下一个位置
    return nums

if __name__ == "__main__":
    # nums = [5, 4, 3, 2, 1]
    # nums = [3, 2, 1, 5, 6]
    nums = [3, 6, 5, 2, 1]
    print(selectionSort(nums))