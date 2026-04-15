class Solution:
    # Date Solved: 14 April 2026, Tuesday
    # Time: O(nL), L = length of word
    # Related: https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = n = len(words)
        for i, word in enumerate(words):
            if word == target:
                ans = min(ans, abs(i - startIndex), n - abs(i - startIndex)) # Clockwise vs Counter-clockwise
        return ans if ans < n else -1
