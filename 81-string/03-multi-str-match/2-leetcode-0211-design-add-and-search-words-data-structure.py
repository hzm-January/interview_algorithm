class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            cid = ord(c) - ord('a')
            if not node.children[cid]:
                node.children[cid] = TrieNode()
            node = node.children[cid]
        node.isEnd = True


class WordDictionary:

    def __init__(self):
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        self.trieRoot.insert(word)

    def search(self, word: str) -> bool:

        def dfs(index:int, node:TrieNode)->bool:
            if index == len(word):
                return node.isEnd
            c = word[index]
            if c!='.':
                child = node.children[ord(c) - ord('a')]
                if child and dfs(index+1, child):
                    return True
            else:
                for child in node.children:
                    if child and dfs(index+1, child):
                        return True
            return False

        return dfs(0, self.trieRoot)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
