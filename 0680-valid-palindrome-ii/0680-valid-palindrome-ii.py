class Solution:
    # Date Solved: 19 August 2026, Wednesday
    # NC250
    # Refer: NeetCode
    # Time: O(n), Space: O(1)
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip_l = s[l + 1 : r + 1]  # Go until r
                skip_r = s[l:r]  # Go until r-1
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            l, r = l + 1, r - 1

        return True
