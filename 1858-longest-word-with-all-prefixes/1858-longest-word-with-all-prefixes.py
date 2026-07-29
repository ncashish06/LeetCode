# Date Solved: 29 July 2026, Wednesday, Weekly Premium W5
# Refer: Claude and Trie Notes


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the trie
    # Time:  O(l), where l = len(word) — one step per character
    # Space: O(l), for the new nodes created along this word's path
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    # Check if all prefixes of the word exist in the trie
    # Time:  O(l), where l = len(word) — one step per character
    # Space: O(1) extra (excluding the trie itself)
    def has_all_prefixes(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children or not curr.children[char].is_end_of_word:
                return False
            curr = curr.children[char]
        return True


class Solution:
    # Let n = len(words), l = length of the longest word.
    # Inserting all words: O(n*l), since each of the n calls to insert() costs up to O(l)
    # Checking all words: O(n*l), since each of the n calls to has_all_prefixes() costs up to O(l)
    # Time:  O(n*l)
    # Space: O(n*l), for the trie — worst case (no shared prefixes) creates up to (n*l) nodes
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        longest_valid_word = ""

        # Insert all words into the trie
        for word in words:
            root.insert(word)

        # Check each word and update the longest valid word
        for word in words:
            if root.has_all_prefixes(word):
                if len(word) > len(longest_valid_word) or (
                    len(word) == len(longest_valid_word) and word < longest_valid_word
                ):
                    longest_valid_word = word

        return longest_valid_word
