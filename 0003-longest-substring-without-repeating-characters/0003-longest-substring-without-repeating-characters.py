class Solution:
    # Date Solved: 1 August 2026, Saturday
    # Blind 75
    # Refer: NeetCode, no codestorywithMIK
    # Time: O(n), Space: O(m) where n = len(s) and m = unique characters in the string
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                # Shrink the window from the left until the duplicate is removed.
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)  # window size = r-l+1
        return res
