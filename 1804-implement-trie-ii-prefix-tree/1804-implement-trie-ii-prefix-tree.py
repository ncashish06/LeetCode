class TrieNode:
    def __init__(self):
        self.children = {}
        self.countWords = 0  # number of words ending here
        self.countPrefix = 0  # number of words passing through here


class Trie:
    # Date Solved: 29 May 2026, Friday
    # Time: O(n) for each function call where n is the length of the string
    # Space: O(t) where t is the total number of TrieNodes created in the Trie
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.countPrefix += 1  # every node word passes through
        curr.countWords += 1  # only end node

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.countWords

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.countPrefix

    def erase(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
            curr.countPrefix -= 1  # undo what insert did
        curr.countWords -= 1  # undo what insert did


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
