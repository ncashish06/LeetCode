class Solution:
    # Date Solved: 29 June 2026, Monday, POTD
    # Refer: codestorywithMIK. This is KMP algorithm.
    def computeLPS(self, pattern: str) -> list[int]:
        M = len(pattern)
        lps = [0] * M
        length = 0
        i = 1

        while i < M:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def kmpSearch(self, pat: str, txt: str) -> bool:
        N, M = len(txt), len(pat)
        lps = self.computeLPS(pat)

        i = 0  # index for txt
        j = 0  # index for pat

        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == M:
                return True  # pattern found
            elif i < N and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return False

    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for pat in patterns:
            if self.kmpSearch(pat, word):
                count += 1
        return count
