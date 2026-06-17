class Solution:
    # Date Solved: 17 June 2026, Wednesday, POTD
    # Refer: codestorywithMIK
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        L = 0
        for ch in s:
            if ch == "*":
                if L > 0:
                    L -= 1
            elif ch == "#":
                L *= 2
            elif ch == "%":
                # reverse - no change in L
                continue
            else:  # 'a' to 'z'
                L += 1

        if k >= L:
            return "."

        for i in range(n - 1, -1, -1):
            ch = s[i]
            if ch == "*":
                L += 1  # no change in k
            elif ch == "%":
                # no change in L
                k = L - k - 1
            elif ch == "#":
                L //= 2
                k = k - L if k >= L else k
            else:  # 'a' to 'z'
                L -= 1

            if k == L:
                return ch

        return "."
