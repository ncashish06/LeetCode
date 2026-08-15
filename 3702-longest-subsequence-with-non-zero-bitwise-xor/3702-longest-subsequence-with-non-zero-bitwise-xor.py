class Solution:
    # Date Solved: 15 August 2026, Saturday, POTD
    # Refer: codestorywithMIK
    # Approach: Simple Observation of XOR property
    # Time: O(n), Space: O(1)
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        resultXor = 0
        allZero = True

        for x in nums:
            resultXor ^= x
            if x != 0:
                allZero = False

        if allZero:
            return 0

        return n - 1 if resultXor == 0 else n
