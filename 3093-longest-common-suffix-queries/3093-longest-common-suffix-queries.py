class TrieNode:
    def __init__(self):
        self.children = {}
        self.bestIdx = -1  # index of shortest/earliest word in wordsContainer


class Solution:
    # Date Solved: 28 May 2026, Thursday, POTD
    # Time: O(C + Q) where C = total characters in wordsContainer, Q = total characters in wordsQuery
    # Space: O(C) for the Trie
    # Refer: codestorywithMIK Trie series
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()

        # Build suffix trie using reversed wordsContainer
        for idx, word in enumerate(wordsContainer):
            cur = root
            # Update bestIdx at root level (handles zero common suffix case)
            if cur.bestIdx == -1 or len(word) < len(wordsContainer[cur.bestIdx]):
                cur.bestIdx = idx

            for c in reversed(word):
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
                # At every node, store the best candidate seen so far
                if cur.bestIdx == -1 or len(word) < len(wordsContainer[cur.bestIdx]):
                    cur.bestIdx = idx

        # Query
        result = []
        for word in wordsQuery:
            cur = root
            for c in reversed(word):
                if c not in cur.children:
                    break
                cur = cur.children[c]
            result.append(cur.bestIdx)

        return result
