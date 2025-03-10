from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            超时代码
            该代码思路与最小基因变化相同，最小基因变化可以AC，但是单词接龙超时
        """
        if beginWord == endWord: return 0
        if endWord not in wordList: return 0

        def diffOne(s1, s2):
            return sum([c1 != c2 for c1, c2 in zip(s1, s2)]) == 1

        # 1 建图 - 无向图
        n = len(wordList)
        adj = [[] for _ in range(n)]
        endIndex = -1
        for i in range(n):
            if wordList[i] == endWord:
                endIndex = i
            for j in range(i + 1, n):
                if not diffOne(wordList[i], wordList[j]): continue
                adj[i].append(j)
                adj[j].append(i)

        # wordList中没有找到endWord，即endWord不合法
        if endIndex == -1:
            return 0

        # 2 BFS搜索
        import collections
        queue = collections.deque([(i, 2) for i, s in enumerate(wordList) if diffOne(s, beginWord)])
        visited = set([i for i, s in enumerate(wordList) if diffOne(s, beginWord)])
        while queue:
            cur, step = queue.popleft()
            if cur == endIndex:
                return step
            for nxt in adj[cur]:
                if nxt in visited: continue  # 已处理过
                if nxt == endIndex:
                    return step + 1
                visited.add(nxt)
                queue.append((nxt, step + 1))  # 待处理顶点入队列

        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            双向BFS
        """
        if beginWord == endWord: return 0
        if endWord not in wordList: return 0

        def diffOne(s1, s2):
            return sum([c1 != c2 for c1, c2 in zip(s1, s2)]) == 1

        # 1 建图 - 无向图
        n = len(wordList)
        adj = [[] for _ in range(n)]
        endIndex = -1
        for i in range(n):
            if wordList[i] == endWord:
                endIndex = i
            for j in range(i + 1, n):
                if not diffOne(wordList[i], wordList[j]): continue
                adj[i].append(j)
                adj[j].append(i)

        # wordList中没有找到endWord，即endWord不合法
        if endIndex == -1:
            return 0

        # 2 BFS搜索
        import collections
        queue = collections.deque([(i, 2) for i, s in enumerate(wordList) if diffOne(s, beginWord)])
        visited = set([i for i, s in enumerate(wordList) if diffOne(s, beginWord)])
        while queue:
            cur, step = queue.popleft()
            if cur == endIndex:
                return step
            for nxt in adj[cur]:
                if nxt in visited: continue  # 已处理过
                if nxt == endIndex:
                    return step + 1
                visited.add(nxt)
                queue.append((nxt, step + 1))  # 待处理顶点入队列

        return 0


if __name__ == '__main__':
    # wordList, beginWord, endWord = ["hot", "dot", "dog", "lot", "log", "cog"], "hit", "cog"
    wordList, beginWord, endWord = ['a', 'b', 'c'], 'a', 'c'
    print(Solution().ladderLength(beginWord, endWord, wordList))
