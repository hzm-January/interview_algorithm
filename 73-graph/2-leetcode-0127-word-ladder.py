from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            超时代码
            该代码思路与最小基因变化相同，最小基因变化可以AC，但是单词接龙超时
            排查问题
            超时原因是：在wordlist很大的时候，建图耗费的时间太长
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
        wordSet = set(wordList)  # 值得学习，使用list有一个测试样例超时，使用set可以通过

        # 2 BFS搜索
        import collections
        beginQueue = collections.deque([beginWord])
        beiginVisited = {beginWord}
        endQueue = collections.deque([endWord])
        endVisited = {endWord}
        step = 1
        while beginQueue and endQueue:
            beginQSize = len(beginQueue)
            for i in range(beginQSize):
                cur = beginQueue.popleft()
                if cur in endQueue:
                    return step
                for ci, c in enumerate(cur):
                    tmp = list(cur)
                    for k in range(26):
                        tmp[ci] = chr(ord('a') + k)
                        tmpS = ''.join(tmp)
                        if tmpS not in wordSet: continue
                        if tmpS in beiginVisited: continue
                        beiginVisited.add(tmpS)
                        beginQueue.append(tmpS)
            step += 1
            endQSize = len(endQueue)
            for i in range(endQSize):
                cur = endQueue.popleft()
                if cur in beginQueue:
                    return step
                for ci, c in enumerate(cur):
                    tmp = list(cur)
                    for k in range(26):
                        tmp[ci] = chr(ord('a') + k)
                        tmpS = ''.join(tmp)
                        if tmpS not in wordSet: continue
                        if tmpS in endVisited: continue
                        endVisited.add(tmpS)
                        endQueue.append(tmpS)
            step += 1
        return 0

    def ladderLength2_2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            双向BFS 写法优化
            每次选择较小队列进行处理，性能有明显提升
        """
        if beginWord == endWord: return 0
        if endWord not in wordList: return 0
        wordSet = set(wordList)  # 值得学习，使用list有一个测试样例超时，使用set可以通过

        # 2 BFS搜索
        import collections
        beginQueue = collections.deque([beginWord])
        beginVisited = {beginWord}
        endQueue = collections.deque([endWord])
        endVisited = {endWord}
        step = 1
        while beginQueue and endQueue:
            # 每次选择较小的队列进行处理
            if len(beginQueue) > len(endQueue):
                beginQueue, endQueue = endQueue, beginQueue
                beginVisited, endVisited = endVisited, beginVisited
            beginQSize = len(beginQueue)
            for i in range(beginQSize):
                cur = beginQueue.popleft()
                if cur in endQueue:
                    return step
                for ci, c in enumerate(cur):
                    tmp = list(cur)
                    for k in range(26):
                        tmp[ci] = chr(ord('a') + k)
                        tmpS = ''.join(tmp)
                        if tmpS not in wordSet: continue
                        if tmpS in beginVisited: continue
                        beginVisited.add(tmpS)
                        beginQueue.append(tmpS)
            step += 1
        return 0

    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            虚拟顶点
            值得学习：密集图，图中边很多，导致建图时间很长，且存储边的容器很大。可以利用虚拟顶点增加顶点个数，大幅减小边的数量
        """
        if beginWord == endWord: return 0
        if endWord not in wordList: return 0
        nodeNum = 0

        def addWord(word):
            nonlocal nodeNum
            if word in wordId: return wordId[word]
            wordId[word] = nodeNum
            nodeNum += 1
            return wordId[word]

        def addEdge(word):
            id1 = addWord(word)
            for i, c in enumerate(word):
                dummyWord = word[:i] + '*' + word[i + 1:]
                id2 = addWord(dummyWord)
                edge[id1].append(id2)
                edge[id2].append(id1)

        wordId = dict()
        import collections
        edge = collections.defaultdict(list)

        # 1 借助虚拟顶点建图
        for word in wordList:
            addEdge(word)

        addEdge(beginWord)  # 起点与图建立链接

        beginId = wordId[beginWord]
        endId = wordId[endWord]

        # 2 无权图单源最短路径
        dist = [-1]*len(wordId)
        dist[beginId] = 0
        queue = collections.deque([beginId])
        while queue:
            cur = queue.popleft()
            if cur==endId:
                return dist[endId]//2+1 # 虚拟顶点导致路径2倍，1为初始顶点
            for nxt in edge[cur]:
                if dist[nxt]!=-1: continue  # 已访问
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
        return 0


if __name__ == '__main__':
    wordList, beginWord, endWord = ["hot", "dot", "dog", "lot", "log", "cog"], "hit", "cog"
    # wordList, beginWord, endWord = ['a', 'b', 'c'], 'a', 'c'
    print(Solution().ladderLength(beginWord, endWord, wordList))
    print(Solution().ladderLength2(beginWord, endWord, wordList))
    print(Solution().ladderLength2_2(beginWord, endWord, wordList))
    print(Solution().ladderLength3(beginWord, endWord, wordList))
