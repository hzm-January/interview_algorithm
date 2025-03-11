class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n, m = len(haystack), len(needle)

        # 1 生成next数组
        def getNext():
            nxt = [-1] * m
            nxt[0] = -1
            k = -1
            for i in range(1, m):
                while k !=-1 and needle[k + 1] != needle[i]:
                    k = nxt[k]
                if needle[k + 1] == needle[i]:
                    k += 1
                nxt[i] = k
            return nxt

        # 2 匹配
        nxt = getNext()
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = nxt[j - 1] + 1
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1


if __name__ == '__main__':
    haystack, needle = "sadbutsad", "sad"
    print(Solution().strStr(haystack, needle))
