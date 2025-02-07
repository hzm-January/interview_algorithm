def canPartition(nums: list[int]) -> bool:
    if sum(nums) % 2 != 0: return False
    target = sum(nums) // 2
    dp = [0] * (target + 1)
    for i in range(len(nums)):
        for j in range(target, nums[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
    return dp[target] == target


def canPartition_2(nums: list[int]) -> bool:
    if sum(nums) % 2 != 0: return False
    # min_value = min(nums)
    target = sum(nums) // 2
    dp = [[0] * (target + 1) for _ in range(len(nums))]
    # init
    # for i in range(min_value, target + 1): # 这道题目，赋值为Min_value能全部通过，但是这是不对的，用1049最后石头的重量题目里的测试样例能测试出来。
    #     dp[0][i] = min_value
    for i in range(nums[0], target + 1):  # 这里用数组的第一个值进行初始化是最正确的，因为之后的遍历就是从nums[0]开始的。
        dp[0][i] = nums[0]

    for i in range(1, len(nums)):
        for j in range(0, target + 1):  # 这里从0开始，从1开始都可以，从0开始需要再赋值一次dp[i][0]，数值都是拷贝dp[0][0]，这在初始化时都已经赋值过了。直接从1开始就可以。
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
            if j == target and dp[i][j] == target: # 可以优化一点时间，只要找到答案，立即返回
                return True
    # print(dp)
    return False


def canPartition_3(nums: list[int]) -> bool: # 这种直接求和的 不用判断元素<2，也不用判断最大值>target
    if sum(nums) % 2 != 0: return False
    # min_value = min(nums)
    target = sum(nums) // 2
    dp = [[0] * (target + 1) for _ in range(len(nums))]
    # init
    # for i in range(min_value, target + 1): # 这道题目，赋值为Min_value能全部通过，但是这是不对的，用1049最后石头的重量题目里的测试样例能测试出来。
    #     dp[0][i] = min_value
    for i in range(nums[0], target + 1): # 这里用数组的第一个值进行初始化是最正确的，因为之后的遍历就是从nums[0]开始的。
        dp[0][i] = nums[0]
    for i in range(1, len(nums)):
        for j in range(0, target + 1): # 这里从0开始，从1开始都可以，从0开始需要再赋值一次dp[i][0]，数值都是拷贝dp[0][0]，这在初始化时都已经赋值过了。直接从1开始就可以。
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
            # print(i,j,dp)
            # if j == target and dp[i][j] == target:
            #     return True
    # print(dp)
    return dp[-1][-1] == target


def canPartition_4(nums: list[int]) -> bool:
    if sum(nums) % 2 != 0: return False # 如果所有元素之和为奇数，一定不满足条件
    if len(nums) < 2: return False # 如果元素个数为1或者0，一定不满足条件。
    target = sum(nums) // 2
    if max(nums)>target: return False # 如果最大值大于target，则其余元素之和一定小于target。其余元素的和一定不等于target
    dp = [[False] * (target + 1) for _ in range(len(nums))]
    # init
    for i in range(len(nums)):
        dp[i][0] = True
    dp[0][nums[0]] = True # 没有这一行也可以AC

    for i in range(1, len(nums)):
        for j in range(1, target + 1):
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]
            print(i, j, dp)
    return dp[-1][-1]


def canPartition_5(nums: list[int]) -> bool:
    if sum(nums) % 2 != 0: return False # 如果所有元素之和为奇数，一定不满足条件
    if len(nums) < 2: return False # 如果元素个数为1或者0，一定不满足条件。
    target = sum(nums) // 2
    if max(nums)>target: return False # 如果最大值大于target，则其余元素之和一定小于target。其余元素的和一定不等于target
    dp = [True] + [False] * target
    # init
    for i in range(1, len(nums)):
        for j in range(target, nums[i]-1, -1):
            dp[j] = dp[j] | dp[j - nums[i]]

    return dp[-1]

if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    # nums = [1, 2, 3, 5]
    # nums = [2, 2, 1, 1]
    # ans = canPartition(nums)
    # ans = canPartition_2(nums)
    ans = canPartition_4(nums)
    print(ans)
