def wordPattern(pattern: str, s: str) -> bool:
    dic = {}
    dic_2 = {}
    p, q = 0, 0
    s_ = s.split(' ')
    n, m = len(pattern), len(s_)
    if n != m: return False
    while p < n and q < m:
        if pattern[p] not in dic:
            if s_[q] not in dic_2:
                dic[pattern[p]] = s_[q]
                dic_2[s_[q]] = pattern[p]
            else:
                if dic_2[s_[q]] != pattern[p]:
                    return False
        else:
            if dic[pattern[p]] != s_[q]:
                return False
        p += 1
        q += 1
    return True


def wordPattern2(pattern: str, s: str) -> bool:
    """ 优化写法 """
    word2ch = dict()
    ch2word = dict()
    words = s.split(' ')
    if len(words) != len(pattern): return False
    for ch,word in zip(pattern, words):
        if (word in word2ch and word2ch[word]!=ch) or (ch in ch2word and ch2word[ch]!=word):
            return False
        word2ch[word] = ch
        ch2word[ch] = word
    return True


if __name__ == '__main__':
    pattern, s = "abba", "dog cat cat dog"
    ans = wordPattern(pattern, s)
    print(ans)
