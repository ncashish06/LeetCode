class Solution:
    # Date Solved: 1 July 2026, Wednesday
    # Refer: Namaste DSA (Two Pointers and Sliding Window)
    # Not in NC250 but leads to KMP algorithm
    def strStr(self, haystack: str, needle: str) -> int:
        # Approach 1: Brute force, Time:  O(n*m)
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            j = 0
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1
