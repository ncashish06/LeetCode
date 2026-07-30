class Solution:
    # Date Solved: 30 July 2026, Thursday
    # In NC All
    # Refer: codestorywithMIK. Below approach works for both this and "LC. 3014 Minimum Number of Pushes to Type Word I (Easy)"
    def minimumPushes(self, word: str) -> int:
        # Time: O(n) + O(26log26) for sorting, Space: O(1)
        mp = [0] * 26
        # count frequency (letters can repeat in Part II unlike in Part I)
        for ch in word:
            mp[ord(ch) - ord("a")] += 1

        mp.sort(reverse=True)  # descending order of frequency

        ans = 0
        for i in range(26):
            freq = mp[i]
            pressed_key = (i // 8) + 1
            ans += freq * pressed_key

        return ans
