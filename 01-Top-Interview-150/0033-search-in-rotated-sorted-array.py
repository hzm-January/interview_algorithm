import math


def search(nums: list[int], target: int) -> int: # 错误算法
    """

        错误算法
        错误原因：寻找峰值和寻找谷底都可能存在多个符合答案的值，并不一定能找到旋转数组旋转之前的起始元素的位置。
    :param nums:
    :param target:
    :return:
    """
    n = len(nums)

    # 寻找0
    def get(idx):
        if idx == -1:
            return -math.inf
        elif idx == n:
            return math.inf
        return nums[idx]

    left, right, ans = 0, len(nums) - 1, 0
    while left <= right:
        mid = left + (right - left) // 2
        if get(mid - 1) > get(mid) < get(mid + 1):
            # ans = mid
            # break
            return mid
        if get(mid) > get(mid + 1):
            left = mid + 1
        else:
            right = mid - 1
    print(ans)
    # 查找target
    # left, right = ans, ans + n
    # while left <= right:
    #     mid = (left + (right - left) // 2)
    #     if nums[mid % n] == target:
    #         return mid % n
    #     if nums[mid % n] < target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1

    return -1


if __name__ == "__main__":
    # target, nums = 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # target, nums = 7, [4, 5, 6, 7, 0, 1, 2]
    # target, nums = 0, [1]
    target, nums = 2, [3, 4, 5, 6, 1, 2]
    ans = search(nums, target)
    print(ans)
