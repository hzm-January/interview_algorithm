import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            滑动窗口
            这份代码可以AC，但是不是滑动窗口的标准写法，是自己第一次写的答案
        """
        n, m = len(s1), len(s2)
        l, r = 0, 0
        needSum = n
        need = collections.Counter(s1)
        print(need)
        while r < m:
            while r < m and r - l + 1 <= n:
                if s2[r] in need:
                    if need[s2[r]] > 0:
                        needSum -= 1
                    need[s2[r]] -= 1 # need[s2[r]]有可能是负数
                r += 1
            if needSum <= 0: return True
            # print('after while: ', l,r,needSum, need)
            if s2[l] in need:
                if need[s2[l]] >= 0: # need[s2[l]]<0时说明，窗口中有多余的s2[l]，现在不需要
                    needSum += 1
                need[s2[l]] += 1
            l += 1

            # print('after l+=1: ', l,r,needSum, need)
        return False

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        """

        """
        n, m = len(s1), len(s2)
        need = collections.Counter(s1)
        needSum = n
        for r in range(m):
            # 右边界滑动一个单元
            if s2[r] in need: # 新增加的元素对需求有影响
                if need[s2[r]] > 0:
                    needSum -= 1
                need[s2[r]] -= 1

            l = r - n  # 滑动窗口现在多一个元素，从左边缩小窗口
            # 左边界滑动一个单元
            if l >= 0 and s2[l] in need:
                if need[s2[l]] >= 0:
                    needSum += 1
                need[s2[l]] += 1
            if needSum <= 0: return True
        return False


if __name__ == '__main__':
    # s1, s2 = "ab", "eidboaoo"
    # s1, s2 = "hello", "ooolleoooleh"
    s1, s2 = "adc", "dcda"
    print(Solution().checkInclusion(s1, s2))
    print(Solution().checkInclusion2(s1, s2))
