class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = { len(s) : 0 }
        trie = Trie(dictionary).root
        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.is_word:
                    res = min(res, dfs(j+1))
            dp[i] = res
            return res
        return dfs(0)
    
class Trie:
    def __init__(self, dictionary):
        self.root = TrieNode()
        for word in dictionary:
            curr = self.root
            for w in word:
                if w not in curr.children:
                    curr.children[w] = TrieNode()
                curr = curr.children[w]
            curr.is_word = True

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False