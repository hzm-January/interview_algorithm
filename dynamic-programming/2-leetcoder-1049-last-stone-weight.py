def lastStoneWeightII(stones: list[int]) -> int:
    n = len(stones)
    s = sum(stones)
    target = s // 2
    dp = [0] * (target + 1)
    for i in range(0, n): # 这里物品从0开始，因为dp没有初始化
        for j in range(target, stones[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        print(i, dp)
    print(s, target, s-target, dp[-1])
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
    for i in range(stones[0], target + 1):  # 用无序数组的第一个元素是正确的
        dp[0][i] = stones[0]
    for i in range(1, n):
        for j in range(1, target + 1):  # 这里从0开始，从1开始都能正确，因为dp[0][0]初始为0，即使这里从0开始，下面的dp[i][0]也只会拷贝dp[0][0]，也会再重新赋值一遍0
            if j < stones[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i]] + stones[i])
        # print(i, dp)
    # print(s, target, s - target, dp[-1][-1])
    return abs((s - dp[-1][-1]) - dp[-1][-1])


def lastStoneWeightII3(stones: list[int]) -> int:
    """
        True False 官方写法，不推荐，没有自己写的求数字的方法好。
        官方Truefalse 物品必须从0开始遍历，lastStoneWeightII3中，dp更新公式dp[i+1][j]=...跟常规不一样，不优雅
        lastStoneWeightII4 是对这个写法的优化
        DP数组含义：DP[i][j] 物品0~i，放入容量为j的背包，是否存在物品组合刚好容量和=j。
    :param stones:
    :return:
    """
    n = len(stones)
    s = sum(stones)
    target = s // 2
    dp = [[False] * (target + 1) for _ in range(n+1)] # 注意这里是n+1，该题目与正常写法不一样，下面物品遍历要从0开始，不从0开始测试样例[1,2]会报错。
    for i in range(n):  # 用无序数组的第一个元素是正确的
        dp[i][0] = True # 容量为0，取0个物品可以使得容量和为0。

    for i in range(0, n):  # 这种写法，这里必须为0，不为0，测试样例[1,2]报错。该题目与正常写法不一样。
        for j in range(1, target + 1):  # 这里从0开始，从1开始都能正确，因为dp[0][0]初始为0，即使这里从0开始，下面的dp[i][0]也只会拷贝dp[0][0]，也会再重新赋值一遍0
            if j < stones[i]:
                dp[i+1][j] = dp[i][j]  # 注意这里是i+1，该题目与正常写法不一样，物品遍历要从0开始，不从0开始测试样例[1,2]会报错。
            else:
                dp[i+1][j] = dp[i][j] | dp[i][j - stones[i]] # 注意这里是i+1，该题目与正常写法不一样，物品遍历要从0开始，不从0开始测试样例[1,2]会报错。
        # print(i, dp)
    # print(s, target, s - target, dp[-1][-1])
    ans = 0
    for i in range(target, -1, -1):
        # 注意这里是n，不是n-1。
        if dp[n][i]:  # 找到dp最后一行中最后一个True，即最大的背包容量
            ans = (s - i) - i
            break
    return ans

def lastStoneWeightII4(stones: list[int]) -> int:
    """
        True False 官方写法，不推荐，没有自己写的求数字的方法好。
        这个写法。是对官方True false的优化，官方Truefalse 物品必须从0开始遍历，lastStoneWeightII3中，dp更新公式dp[i+1][j]=...跟常规不一样，不优雅
        DP数组含义：DP[i][j] 物品0~i，放入容量为j的背包，是否存在物品组合刚好容量和=j。
    :param stones:
    :return:
    """
    n = len(stones)
    s = sum(stones)
    target = s // 2
    dp = [[False] * (target + 1) for _ in range(n)]
    for i in range(n):  # 用无序数组的第一个元素是正确的
        dp[i][0] = True # 容量为0，取0个物品可以使得容量和为0。

    # 这一行是重点，可以避免dp更新物品从0开始遍历，避免dp[i+1][j]=....
    # 当 i==0 时，只有一个正整数 nums[0] 可以被选取，因此 dp[0][nums[0]]=true。
    # 只有物品0，则容量为物品0的重量时，可以使得容量和为背包容量。
    if stones[0]<=target: dp[0][stones[0]] = True # 这道题目的这个写法，这里必须设置

    for i in range(1, n): # 从1开始，因为dp矩阵第一行dp[0][j]已经初始化了
        for j in range(1, target + 1):  # 这里从0开始，从1开始都能正确，因为dp[0][0]初始为0，即使这里从0开始，下面的dp[i][0]也只会拷贝dp[0][0]，也会再重新赋值一遍0
            if j < stones[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j - stones[i]]
        # print(i, dp)
        # print(s, target, s - target, dp[-1][-1])
    ans = 0
    for i in range(target, -1, -1):
        if dp[n - 1][i]:  # 找到dp最后一行中最后一个True，即最大的背包容量
            ans = (s - i) - i
            break
    return ans
def lastStoneWeightII5(stones: list[int]) -> int:
    n = len(stones)
    s = sum(stones)
    target = s // 2
    dp = [True]+[False] * target
    for i in range(0, n): # 这里要从0开始遍历。
        for j in range(target, stones[i]-1, -1):  # 这里从0开始，从1开始都能正确，因为dp[0][0]初始为0，即使这里从0开始，下面的dp[i][0]也只会拷贝dp[0][0]，也会再重新赋值一遍0
            dp[j] = dp[j] | dp[j - stones[i]]

    ans = 0
    for i in range(target, -1, -1):
        if dp[i]:  # 找到dp最后一行中最后一个True，即最大的背包容量
            ans = (s - i) - i
            break
    return ans
def lastStoneWeightII6(stones: list[int]) -> int:
    n = len(stones)
    s = sum(stones)
    target = s // 2
    dp = [True]+[False] * target
    if stones[0]<=target: dp[stones[0]] = True
    for i in range(1, n):
        for j in range(target, stones[i]-1, -1):  # 这里从0开始，从1开始都能正确，因为dp[0][0]初始为0，即使这里从0开始，下面的dp[i][0]也只会拷贝dp[0][0]，也会再重新赋值一遍0
            dp[j] = dp[j] | dp[j - stones[i]]

    ans = 0
    for i in range(target, -1, -1):
        if dp[i]:  # 找到dp最后一行中最后一个True，即最大的背包容量
            ans = (s - i) - i
            break
    return ans

if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    # stones = [31, 26, 33, 21, 40]
    # stones = [1, 2]
    ans = lastStoneWeightII(stones)
    # ans = lastStoneWeightII2(stones)
    # ans = lastStoneWeightII3(stones)
    # ans = lastStoneWeightII4(stones)
    print(ans)
