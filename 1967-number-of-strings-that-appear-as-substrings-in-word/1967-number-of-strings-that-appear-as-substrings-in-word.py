class Solution:
    # Date Solved: 29 June 2026, Monday, POTD
    # Refer: NamasteDSA or codestorywithMIK (KMP algorithm). Both are same but variable names are slightly different.
    # Refer: LC. 28 as well
    # Time: O(sum(word + patterns[i])) for i in range(k),  where k = number of patterns, W = length of word, P = sum of lengths of all patterns (sum(len(p) for p in patterns))
    # Space: O(max(|patterns[i]|))
    def computeLPS(self, pattern: str) -> list[int]:
        m = len(pattern)
        lps = [0] * m
        i = 0
        j = 1

        while j < m:
            if pattern[i] == pattern[j]:
                i += 1
                lps[j] = i
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]

        return lps

    def kmpSearch(self, needle: str, haystack: str) -> bool:
        n, m = len(haystack), len(needle)
        lps = self.computeLPS(needle)

        i = j = 0  # i: index for haystack, j: index for needle
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == m:
                return True  # pattern found

        return False

    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for pat in patterns:
            if self.kmpSearch(pat, word):
                count += 1
        return count
