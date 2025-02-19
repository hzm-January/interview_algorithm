from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p, q = 0, 0
        while p < len(g) and q < len(s):
            if s[q] >= g[p]:
                p += 1
            q += 1
        return p

    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        """ 官方代码 有点繁琐 """
        g.sort()
        s.sort()
        m, n = len(g), len(s)
        j, count = 0, 0
        for i in range(m):
            while j < n and g[i] > s[j]: # 一直循环找到最小的适合孩子胃口g[i]的饼干
                j += 1
            if j < n:
                count += 1
            j+=1
            i+=1
        return count



if __name__ == '__main__':
    # g, s = [1, 2, 3], [1, 1]
    g, s = [1, 2], [1, 2, 3]
    sol = Solution()
    print(sol.findContentChildren(g, s))
    print(sol.findContentChildren2(g, s))
