class TrieNode(dict):
    def __init__(self):
        self.is_end = False

class WordDictionary(dict):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node:
                node[char] = TrieNode()
            node = node[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        return self._search(word, self.root)

    def _search(self, word: str, node: TrieNode) -> bool:
        for i, char in enumerate(word):
            if char == ".":
                for child in node.values():
                    if self._search(word[i+1:], child):
                        return True
                return False
            elif char not in node:
                return False

            node = node[char]

        return node.is_end