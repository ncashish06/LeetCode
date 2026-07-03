class Solution:
    # Date Solved: 3 July 2026, Friday
    # Refer: Namaste DSA, not in NCA All
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Approach 1: Brute Force
        # Time: O(n × (m + n)) with m = len(a), n = len(b), Space: O(m + n)
        """
        The while loop repeats a until text is at least as long as b, which takes about n/m iterations, building text up to length O(m + n).
Each b in text check is a substring search. Worst-case (naive) substring matching costs O(len(text) × len(b)), i.e. O((m+n) × n).
Since this check happens (up to) twice on a string of size O(m+n), the dominant cost is O(n × (m+n)).
"""
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