def bubble_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    flag = False
    for i in range(0, n - 1):  # 比较轮次
        for j in range(1, n - i): # 剪枝，i个元素已经排好序
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                flag = True
        if not flag: break # 如果本轮比较没有元素交换位置，说明排序已完成
    return nums


if __name__ == '__main__':
    # nums = [5, 4, 3, 2, 1]
    # nums = [3, 2, 1, 5, 6]
    nums = [3, 6, 5, 2, 1]
    print(bubble_sort(nums))
