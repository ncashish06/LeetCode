class Solution:
    # Date Solved: 22 June 2026, Monday, POTD
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter

        target = "balloon"
        text_count = Counter(text)
        target_count = Counter(target)

        result = float("inf")
        for ch, freq in target_count.items():
            result = min(result, text_count[ch] // freq)

        return result
