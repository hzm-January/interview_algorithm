def lengthOfLastWord(s: str) -> int:
    len_space = 0
    for i in range(len(s)-1,-1,-1):
        if s[i]!=' ':
            break
        len_space+=1
    index=0
    for i in range(len(s)-1-len_space, -1, -1):
        if s[i] == ' ':
            break
        index += 1
    return index


def lengthOfLastWord2(s: str) -> int:
    p = len(s) - 1
    while p >= 0 and s[p] == ' ':
        p -= 1
    n = p
    while p >= 0:
        if s[p] == ' ':
            break
        p -= 1
    return n - p


if __name__ == '__main__':
    s = "Hello World"
    # s = "   fly me   to   the moon  "
    print(lengthOfLastWord(s))
    print(lengthOfLastWord2(s))
