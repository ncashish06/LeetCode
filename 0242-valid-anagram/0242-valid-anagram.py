class Solution:
    # Date Solved: 16 April 2026, Thursday
    # Refer: structy.net
    def char_count(self, s):
        count = {}

        for char in s:
            if char not in count:
                count[char] = 0

            count[char] += 1

        return count

    def isAnagram(self, s: str, t: str) -> bool:
        return self.char_count(s) == self.char_count(t)
