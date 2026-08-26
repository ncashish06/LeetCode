class Solution:
    # Date: 26 August 2026, Wednesday, POTD
    # Refer: codestorywithMIK
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        """
        # Approach 1: Brute force
        # Time: O(n^3), Space: O(n), for temp string of length n
        n = len(s)

        for length in range(k, n + 1):
            result = ""

            for start in range(0, n - length + 1):  # trying all possible substr of len
                temp = s[start : start + length]  # [start ... start+length]

                ones = sum(1 for ch in temp if ch == "1")

                # Keep it if it's beautiful and smaller than current best.
                if ones == k:
                    if not result or temp < result:
                        result = temp

            # if we find result of length size, then it's smallest, no need to move to length+1
            if result:
                return result

        return ""
        """
        # Approach 2: Sliding Window
        # Time: O(n^2), Space: O(1)
        n = len(s)
        i = 0
        ones = 0  # number of '1's in window [i, j]
        result = ""

        for j in range(n):
            if s[j] == "1":
                ones += 1

            # remove extra 1's, then trim leading 0's
            while i <= j and (ones > k or s[i] == "0"):
                if s[i] == "1":
                    ones -= 1
                i += 1

            if ones == k:
                temp = s[i : j + 1]
                if (
                    not result
                    or j - i + 1 < len(result)
                    or (j - i + 1 == len(result) and temp < result)
                ):
                    result = temp

        return result
