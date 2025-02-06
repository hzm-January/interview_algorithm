def isSubsequence(s: str, t: str) -> bool:
    p,q=0,0
    while p<len(s) and q<len(t):
        if s[p] == t[q]:
            p+=1
        q+=1
    return p==len(s)


if __name__ == '__main__':
    s, t = "abc", "ahbgdc"
    flag = isSubsequence(s, t)
    print(flag)
