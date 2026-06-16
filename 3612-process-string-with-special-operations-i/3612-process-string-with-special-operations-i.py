class Solution:
    # Date Solved: 16 June 2026, Tuesday, POTD
    def processStr(self, s: str) -> str:
        result = ""

        for ch in s:
            if ch == "*":
                if len(result) > 0:
                    result = result[:-1]
            elif ch == "#":
                result += result
            elif ch == "%":
                result = result[::-1]  # or ''.join(reversed(result))
            else:
                result += ch

        return result
