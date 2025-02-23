def subsets2(nums: list[int]) -> list[list[int]]:
    """
        回溯 - 已知长度为n的数组nums(有重复数字)，求组合元素个数k分别为[0,...,n]的组合
        树层去重 - used 数组
    :param nums:
    :return:
    """
    path, ans = [], []
    used = [0] * len(nums)

    def backtraking(cur, k):
        if len(path) == k:
            ans.append(path.copy())
            return
        for i in range(cur, len(nums) - (k - len(path)) + 1):
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            path.append(nums[i])
            used[i] = 1
            backtraking(i + 1, k)
            used[i] = 0
            path.pop()

    nums.sort()  # 排序，之后才能树层去重
    for i in range(0, len(nums) + 1):  # 依次求不同元素个数k的组合
        path = []  # 重置path数组
        used = [0] * len(nums)
        backtraking(0, i)
        print(ans)

    return ans


def subsets2_2(nums: list[int]) -> list[list[int]]:
    """
        回溯 - 已知长度为n的数组nums(有重复数字)，求组合元素个数k分别为[0,...,n]的组合
        树层去重 - startIndex
    :param nums:
    :return:
    """
    path, ans = [], []

    def backtraking(cur, k):
        if len(path) == k:
            ans.append(path.copy())
            return
        for i in range(cur, len(nums) - (k - len(path)) + 1):
            if i > cur and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtraking(i + 1, k)
            path.pop()

    nums.sort()  # 排序，之后才能树层去重
    for i in range(0, len(nums) + 1):  # 依次求不同元素个数k的组合
        path = []  # 重置path数组
        backtraking(0, i)
        print(ans)

    return ans


# def subsets2_3(nums: list[int]) -> list[list[int]]:
#     """
#         错误代码
#         测试样例：[4,4,4,1,4]
#         1）如果不进行非递减操作：
#         输出：[[],[4],[4,4],[4,4,4],[4,4,4,1],[4,4,4,1,4],[4,4,4,4],[4,4,1],[4,4,1,4],[4,1],[4,1,4],[1],[1,4]]
#         预期：[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
#         注意输出中：[4,4,4,1] 和 [4,4,1,4] 属于重复子集
#         2）如果进行非递减操作：
#         输出：[[],[4],[4,4],[4,4,4],[4,4,4,4],[1],[1,4]]
#         预期：[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
#         注意输出中：没有[1,4,4,4]，因为[4,4,4,1]被非递减操作过滤了
#
#         回溯 - 已知长度为n的数组nums(有重复数字)，求组合元素个数k分别为[0,...,n]的组合
#         树层去重 - used 数组
#     :param nums:
#     :return:
#     """
#     path, ans = [], []
#     n = len(nums)
#     def backtraking(cur):
#         ans.append(path.copy())
#         if cur>=n: return # 可以省略，因为单层逻辑最大为len(nums)
#         used = set()
#         for i in range(cur, n):
#             if nums[i] in used:
#                 continue
#             # if path and path[-1] > nums[i]: continue
#             used.add(nums[i])
#             path.append(nums[i])
#             backtraking(i + 1)
#             path.pop()
#
#     backtraking(0)
#     return ans


if __name__ == '__main__':
    # nums = [1, 2, 2]
    # nums = [0]
    nums = [4, 4, 4, 1, 4]
    # ans = subsets2(nums)
    # ans = subsets2_2(nums)
    ans = subsets2_3(nums)
    print(ans)
