class Solution:
    # Date Solved: 13 July 2026, Monday
    # Blind 75
    # Refer: structy.net
    # Time: O(n + m) one pass to build each count dict, plus O(k) to compare them (k = number of unique characters)
    # Space: O(k) for each dictionary, where k <= 26 for lowercase letters, so effectively O(1)
    def char_count(self, s):
        count = {}

        for char in s:
            if char not in count:
                count[char] = 0

            count[char] += 1

        return count

    def isAnagram(self, s: str, t: str) -> bool:
        count_s = self.char_count(s)
        count_t = self.char_count(t)

        # Different number of unique characters means they can't match
        if len(count_s) != len(count_t):
            return False

        # Check every key in count_s exists in count_t with the same value
        for char in count_s:
            if char not in count_t:
                return False
            if count_s[char] != count_t[char]:
                return False

        return True
