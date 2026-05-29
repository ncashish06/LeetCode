class Solution:
    # Date Solved: 14 April 2026, Tuesday
    # NeetCode 250
    # Time: O(n*m), Space: O(1)
    # Where n is the length of the shortest string and  m is the number of strings.
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
