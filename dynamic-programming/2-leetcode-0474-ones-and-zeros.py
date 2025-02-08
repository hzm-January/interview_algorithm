def findMaxForm(strs: list[str], m: int, n: int) -> int:
    """
        动态规划
        题目概述：背包容量固定，求装满背包最多能装多少个物品。
        易错点：该题用二维dp数组模拟传统01背包中的一维滚动数组，思路还是跟01背包中的一维滚动数组思路一样。
        dp数组含义：dp[i][j] i个0和j个1的容器，最多能装dp[i][j]个元素
        物品重量：x个0，y个1
        物品价值：1，放入该物品到背包，提供1个物品
    :param strs:
    :param m:
    :param n:
    :return:
    """
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # 该题目必须定义二维dp数组，因为背包容量是二维：0的个数和1的个数。
    # dp init
    for str in strs:  # 遍历物品
        x, y = str.count('0'), str.count('1')
        for i in range(m, x - 1, -1):  # 遍历背包，要逆序遍历，背包是二维的，所以是两层循环
            for j in range(n, y - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - x][j - y] + 1)
        # print(dp)
    return dp[-1][-1]


if __name__ == "__main__":
    # strs, m, n = ["10", "0001", "111001", "1", "0"], 5, 3
    strs, m, n = ["10", "0", "1"], 1, 1
    ans = findMaxForm(strs, m, n)
    print(ans)
