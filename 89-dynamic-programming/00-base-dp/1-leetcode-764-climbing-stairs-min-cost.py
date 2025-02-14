# def minCostClimbingStairs(cost) -> int:
#     dp = [0 for _ in range(len(cost) + 1)]
#     for i in range(2, len(cost) + 1):
#         dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
#     return dp[len(cost)]

def minCostClimbingStairs(cost) -> int:
    p, q, r = 0, 0, 0
    for i in range(2, len(cost) + 1):
        r = min(q + cost[i - 1], p + cost[i - 2])
        p = q
        q = r
    return r


if __name__ == '__main__':
    print(minCostClimbingStairs([10, 15, 20]))
    print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
