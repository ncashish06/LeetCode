class Solution:
    # Date Solved: 30 July 2026, Thursday, POTD
    # Refer: codestorywithMIK. Approach 2 works for both this and "LC. 3016 Minimum Number of Pushes to Type Word II (Medium)"
    def minimumPushes(self, word: str) -> int:
        """
        # Approach-1: Using Map and doing as asked in Problem
        # Time: O(n), Space: O(n)
        if len(word) <= 8:
            return len(word)

        count = 0
        mp = {}  # You can use an array of size 10 also and use index 2 to 9

        assign = 2
        for ch in word:
            if assign > 9:
                assign = 2

            mp[assign] = mp.get(assign, 0) + 1
            count += mp[assign]
            assign += 1

        return count
        """
        # Approach-2: Simplified Approach-1 above
        # Time: O(n) + O(26log26) for sorting, Space: O(1)
        mp = [0] * 26
        # Mentioned in question that all letters will be distinct, unlike in LC. 3016
        for ch in word:
            mp[ord(ch) - ord("a")] = 1

        mp.sort(reverse=True)  # descending order of frequency

        ans = 0
        for i in range(26):
            freq = mp[i]  # always 1 or 0 as no duplicates
            # if not freq: # optional: once sorted all ones come before zeroes
            #    break
            pressed_key = (i // 8) + 1
            ans += freq * pressed_key

        return ans
