class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # think length of encodedText as area = rows*col
        """
        if rows == 1:
            return encodedText
        n = len(encodedText)
        cols = n // rows
        res = []
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                index = r * cols + c
                res.append(encodedText[index])
                r += 1
                c += 1
        return "".join(res).rstrip()
        """
        original_text = ""
        cols = len(encodedText)//rows

        for i in range(cols):
            next_pos = i
            while next_pos < len(encodedText):
                original_text += encodedText[next_pos]
                next_pos += cols + 1 #Jump to next_poss

        return original_text.rstrip()
        
        
