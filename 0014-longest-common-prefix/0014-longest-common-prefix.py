class Solution:
    # Date Solved: 14 April 2026, Tuesday
    # NeetCode 250
    # Time: O(n*m), Space: O(1)
    # Where n is the length of the shortest string and  m is the number of strings.
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]  # Initial Prefix Candidate

        for i in range(1, len(strs)):
            j = 0

            # Stop if we reach the end of either string or characters don't match
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1

            # Trim prefix to only the matched portion,
            # If j=0 (no match), prefix becomes "" and we can stop early
            prefix = prefix[:j]
            if not prefix:
                return ""

        return prefix
