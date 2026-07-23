class Solution:
    # Date Solved: 23 July 2026, Thursday
    # POTD of 21 July 2026, Tuesday (Unsolved due to Bari trip)
    # Refer: codestorywithMIK
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Approach: target 1s and find max pair sum of zero blocks
        # Time: O(n), Space: O(n)
        n = len(s)

        # existing count of 1s
        activeCount = s.count("1")

        inactiveBlocks = []
        i = 0
        while i < n:
            if s[i] == "0":
                start = i
                while i < n and s[i] == "0":
                    i += 1
                inactiveBlocks.append(i - start)
            else:
                i += 1

        maxPairSum = 0
        # max(inactiveBlocks[i] + inactiveBlocks[i-1])
        for i in range(1, len(inactiveBlocks)):
            maxPairSum = max(maxPairSum, inactiveBlocks[i] + inactiveBlocks[i - 1])

        return maxPairSum + activeCount
