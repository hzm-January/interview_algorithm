def lastStoneWeightII(stones: list[int]) -> int:
    n = len(stones)
    s = sum(stones)
    target = s // 2
    dp = [0] * (target + 1)
    for i in range(0, n):
        for j in range(target, stones[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        # print(i, dp)
    # print(s, target, s-target, dp[-1])
    return abs((s - dp[-1]) - dp[-1])


def lastStoneWeightII2(stones: list[int]) -> int:
    n = len(stones)
    s = sum(stones)
    target = s // 2
    # min_v = min(stones)
    dp = [[0] * (target + 1) for _ in range(n)]
    # dp init
    # for i in range(min_v, target + 1): # 不能用最小值，错误，可能是因为遍历是按照无序数组遍历，这个最小值后面还要遍历到，还要放入背包一次。
    #     dp[0][i] = min_v
    for i in range(stones[0], target + 1): # 用无序数组的第一个元素是正确的
        dp[0][i] = stones[0]
    for i in range(1, n):
        for j in range(1, target + 1): # 这里从0开始，从1开始都能正确，因为dp[0][0]初始为0，即使这里从0开始，下面的dp[i][0]也只会拷贝dp[0][0]，也会再重新赋值一遍0
            if j < stones[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i]] + stones[i])
        # print(i, dp)
    # print(s, target, s - target, dp[-1][-1])
    return abs((s - dp[-1][-1]) - dp[-1][-1])


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    # stones = [31, 26, 33, 21, 40]
    # ans = lastStoneWeightII(stones)
    ans = lastStoneWeightII2(stones)
    print(ans)
