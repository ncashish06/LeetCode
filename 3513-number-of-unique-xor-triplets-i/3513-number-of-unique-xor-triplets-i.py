class Solution:
    # Date Solved: 23 July 2026, Thursday, POTD
    # Refer: NC Ashish for Approach 1: Brute force and codestorywithMIK for Approach 2
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        """
        # Approach 1: Brute force
        # This will not work as given constraint is 10^5. You can't even go O(n^2).
        # Time: O(n^3), Space: O(n) for result_set
        result_set = set()
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    xor_ijk = nums[i] ^ nums[j] ^ nums[k]
                    result_set.add(xor_ijk)
        return len(result_set)
        """
        # Approach 2:
        # By codestorywithMIK
        # Time: O(log2(n)), Space: O(1)
        # Permutation doesn't matter as XOR remains the same. Result is same for any permutation of numbers in the range [1,n]. Kind of pattern recognition.
        n = len(nums)
        if n == 1 or n == 2:
            return n

        ans = 1  # which is 2^0
        while ans <= n:
            ans *= 2

        return ans
