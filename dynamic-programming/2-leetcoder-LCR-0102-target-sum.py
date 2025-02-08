def findTargetSumWays(nums: list[int], target: int) -> int:
    """
     凑正数
    """
    s, n = sum(nums), len(nums)
    """
        left+right=sum left-right=target -> left=(sum+target)//2 right=(sum-target)//2
    """
    if (s + target) % 2 != 0: return 0  # 奇数 一定凑不出答案（上面公式没有解）测试样例[1] 2
    nt = (s + target) // 2  # new target 凑正数
    dp = [0] * (nt + 1)
    dp[0] = 1 # 注意这里必须初始化，跟传统的滚动数组初始化全0不一样。
    for i in range(n):
        for j in range(nt, nums[i] - 1, -1):
            dp[j] = dp[j] + dp[j - nums[i]]
        # print(i, dp)
    return dp[-1]


def findTargetSumWays2(nums: list[int], target: int) -> int:
    """
        凑负数
    :param nums:
    :param target:
    :return:
    """
    s, n = sum(nums), len(nums)
    """
        left+right=sum left-right=target -> left=(sum+target)//2 right=(sum-target)//2
    """
    if s - target < 0 or (s - target) % 2 != 0: return 0  # sum<target一定凑不出答案，奇数 一定凑不出答案（上面公式没有解）
    nt = (s - target) // 2  # new target
    dp = [0] * (nt + 1)
    dp[0] = 1 # 注意这里必须初始化，跟传统的滚动数组初始化全0不一样。
    for i in range(n):
        for j in range(nt, nums[i] - 1, -1):
            dp[j] = dp[j] + dp[j - nums[i]]
        # print(i, dp)
    return dp[-1]


if __name__ == '__main__':
    target, nums = 3, [1, 1, 1, 1, 1]
    # print(findTargetSumWays(nums, target))
    print(findTargetSumWays2(nums, target))
