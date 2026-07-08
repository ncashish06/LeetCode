class Solution:
    # Date Solved: 8 July 2026, Wednesday, Weekly Premium W2
    # Refer: Claude
    # In NC All
    # There are Word Break 1,2 (dp, backtracking) and Word Search 2 (backtracking, trie) which are B75 or NC150 or NC250.
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        charToWord = {}
        wordToChar = {}

        def backtrack(pIdx: int, sIdx: int) -> bool:
            # Both pattern and s fully consumed -> success
            if pIdx == len(pattern) and sIdx == len(s):
                return True
            # One is exhausted but not the other -> fail
            if pIdx == len(pattern) or sIdx == len(s):
                return False

            c = pattern[pIdx]

            # If c is already mapped, the next word MUST match that mapping exactly
            if c in charToWord:
                word = charToWord[c]
                if s.startswith(word, sIdx):
                    return backtrack(pIdx + 1, sIdx + len(word))
                return False

            # c is unmapped -> try every possible word length starting at sIdx
            for end in range(sIdx + 1, len(s) + 1):
                word = s[sIdx:end]

                if word in wordToChar:
                    continue  # this word is already claimed by another char

                # Tentatively map
                charToWord[c] = word
                wordToChar[word] = c

                if backtrack(pIdx + 1, end):
                    return True

                # Backtrack
                del charToWord[c]
                del wordToChar[word]

            return False

        return backtrack(0, 0)
