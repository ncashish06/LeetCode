class Solution:
    # Date Solved: 26 May 2026, Tuesday, POTD
    def numberOfSpecialChars(self, word: str) -> int:
        char_freq = [0] * 123
        count = 0
        for ch in word:
            ascii_val = ord(ch)
            char_freq[ascii_val] += 1
            if 65 <= ascii_val <= 90:  # uppercase
                complement_ascii = ascii_val + 32
                if char_freq[ascii_val] == 1 and char_freq[complement_ascii] > 0:
                    count += 1
            else:  # lowercase
                complement_ascii = ascii_val - 32
                if char_freq[ascii_val] == 1 and char_freq[complement_ascii] > 0:
                    count += 1
        return count
