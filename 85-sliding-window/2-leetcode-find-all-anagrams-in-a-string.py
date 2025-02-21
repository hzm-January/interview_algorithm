from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """ 暴力 可AC """
        n, m = len(s), len(p)
        from collections import Counter
        d = Counter(p)
        ans = []
        for i in range(0, n - m + 1):
            h = Counter(s[i:m + i])
            if h == d:
                ans.append(i)
        return ans

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        """ 滑动窗口 """
        n, m = len(s), len(p)
        d, h = {}, {}
        ans = []
        if n < m: return ans
        for i in range(m):
            d[p[i]] = d.get(p[i], 0) + 1
            h[s[i]] = h.get(s[i], 0) + 1

        if h == d: ans.append(0)
        for i in range(0, n - m):
            h[s[i]] = h.get(s[i], 0) - 1
            if h[s[i]] <= 0:
                h.pop(s[i])
            h[s[i + m]] = h.get(s[i + m], 0) + 1
            if h == d:
                ans.append(i + 1)
        return ans

    def findAnagrams3(self, s: str, p: str) -> List[int]:
        """ 滑动窗口 """
        n, m = len(s), len(p)
        d, c = [0] * 26, [0] * 26
        differ = 0
        ans = []
        if n < m: return ans
        for i in range(m):
            d[ord(p[i]) - 97] += 1
            d[ord(s[i]) - 97] -= 1

        differ = [t != 0 for t in d].count(True)

        if differ == 0: ans.append(0)

        for i in range(n - m):
            if d[ord(s[i]) - 97] == 1:  # 不同变相同
                differ -= 1
            if d[ord(s[i]) - 97] == 0:  # 相同变不同
                differ += 1

            d[ord(s[i]) - 97] -= 1

            if d[ord(s[i + m]) - 97] == -1:  # 不同变相同
                differ -= 1
            if d[ord(s[i + m]) - 97] == 0:  # 相同变不同
                differ += 1

            d[ord(s[i+m]) - 97] += 1

            if differ == 0:
                ans.append(i + 1)
        return ans


if __name__ == '__main__':
    s, p = "cbaebabacd", "abc"
    # s, p = "abab", "ab"
    # s, p = "aaaaaaaaaa", "aaaaaaaaaaaaa"  # 测试样例 len(s)<len(p)
    # print(Solution().findAnagrams(s, p))
    # print(Solution().findAnagrams2(s, p))
    print(Solution().findAnagrams3(s, p))
