class Solution:
    # Date Solved: 1 August 2026, Saturday
    # Blind 75
    # Refer: Claude
    # Time: O(n), Space: O(min(n, k)) where k is the character set size
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}  # char -> most recent index
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                # duplicate found inside current window; shrink from the left
                left = last_seen[char] + 1

            last_seen[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
