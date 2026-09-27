class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for index in range(len(word)):
            if word[index] in node.children:
                node = node.children[word[index]]
            else:
                node.children[word[index]] = TrieNode()
                node = node.children[word[index]]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for index in range(len(word)):
            if word[index] in node.children:
                node = node.children[word[index]]
                if (index == len(word)-1) and node.is_end_of_word:
                    return True
            else:
                return False
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for index in range(len(prefix)):
            if prefix[index] in node.children:
                node = node.children[prefix[index]]
            else:
                return False
        return True

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False