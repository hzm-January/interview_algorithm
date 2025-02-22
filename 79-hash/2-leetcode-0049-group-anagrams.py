import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))  # 字母排序后作为哈希表的key
            mp[key].append(s)
        # print(mp.values())
        return list(mp.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 26  # 题目已知元素都是小写字母
            for c in s:
                counts[ord(c) - ord('a')] += 1
            mp[tuple(counts)].append(s)
        return list(mp.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # print(Solution().groupAnagrams(strs))
    print(Solution().groupAnagrams2(strs))
