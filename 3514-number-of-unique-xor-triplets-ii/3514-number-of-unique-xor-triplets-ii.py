class Solution:
    # Date Solved: 24 July 2026, Friday, POTD
    # Refer: NC Ashish for Approach 1: Brute force and codestorywithMIK for Approach 2
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        """
        # Approach 1: Brute force
        # This will not work as based on given constraints, this will exceed 10^9. Though, you can still go O(n^2).
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
        # Approach 2: XOR Pairs and then XOR triplets
        # By codestorywithMIK
        # Time: O(n^2 + n*maxEl), maxEl = max element in nums
        # Space: O(maxEl), less than next power of 2 after maxEl
        n = len(nums)

        # Store all Pair Xors
        # O(n^2) -> nested loop over all (i, j) pairs
        s1 = set()
        for i in range(n):
            for j in range(i, n):
                s1.add(nums[i] ^ nums[j])

        # |s1| is bounded by O(maxEl), since XOR of two numbers can't exceed the next power of 2
        # So, outer loop runs O(maxEl) times, inner loop runs O(n). Total Time = O(n * maxEl)
        s2 = set()
        for pairXor in s1:
            for num in nums:
                s2.add(pairXor ^ num)

        return len(s2)
