class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
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
        
        
