def subsets(nums: list[int]) -> list[list[int]]:
    """
        回溯 - 已知长度为n的数组nums(无重复数字)，求组合元素个数k分别为[0,...,n]的组合
    :param nums:
    :return:
    """
    path, ans = [], []

    def backtraking(cur, k):
        if len(path) == k:
            ans.append(path.copy())
            return
        for i in range(cur, len(nums) - (k - len(path)) + 1):
            path.append(nums[i])
            backtraking(i + 1, k)
            path.pop()

    for i in range(0, len(nums) + 1): # 依次求不同元素个数k的组合
        path = [] # 重置path数组
        backtraking(0, i)
    return ans


if __name__ == '__main__':
    # nums = [1, 2, 3]
    nums = [0]
    ans = subsets(nums)
    print(ans)
