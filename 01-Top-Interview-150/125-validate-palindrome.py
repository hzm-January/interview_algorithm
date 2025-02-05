def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    if len(s) < 2: return True
    p, q = 0, len(s) - 1
    while p < q:
        if s[p] != s[q]:
            break
        p += 1
        q -= 1
    return p >= q

def isPalindrome2(s: str) -> bool:
    s = ''.join(c for c in s.lower() if c.isalnum())
    return s == s[::-1]

def isPalindrome3(s: str) -> bool:
    if len(s) < 2: return True
    p, q = 0, len(s) - 1
    while p < q:
        while p < q and not s[p].isalnum():
            p+=1
        while p < q and not s[q].isalnum():
            q-=1
        if p < q:
            if s[p].lower() != s[q].lower():
                break
            else:
                p += 1
                q -= 1
    return p >= q

if __name__ == '__main__':
    s = 'A man, a plan, a canal: Panama'
    # s = 'race a car'
    # flag = isPalindrome(s)
    flag = isPalindrome3(s)
    print(flag)
