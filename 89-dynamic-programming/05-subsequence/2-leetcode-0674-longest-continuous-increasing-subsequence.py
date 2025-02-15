def findLengthOfLCIS(nums: list[int]) -> int:
    """
        动态规划
        1 dp数组定义：以nums[i]为结尾的最长连续子序列长度为dp[i]
        2 递推公式
        3 dp数组初始化：
        4 遍历顺序
        5 打印
    """
    n = len(nums)
    if n==1: return 1
    dp = [1] * n
    max_subs_len = 0
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
        max_subs_len = max(max_subs_len, dp[i])
        # print(dp)
    return max_subs_len


if __name__ == "__main__":
    nums = [1, 3, 5, 4, 7]
    ans = findLengthOfLCIS(nums)
    print(ans)
