class Solution:
    # Date Solved: 16 August 2026, Sunday
    # Blind 75
    # Refer: codestorywithMIK
    # Time: O(m+n) where m = length of s and n = length of t
    # Space: O(n)
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        mp = defaultdict(int)

        for ch in t:
            mp[ch] += 1

        required_count = len(t)
        i = 0
        j = 0
        min_window_start = 0
        min_window_size = float("inf")

        while j < n:
            ch_j = s[j]
            if mp[ch_j] > 0:
                required_count -= 1

            mp[ch_j] -= 1

            while required_count == 0:  # try to shrink the window
                curr_window_size = j - i + 1
                if curr_window_size < min_window_size:
                    min_window_size = curr_window_size
                    min_window_start = i

                ch_i = s[i]
                mp[ch_i] += 1
                if mp[ch_i] > 0:
                    required_count += 1
                i += 1

            j += 1

        return (
            ""
            if min_window_size == float("inf")
            else s[min_window_start : min_window_start + min_window_size]
        )
