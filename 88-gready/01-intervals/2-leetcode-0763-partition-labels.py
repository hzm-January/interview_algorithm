from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 1 统计同一字符出现的最后索引
        hash = dict()
        for i in range(len(s)):
            hash[s[i]] = i
        # 2 划分区间
        left, right = 0, 0
        ans = []
        for i, c in enumerate(s):
            right = max(right, hash[c])
            if i == right:
                ans.append(right - left + 1)
                left = right + 1
        return ans


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels(s))
