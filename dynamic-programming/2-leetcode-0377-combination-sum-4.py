def combinationSum4(nums: list[int], target: int) -> int:
    """
        完全背包 排列 先遍历背包后遍历物品
        dp数组含义：背包容量为j，装满背包有dp[j]种方法。
    """
    n = len(nums)
    dp = [0] * (target + 1)
    dp[0] = 1
    for j in range(target + 1):  # 先遍历背包
        for i in range(n):  # 后遍历物品
            if j >= nums[i]: dp[j] += dp[j - nums[i]]
        # print(j, dp)
    return dp[-1]


if __name__ == "__main__":
    nums, target = [1, 2, 3], 4
    ans = combinationSum4(nums, target)
    print(ans)
