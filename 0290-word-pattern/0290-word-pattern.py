class Solution:
    # Date Solved: 8 July 2026, Wednesday, Part 1 of this week's premium question
    # Refer: codestorywithMIK and NeetCode
    # Part of NC All
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        # Approach 1 (using dict and set)
        # Time: O(n+m) where n is the length of the string pattern and m is the length of the string s
        # Space: O(m) where mp dict and used set store word/char data, dominated by len(s)
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        mp = {}
        used = set()

        for i in range(len(pattern)):
            if words[i] not in mp and pattern[i] not in used:
                used.add(pattern[i])
                mp[words[i]] = pattern[i]
            elif mp.get(words[i]) != pattern[i]:
                return False

        return True
        """
        # Approach 2 (2 maps)
        # Time: O(n+m) where n is the length of the string pattern and m is the length of the string s
        # Space: O(m) where charToWord and wordToChar store word/char data, dominated by len(s)
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        charToWord = {}
        wordToChar = {}

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True
