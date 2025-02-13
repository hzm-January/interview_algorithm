def wordBreak(s: str, wordDict: list[str]) -> bool:
    """
        回溯 - 全排列 - 分隔子串是否在wordDict中出现过
    """
    wordSet = set(wordDict)
    memory = [True] * len(s)
    def backtracking(cur,s, wordSet, memory):
        if cur>=len(s):
            return True
        if not memory[cur]:
            return memory[cur]
        for i in range(cur, len(s)):
            if (s[cur:i+1] in wordSet) and backtracking(cur+1, s, wordSet, memory):
                return True
        memory[cur]=False
        return False
    return backtracking(0, s, wordSet, memory)


def wordBreak2(s: str, wordDict: list[str]) -> bool:  # 错误代码

    """
        动态规划 完全背包 排列 先遍历背包后遍历物品
        题意：s 是背包，wordDict 是物品集合。求物品是否可以将背包装满。
        dp数组含义：背包容量i，dp[i]表示物品是否可以恰好装满背包。
    :param s:
    :param wordDict:
    :return:
    """
    n, m = len(wordDict), len(s)
    dp = [True] + [False] * m  # dp[i]是一个可以构成
    # 排列
    for j in range(m + 1):  # 先遍历背包
        for i in range(j):  # 后遍历物品
            print(s[i:j])
            if (s[i:j] in wordDict) and dp[i]:
                dp[j] = True
                break # leet 成功匹配后，eet,et和t 就不需要再继续处理了
        print(j, dp)
    return dp[-1]


if __name__ == '__main__':
    # s, wordDict = "leetcode", ["leet", "code"]
    # s, wordDict = "applepenapple", ["apple", "pen"]
    s, wordDict = "catsandog", ["cats", "dog", "sand", "and", "cat"]
    # s, wordDict = "ccbb", ["bc", "cb"]
    # s, wordDict = "ccaccc", ["cc","ac"]
    # s, wordDict = "catscatdog", ["cat", "cats", "dog"]
    ans = wordBreak(s, wordDict)
    print(ans)
