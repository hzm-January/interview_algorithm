def numTrees(n: int) -> int:
    """
        1 dp数组含义：由i个节点组成的1~n互不相同的二叉搜索树有dp[i]种
        2 递推公式：dp[i]+=dp[i-1]*dp[j-i]
        3 dp数组初始化：dp[0]=1 dp[i]=0
        4 遍历顺序：从前到后
        5 打印：
    """
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):  # 有i个节点
        for j in range(1, i + 1):  # 分别以j作为根节点
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[-1]


def numTrees_2(n: int) -> int:
    """
        卡特兰数
    """
    C = 1
    for i in range(0, n):  # 根据i=n-1计算的Cn
        C = C * 2 * (2 * i + 1) / (i + 2)
    return int(C)


if __name__ == '__main__':
    # nt = numTrees(10)
    # nt = numTrees(3)
    # nt = numTrees(1)
    nt = numTrees_2(3)
    # nt = numTrees_2(1)
    print(nt)
