class Vertex:
    def __init__(self, v: str):
        self.val = v
        self.adj = dict()

class Trie:
    def __init__(self):
        self.roots = dict()
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)

        if word[0] not in self.roots:
            self.roots[word[0]] = Vertex(word[0])

        p = self.roots[word[0]]
        for ch in word[1:]:
            if ch not in p.adj:
                p.adj[ch] = Vertex(ch)
            p = p.adj[ch]

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.roots:
            return False

        p = self.roots[prefix[0]]

        for ch in prefix[1:]:
            if ch not in p.adj:
                return False
            p = p.adj[ch]

        return True