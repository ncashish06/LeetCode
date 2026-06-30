class Solution:
    # Date: 30 June 2026, Tuesday, POTD
    # Refer: codestorywithMIK and NeetCode (in NC All) but codestorywithMIK is easy to understand
    # Time: O(2n) = O(n)
    # Space: O(1)
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        mp = [0, 0, 0]  # 0 - a, 1 - b, 2 - c

        i = 0
        j = 0
        while j < n:
            ch = s[j]
            mp[ord(ch) - ord("a")] += 1

            while mp[0] > 0 and mp[1] > 0 and mp[2] > 0:
                result += n - j
                mp[ord(s[i]) - ord("a")] -= 1
                i += 1

            j += 1

        return result
