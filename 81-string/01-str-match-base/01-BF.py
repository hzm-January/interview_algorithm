def bf(s1: str, s2: str) -> (int, str):
    n, m = len(s1), len(s2)
    for i in range(n - m + 1):
        sub1 = s1[i:i + m]
        flag = True
        for j in range(m):
            if sub1[j] != s2[j]:
                flag = False
                break
        if flag: return i, sub1
    return -1, ''


if __name__ == '__main__':
    # s1, s2 = 'afalskflsdfaasd', 'skfl'
    # s1, s2 = 'afalskflsdfaasd', 'aasd'
    # s1, s2 = 'afalskflsdfaasd', 'afal'
    s1, s2 = 'afalskflsdfaasd', 'flsd'
    print(bf(s1, s2))
