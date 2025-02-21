class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        h = {}
        ans = 0
        for i in range(n):
            h[s[i]] = h.get(s[i], 0) + 1
        for k, v in h.items():
            ans += v // 2 * 2
            if v % 2 == 1 and ans % 2 == 0: ans += 1
        return ans
    def longestPalindrome2(self, s: str) -> int:
        import collections
        ans = 0
        h = collections.Counter(s)
        for k, v in h.items():
            ans += v // 2 * 2
            if v % 2 == 1 and ans % 2 == 0: ans += 1
        return ans

if __name__ == '__main__':
    # s = "abccccdd"
    s = "a"
    print(Solution().longestPalindrome(s))
