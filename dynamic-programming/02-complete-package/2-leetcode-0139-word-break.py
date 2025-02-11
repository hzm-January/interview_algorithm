# def wordBreak(s: str, wordDict: list[str]) -> bool:
#     """
#         动态规划 完全背包
#         题意：s 是背包，wordDict 是物品集合。求物品是否可以将背包装满。
#         dp数组含义：背包容量i，最多能装物品的价值为dp[i]。
#         dp数组含义：背包容量i，dp[i]表示物品是否可以恰好装满背包。
#     :param s:
#     :param wordDict:
#     :return:
#     """
#     n, m = len(wordDict), len(s)
#     dp = [0] * (m + 1)
#     for i in range(n):  # 先遍历物品
#         for j in range(len(wordDict[i]), m + 1):  # 后遍历背包
#             dp[j] = max(dp[j], dp[j - len(wordDict[i])] + len(wordDict[i]))
#             print(' ', dp)
#         print(i, dp)
#     return dp[-1] == len(s)


def wordBreak(s: str, wordDict: list[str]) -> bool: # 错误代码

    """
        错误代码，valid函数中len(s_j)==len(s)判断逻辑中，不能使用replace，因为有很多错误。

        动态规划 完全背包
        题意：s 是背包，wordDict 是物品集合。求物品是否可以将背包装满。
        dp数组含义：背包容量i，最多能装物品的价值为dp[i]。
        dp数组含义：背包容量i，dp[i]表示物品是否可以恰好装满背包。
    :param s:
    :param wordDict:
    :return:
    """
    def valid(tmp:list[str])->bool:
        s_j = ''.join(tmp)
        if len(s_j)>len(s) :return False # 当前子串长度大于目标字符串
        for subs in tmp:
            if subs not in s:
                return False # subs不是s的子串
        if len(s_j)<len(s):
            tmp_s = s
            for subs in tmp:
                if subs not in tmp_s:
                    return False
                tmp_s = tmp_s.replace(subs, "_"*len(subs), 1)

        if len(s_j)==len(s):
            tmp_s = s
            # 验证是否可以组成目标字符串
            for subs in tmp:
                # tmp_s = tmp_s.replace(subs,"",1) # 不能用""，否则测试样例 s='ccbb' ['cb','bc']不能通过，因为['cb','cb']这种情况是不满足条件的，但是replace两次后为空字符串，返回True（错误）
                tmp_s = tmp_s.replace(subs,"_"*len(subs),1)
            # if tmp_s!='':
            if tmp_s!='_'*len(s):
                return False
        return True
    n, m = len(wordDict), len(s)
    dp = [[] for _ in range(m+1)] # dp[i]是一个可以构成
    for i in range(n):  # 先遍历物品
        for j in range(len(wordDict[i]), m + 1):  # 后遍历背包
            tmp = dp[j - len(wordDict[i])].copy()
            # tmp = dp[j].copy()
            tmp.append(wordDict[i])
            if valid(tmp) and len(tmp)>len(dp[j]):
                dp[j] = tmp
            # print(' ', dp)
        # print(i, dp)
    return len(''.join(dp[-1])) == len(s)

if __name__ == '__main__':
    # s, wordDict = "leetcode", ["leet", "code"]
    # s, wordDict = "applepenapple", ["apple", "pen"]
    # s, wordDict = "catsandog", ["cats", "dog", "sand", "and", "cat"]
    s, wordDict = "ccbb", ["bc", "cb"]
    ans = wordBreak(s, wordDict)
    print(ans)
