class Solution:
    # Date Solved: 23 July 2026, Thursday
    # Same as POTD of 19 July 2026, Sunday "LC. 1081 Smallest Subsequence of Distinct Characters"
    # Refer: codestorywithMIK
    def removeDuplicateLetters(self, s: str) -> str:
        # Approach-1 (Using string as a stack)
        # Time : O(n), Space : O(1)
        n = len(s)
        result = []

        taken = [False] * 26  # O(1) space
        lastIndex = [0] * 26  # O(1) space

        for i in range(n):
            ch = s[i]
            lastIndex[ord(ch) - ord("a")] = i

        for i in range(n):
            idx = ord(s[i]) - ord("a")

            if taken[idx]:
                continue

            while (
                result
                and s[i] < result[-1]
                and lastIndex[ord(result[-1]) - ord("a")] > i
            ):
                taken[ord(result[-1]) - ord("a")] = False
                result.pop()

            result.append(s[i])
            taken[idx] = True

        return "".join(result)

        """
        # Approach-2 (Using stack)
        # Time : O(n), Space: O(n) stack
        n = len(s)
        st = []  # using a list as a stack

        taken = [False] * 26
        lastIndex = [0] * 26

        for i in range(n):
            ch = s[i]
            lastIndex[ord(ch) - ord("a")] = i

        for i in range(n):
            idx = ord(s[i]) - ord("a")

            if taken[idx]:
                continue

            while st and s[i] < st[-1] and lastIndex[ord(st[-1]) - ord("a")] > i:
                taken[ord(st.pop()) - ord("a")] = False

            st.append(s[i])
            taken[idx] = True

        return "".join(st)
        """
