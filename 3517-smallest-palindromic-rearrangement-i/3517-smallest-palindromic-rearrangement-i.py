class Solution:
    # Date Solved: 28 July 2026, Tuesday, POTD
    # Refer: codestorywithMIK
    def smallestPalindrome(self, s: str) -> str:
        # Approach: Split in half, sort and form palindrome
        # Time: O(nlogn), Space: O(1) (ignoring the space taken for sorting internally)
        s = list(s)
        n = len(s)
        mid = n // 2

        s[:mid] = sorted(s[:mid])  # [0, mid)

        for i in range(mid):
            s[n - 1 - i] = s[i]

        return "".join(s)
