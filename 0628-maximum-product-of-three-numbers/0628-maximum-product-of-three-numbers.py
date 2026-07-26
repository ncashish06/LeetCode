class Solution:
    # Date Solved: 26 July 2026, Sunday, POTD
    def maximumProduct(self, nums: List[int]) -> int:
        """
        # Approach 1: Solved on my own
        # Time: O(n log n), Space: O(1)
        nums.sort()
        # Case 1: three largest positive numbers
        candidate1 = nums[-1] * nums[-2] * nums[-3]
        # Case 2: two smallest (could be very negative) * largest
        candidate2 = nums[0] * nums[1] * nums[-1]
        return max(candidate1, candidate2)
        """
        # Approach 2: Track the top 3 max and bottom 2 min as you go
        # Time: O(n), Space: O(1)
        max1 = max2 = max3 = float("-inf")  # top 3 largest
        min1 = min2 = float("inf")  # bottom 2 smallest

        for n in nums:
            # update top 3 max
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n

            # update bottom 2 min
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n

        return max(max1 * max2 * max3, min1 * min2 * max1)
