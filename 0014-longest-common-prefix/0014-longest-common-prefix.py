class Solution:
    # Date Solved: 29 May 2026, Friday
    # NeetCode 250
    # Time: O(n*m), Space: O(1)
    # Where n is the length of the shortest string and  m is the number of strings.
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                # The moment we find a mismatch or reach the end of any string, we've found where the common prefix ends.
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
