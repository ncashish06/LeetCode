class Solution:
    # Date Solved: 5 April 2026, Sunday
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Think length of encodedText as area = rows*col
        if rows == 1:
            return encodedText
        n = len(encodedText)
        cols = n // rows
        res = []
        # Start at each column of the first row (row 0)
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                index = r * cols + c
                res.append(encodedText[index])
                r += 1
                c += 1
        return "".join(res).rstrip()

        # Abhijit's solution: Collapsed the above 2D grid logic into a 1D index jump.
        # This works because moving "one row down and one column right" in a flattened string is mathematically equivalent to jumping forward by cols + 1 characters.
        original_text = ""
        cols = len(encodedText) // rows

        for i in range(cols):
            next_pos = i
            while next_pos < len(encodedText):
                original_text += encodedText[next_pos]
                next_pos += cols + 1  # Jump to next_pos

        return original_text.rstrip()
