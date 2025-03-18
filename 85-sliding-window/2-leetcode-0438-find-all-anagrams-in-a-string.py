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
            if h == d:  # 缺点：要比较两个字典
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
            if h == d:  # 缺点；要比较两个字典
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

            d[ord(s[i + m]) - 97] += 1

            if differ == 0:
                ans.append(i + 1)
        return ans

    def findAnagrams4(self, s: str, p: str) -> List[int]:
        """
            滑动窗口  窗口长度固定  正规写法 (推荐)
            needSum 记录需要元素总数
            need 记录需要每个元素的个数
            1 右进左出，保证窗口长度不变
                右进：右进字符为目标串中字符，需求-1，总需求-1
                左出：左出字符为目标串中字符，需求+1，总需求+1
            2 needSum==0，表示窗口中的子串匹配上了目标串
        """
        from collections import Counter
        s_len, p_len = len(s), len(p)
        need = dict(Counter(p))
        needSum = p_len
        ans=[]
        for j in range(s_len):
            if s[j] in need:  # 右侧进一个字符
                if need[s[j]] > 0: # 如果need[s[j]]<0，说明当前窗口中有多余的s[j]。如果need[s[j]]==0，说明窗口中s[j]的个数与目标串中s[j]的个数相同，暂时不需要s[j]
                    needSum -= 1
                need[s[j]] -= 1
            i = j - p_len
            if i >= 0 and s[i] in need:  # 左侧出一个字符
                if need[s[i]] >= 0:  # 如果need[s[i]]<0，表示当前窗口中有多余的s[i]，暂时不需要s[i]
                    needSum += 1 # 如果need[s[i]]==0，表示当前窗口中s[j]个数与目标串中s[j]的个数相同，但是现在左侧要弹出一个是s[j]，窗口中从刚好不需要就变成需要一个s[j]
                need[s[i]] += 1
            if needSum==0:
                ans.append(i+1)
        return ans


if __name__ == '__main__':
    # s, p = "cbaebabacd", "abc"
    # s, p = "abab", "ab"
    s, p = "baa", "aa"
    # s, p = "aaaaaaaaaa", "aaaaaaaaaaaaa"  # 测试样例 len(s)<len(p)
    # print(Solution().findAnagrams(s, p))
    # print(Solution().findAnagrams2(s, p))
    print(Solution().findAnagrams3(s, p))
    print(Solution().findAnagrams4(s, p))
