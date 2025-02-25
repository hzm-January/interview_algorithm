"""
    基数排序
"""
import random


def radixSort(nums: list[int]) -> list[int]:
    def countingSort(nums: list[int], exp: int):
        # 1 确定数值范围
        valRange = 10  # 0~9
        # 2 统计数值出现个数，并累加计数数组
        counter = [0] * valRange
        for num in nums:
            index = (num // exp) % 10  # 取出独立位
            counter[index] += 1
        for i in range(1, valRange):
            counter[i] += counter[i - 1]
        # 3 倒序生成排序结果
        sorted = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            index = (nums[i] // exp) % 10  # 取出独立位
            sorted[counter[index] - 1] = nums[i]
            counter[index] -= 1
        nums[:] = sorted  # 必须使用[:]

    maxVal = max(nums)
    exp = 1 # 取独立位的除数
    while maxVal // exp > 0:
        countingSort(nums, exp)
        exp *= 10
    return nums


if __name__ == '__main__':
    nums = [random.randint(0, 100) for _ in range(100)]
    print('original nums: ', nums)
    print(radixSort(nums))
