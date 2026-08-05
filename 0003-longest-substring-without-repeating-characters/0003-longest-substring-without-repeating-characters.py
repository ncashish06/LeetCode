class Solution:
    # Date Solved: 1 August 2026, Saturday
    # Blind 75
    # Refer: NeetCode, no codestorywithMIK
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        # Approach 1: Brute force
        # Time: O(n*m), Space: O(m) where n = len(s) and m = unique characters in the string
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res
        """
        # Approach 2: Optimal - Sliding Window
        # Time: O(n), Space: O(m) where n = len(s) and m = unique characters in the string
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
