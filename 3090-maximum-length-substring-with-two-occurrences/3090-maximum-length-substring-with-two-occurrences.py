class Solution:
    # Date Solved: 14 August 2026, Friday, POTD
    # Refer: LC2958. Length of Longest Subarray With at Most K Frequency, 12 August 2026, Wednesday, POTD
    # Approach: Classic Khandani Sliding Window Template
    # Time: O(n), Space: O(1)
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        mp = defaultdict(int)

        i = 0
        j = 0
        result = 0

        while j < n:
            mp[s[j]] += 1

            while mp[s[j]] > 2:
                mp[s[i]] -= 1
                i += 1

            result = max(result, j - i + 1)
            j += 1

        return result
