class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            cid = ord(c) - ord('a')
            if not node.children[cid]:
                node.children[cid] = Trie()
            node = node.children[cid] # 深度前进
        node.isEnd=True

    def searchPrefix(self, prefix: str) -> 'Trie':
        node = self
        for c in prefix:
            cid = ord(c) - ord('a')
            if not node.children[cid]:
                return None
            node = node.children[cid]
        return node

    def search(self, word: str) -> bool:
        node =self.searchPrefix(word)
        return node is not None and node.isEnd


    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
