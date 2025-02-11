def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    dic_st, dic_ts = {}, {}
    p, q = 0, 0
    flag_st, flag_ts = True, True
    while p < len(t):
        if t[p] not in dic_st:
            dic_st[t[p]] = s[p]
        elif dic_st[t[p]] != s[p]:
            flag_st = False
        p += 1
    while q < len(t):
        if s[q] not in dic_ts:
            dic_ts[s[q]] = t[q]
        elif dic_ts[s[q]] != t[q]:
            flag_ts = False
        q += 1
    return flag_st and flag_ts

def isIsomorphic2(s: str, t: str) -> bool:
    """ 写法 优化 """
    if len(s) != len(t): return False
    dic_st, dic_ts = {}, {}
    p = 0
    while p < len(t):
        if (t[p] in dic_ts and dic_ts[t[p]] != s[p]) or (s[p] in dic_st and dic_st[s[p]] != t[p]):
            return False
        dic_ts[t[p]] = s[p]
        dic_st[s[p]] = t[p]
        p += 1
    return True

if __name__ == '__main__':
    # s, t = 'egg', 'add'
    # s, t = 'foo', 'bar'
    s, t = 'paper', 'title'
    # s, t = 'badc', 'baba'
    ans = isIsomorphic(s, t)
    print(ans)
