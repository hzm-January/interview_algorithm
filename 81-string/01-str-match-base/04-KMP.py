def kmp(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)

    def getNext(s2: str) -> list[int]:
        nxt = [-1] * m
        # 初始化next[0]=-1
        nxt[0] = -1
        k = -1  # k指向公共最长前缀的末尾
        for i in range(1, m):  # 计算模式串子串[0,i]的公共最长前缀
            # [0,i-1]的公共最长前缀已找到并记录在nxt[i-1]中
            # 现在判断下一个字符是否相等
            while k !=-1 and s2[k + 1] != s2[i]: # k!=-1保证nxt正常访问
                k = nxt[k]  # 下一个字符不相等，回退到上一个最长公共前缀末尾
            if s2[k + 1] == s2[i]:
                k += 1  # 下一个字符相等，则递推k = k+1
            nxt[i] = k
        return nxt

    # next数组
    nxt = getNext(s2)
    j = 0  # j指向模式串中当前正在匹配的字符
    for i in range(n):  # i指向主串中当前正在匹配的字符
        while j > 0 and s1[i] != s2[j]:  # 当前字符不匹配
            j = nxt[j - 1] + 1  # 跳转到最长公共后缀的最长公共前缀的下一个索引
        if s1[i] == s2[j]:  # 当前字符匹配
            j += 1  # 继续匹配之后的字符
        if j == m:  # 模式串已匹配成功
            return i - m + 1
    return -1


if __name__ == '__main__':
    # s1, s2 = 'afalskflsdfaasd', 'skfl'  # 4
    # s1, s2 = 'afalskflsdfaasd', 'aasd' # 11
    # s1, s2 = 'afalskflsdfaasd', 'afal' # 0
    # s1, s2 = 'afalskflsdfaasd', 'flsd' # 6
    # s1,s2 = "mississippi", "issip"
    s1,s2="bbababaaaababbaabbbabbbaaabbbaaababbabaabbaaaaabbaaabbbbaaabaabbaababbbaabaaababbaaabbbbbbaabbbbbaaabbababaaaaabaabbbababbaababaabbaa","bbabba"
    print(kmp(s1, s2))
