class Solution:
    # Date Solved: 22 June 2026, Monday, Same as this day's POTD
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter

        s_count = Counter(s)
        target_count = Counter(target)

        result = float("inf")
        for ch, freq in target_count.items():
            result = min(result, s_count[ch] // freq)

        return result
