class Solution:
    # Date Solved: 13 June 2026, Saturday, POTD
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""
        for word in words:
            temp = sum(weights[ord(ch) - ord("a")] for ch in word)
            result += chr(ord("z") - temp % 26)
        return result
