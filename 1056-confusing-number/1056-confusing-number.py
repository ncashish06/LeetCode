class Solution:
    # Date Solved: 29 May 2026, Friday
    # Refer: LC246. Strobogrammatic Number
    # Weekly Premium W5
    def confusingNumber(self, n: int) -> bool:
        inverse_char = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        s = str(n)

        # First check all digits are valid (0,1,6,8,9 only)
        for ch in s:
            if ch not in inverse_char:
                return False

        # Build the rotated number (reverse + map each digit)
        rotated = "".join(inverse_char[ch] for ch in reversed(s))

        return rotated != s
