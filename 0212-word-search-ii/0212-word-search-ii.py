class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""  # stores complete word at end node

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word


class Solution:
    # Date Solved: 28 May 2026, Thursday
    # Blind 75, (Word Search I is also Blind 75 but Medium level)
    # Time: O(M * N * 3^L) where M = rows, N = cols, L = length of longest word
    # Space: O(W * L) for Trie storage where W = number of words
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.insert(word)

        ROWS, COLS = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or board[r][c] == "#"
                or board[r][c] not in node.children
            ):
                return

            char = board[r][c]
            node = node.children[char]

            if node.word:
                result.append(node.word)
                node.word = ""  # prevent duplicates

            board[r][c] = "#"
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            board[r][c] = char  # restore

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result
