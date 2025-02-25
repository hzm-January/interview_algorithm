def countingSort(nums: list[int]) -> list[int]:
    # 1 确定计数数组长度
    max_val = max(nums)
    min_val = min(nums)

    # 2 对元素个数计数，并累加计数
    counter = [0] * (max_val - min_val + 1)
    for num in nums:
        counter[num - min_val] += 1
    print('counter before accumulate', counter)
    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]
    print('counter after accumulate', counter)

    # 3 生成排序结果
    sorted = [0] * len(nums)
    # 反向填充数组，确保排序稳定
    for i in range(len(nums) - 1, -1, -1):
        sorted[counter[nums[i]-min_val] - 1] = nums[i]
        counter[nums[i]-min_val] -= 1
    return sorted


if __name__ == '__main__':
    import random

    nums = [random.randint(0, 100) for _ in range(100)]
    print(nums)
    print(countingSort(nums))
