class Solution:
    # Date Solved: 23 July 2026, Thursday
    # POTD of 19 July 2026, Sunday (Unsolved due to Bari trip)
    # Refer: codestorywithMIK's "LC. 316 Remove Duplicate Letters" video which is exactly same.
    def smallestSubsequence(self, s: str) -> str:
        # Approach-1 (Using string as a stack)
        # Time : O(n), Space : O(1)
        n = len(s)
        result = []  # acts as our stack

        taken = [False] * 26  # is char currently in result?
        lastIndex = [0] * 26  # last occurrence index of each char

        # precompute last index of every character
        for i in range(n):
            ch = s[i]
            lastIndex[ord(ch) - ord("a")] = i

        for i in range(n):
            idx = ord(s[i]) - ord("a")

            if taken[idx]:  # already in result, skip (keep first/earlier position)
                continue

            # pop from result if:
            # 1) current char is smaller (helps get lexicographically smaller result)
            # 2) top of result appears again later (so it's safe to remove now)
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

            # same greedy pop condition as approach-1
            while st and s[i] < st[-1] and lastIndex[ord(st[-1]) - ord("a")] > i:
                taken[ord(st.pop()) - ord("a")] = False

            st.append(s[i])
            taken[idx] = True

        return "".join(st)
        """
