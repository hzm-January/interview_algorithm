def canConstruct(ransomNote: str, magazine: str) -> bool:
    dic = {}
    for m in magazine:
        if m not in dic:
            dic[m] = 1
        else:
            dic[m] += 1
    for r in ransomNote:
        if r in dic and dic[r] != 0:
            dic[r] -= 1
        else:
            return False
    return True
def canConstruct2(ransomNote: str, magazine: str) -> bool:
    import collections
    """ 优化写法 """
    if len(magazine) < len(ransomNote):
        return False
    return not collections.Counter(ransomNote) - collections.Counter(magazine)

if __name__ == "__main__":
    # ransomNote, magazine = "a", "b"
    # ransomNote, magazine = "aa", "ab"
    ransomNote, magazine = "aa", "aab"
    # ans = canConstruct(ransomNote, magazine)
    ans = canConstruct2(ransomNote, magazine)
    print(ans)
