import collections


def rk_unique_hash(s1: str, s2: str):
    """ 哈希唯一  无哈希冲突 """
    n, m = len(s1), len(s2)
    hash = dict()  # hash表

    pre_hash = 0  # 主串第一个长度为m子串的hash
    pattern_hash = 0  # 模式串hash
    for i in range(m):
        pre_hash += (ord(s1[i]) - ord('a')) * pow(26, m - i - 1)
        pattern_hash += (ord(s2[i]) - ord('a')) * pow(26, m - i - 1)
    hash[pre_hash] = s1[0:m]

    # 计算主串中所有长度为m的子串hash和模式串的hash
    # 同时匹配查找模式串在主串中的起始位置
    index = -1
    for i in range(1, n - m + 1):
        sub1 = s1[i:i + m]
        hash1 = (pre_hash - (ord(s1[i - 1]) - ord('a')) * pow(26, m - 1)) * 26 + (ord(s1[i + m - 1]) - ord('a'))
        hash[hash1] = sub1
        pre_hash = hash1
        if hash1 == pattern_hash:
            index = i
            break
    return index, s1[index:index + m]


def rk_hash(s1: str, s2: str):
    """ 哈希不唯一  有哈希冲突 """
    n, m = len(s1), len(s2)
    hash = collections.defaultdict(list)  # hash表

    pre_hash = 0  # 主串第一个长度为m子串的hash
    pattern_hash = 0  # 模式串hash
    for i in range(m):
        pre_hash += (ord(s1[i]) - ord('a'))
        pattern_hash += (ord(s2[i]) - ord('a'))
    hash[pre_hash].append((0, s1[0:m]))

    # 计算主串中所有长度为m的子串hash和模式串的hash
    # 同时匹配查找模式串在主串中的起始位置
    index = -1
    for i in range(1, n - m + 1):
        sub1 = s1[i:i + m]
        hash1 = (pre_hash - (ord(s1[i - 1]) - ord('a'))) + (ord(s1[i + m - 1]) - ord('a'))
        hash[hash1].append((i, sub1))
        pre_hash = hash1
        if hash1 == pattern_hash and sub1 == s2:
            index = i
            break
    return index, s1[index:index + m]


if __name__ == '__main__':
    # s1, s2 = 'afalskflsdfaasd', 'skfl'
    # s1, s2 = 'afalskflsdfaasd', 'aasd'
    # s1, s2 = 'afalskflsdfaasd', 'afal'
    s1, s2 = 'afalskflsdfaasd', 'flsd'
    index, s = rk_unique_hash(s1, s2)
    print(index, s)
    index, s = rk_hash(s1, s2)
    print('------------------------')
    print(index, s)
