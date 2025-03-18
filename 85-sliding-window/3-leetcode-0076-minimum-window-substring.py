class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        n, m = len(s), len(t)
        i = 0
        need = dict(Counter(t))
        needSum = m
        minLen = n + 1
        minSub = None
        for j in range(n):
            # 右进
            if s[j] not in need:  # 右进字符不在目标串中
                continue
            # 如果need[s[j]]<0，说明当前窗口中有多余的s[j]。如果need[s[j]]==0，说明窗口中s[j]的个数与目标串中s[j]的个数相同，暂时不需要s[j]
            if need[s[j]] > 0:
                needSum -= 1  # 右进
            need[s[j]] = need.get(s[j], 0) - 1  # 右进
            # 左出
            while needSum <= 0:
                if minLen > j - i + 1:
                    minLen = j - i + 1
                    minSub = s[i:j + 1]
                # 左出
                if s[i] not in need:
                    i += 1
                    continue
                # 如果need[s[i]]<0，表示当前窗口中有多余的s[i]，暂时不需要s[i]
                # 如果need[s[i]]==0，表示当前窗口中s[j]个数与目标串中s[j]的个数相同，但是现在左侧要弹出一个是s[j]，窗口中从刚好不需要就变成需要一个s[j]
                if need[s[i]] >= 0:
                    needSum += 1
                need[s[i]] = need.get(s[i], 0) + 1  # 左出
                i += 1   # 左侧出一个字符
        return minSub if minSub else ""


if __name__ == '__main__':
    # s, t = "ADOBECODEBANC", "ABC"
    # s, t = 'a', 'a'
    s,t = 'a','aa'
    print(Solution().minWindow(s, t))
