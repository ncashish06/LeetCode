class Solution:
    # Date Solved: 3 July 2026, Friday
    # Refer: Namaste DSA, not in NCA All
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        # Approach 1: Brute Force
        # Time: O(n × (m + n)) with m = len(a), n = len(b), Space: O(m + n)
        count = 1
        text = a

        while len(text) < len(b):
            text += a
            count += 1

        if b in text:
            return count

        text += a
        count += 1

        if b in text:
            return count

        return -1
        """
        # Approach 2: Rabin Karp
        # # Time: O(m + n) in average with m = len(a), n = len(b), Space: O(1)
        count = 1
        text = a

        while len(text) < len(b):
            text += a
            count += 1

        if self.rabinKarp(text, b):
            return count

        text += a
        count += 1

        if self.rabinKarp(text, b):
            return count

        return -1

    def rabinKarp(self, text, pattern):
        base = 256
        mod = int(1e9 + 7)

        n = len(text)
        m = len(pattern)

        patternHash = 0
        windowHash = 0

        for i in range(m):
            patternHash = (patternHash * base + ord(pattern[i])) % mod
            windowHash = (windowHash * base + ord(text[i])) % mod

        power = 1
        for _ in range(m - 1):
            power = (power * base) % mod

        for i in range(n - m + 1):
            if patternHash == windowHash:
                if text[i : i + m] == pattern:
                    return True

            if i < n - m:
                windowHash = (windowHash - (power * ord(text[i])) % mod + mod) % mod
                windowHash = (windowHash * base + ord(text[i + m])) % mod

        return False
