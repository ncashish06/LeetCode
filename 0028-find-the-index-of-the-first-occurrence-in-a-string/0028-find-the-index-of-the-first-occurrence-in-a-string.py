class Solution:
    # Date Solved: 1 July 2026, Wednesday
    # Refer: Namaste DSA (Two Pointers and Sliding Window)
    # Not in NC250 but leads to KMP algorithm
    # Refer: LC. 1967 as well
    def strStr(self, haystack: str, needle: str) -> int:
        """
        # Approach 1: Brute force, Time: O(n*m)
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
                if j == m - 1:
                    return i

        return -1
        """
        # Approach 2: KMP
        # Time: O(n+m) where n = len(haystack), m = len(needle)
        # Space: O(m)
        n = len(haystack)
        m = len(needle)
        lps = [0] * m
        i = 0
        j = 1
        while j < m:
            if needle[i] == needle[j]:
                i += 1
                lps[j] = i
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]
        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == m:
                return i - m
        return -1
        """
        # Approach 3: Rabin Karp
        # Average case time: O(m + n) with m = len(needle), n = len(haystack)
        # Worst case time: O(n*m) due to potential hash collisions forcing the haystack[i:i+m] == needle verification at every window
        # Space: O(1)
        base = 256
        mod = int(1e9 + 7)

        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1

        patternHash = 0
        windowHash = 0

        for i in range(m):
            patternHash = (patternHash * base + ord(needle[i])) % mod
            windowHash = (windowHash * base + ord(haystack[i])) % mod

        power = 1
        for _ in range(m - 1):
            power = (power * base) % mod

        for i in range(n - m + 1):
            if patternHash == windowHash:
                if haystack[i : i + m] == needle:
                    return i

            if i < n - m:
                windowHash = (windowHash - (power * ord(haystack[i])) % mod + mod) % mod
                windowHash = (windowHash * base + ord(haystack[i + m])) % mod

        return -1
        """
