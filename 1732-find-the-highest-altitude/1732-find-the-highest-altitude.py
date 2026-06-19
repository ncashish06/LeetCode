class Solution:
    # Date Solved: 19 June 2026, Friday, POTD
    def largestAltitude(self, gain: List[int]) -> int:
        curr, max_alt = 0, 0
        for i in range(len(gain)):
            curr += gain[i]
            max_alt = max(max_alt, curr)
        return max_alt
