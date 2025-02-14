def isAnagram(s: str, t: str) -> bool:
    """ hash """
    n, m = len(s), len(t)
    if n != m: return False
    hash = [0] * 30
    for i, j in zip(s, t):
        hash[ord(i) - ord('a')] += 1
        hash[ord(j) - ord('a')] -= 1
    print(hash)
    return not any(x!=0 for x in hash)
def isAnagram2(s: str, t: str) -> bool:
    from collections import Counter
    return Counter(s) == Counter(t)

if __name__ == '__main__':
    s, t = "anagram", "nagaram"
    # s, t = 'rat', 'car'
    ans = isAnagram(s, t)
    print(ans)
