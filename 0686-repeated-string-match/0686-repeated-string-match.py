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
        # Average case time: O(m + n) with m = len(pattern), n = len(text)
        # Worst case time: O(n*m) due to potential hash collisions forcing the text[i:i+m] == pattern verification at every window
        # Space: O(1)
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

        if m > n:
            return False

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
        """
        # Approach 3: KMP
        # Time: O(n+m) where n = len(text), m = len(pattern)
        # Space: O(m)
        count = 1
        text = a

        while len(text) < len(b):
            text += a
            count += 1

        if self.kmpSearch(text, b):
            return count

        text += a
        count += 1

        if self.kmpSearch(text, b):
            return count

        return -1

    def kmpSearch(self, text: str, pattern: str) -> bool:
        n = len(text)
        m = len(pattern)

        if m == 0:
            return True
        if m > n:
            return False

        lps = [0] * m
        i = 0
        j = 1
        while j < m:
            if pattern[i] == pattern[j]:
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
            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == m:
                return True
        return False
    """
