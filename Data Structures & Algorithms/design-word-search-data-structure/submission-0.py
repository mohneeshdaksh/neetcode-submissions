class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for index in range(len(word)):
            if word[index] in node.children:
                node = node.children[word[index]]
            else:
                node.children[word[index]] = TrieNode()
                node = node.children[word[index]]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_end_of_word
            if word[index] != ".":
                if word[index] in node.children:
                    return dfs(node.children[word[index]], index + 1)
                else:
                    return False
            else:
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            
        return dfs(self.root, 0)

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False