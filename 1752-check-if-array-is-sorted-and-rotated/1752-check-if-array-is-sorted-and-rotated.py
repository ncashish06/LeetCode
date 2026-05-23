class Solution:
    # Date Solved: 22 May 2026, Friday
    def check(self, nums: List[int]) -> bool:
        # Approach 1: Sliding Window
        # Time: O(n), Space: O(1)
        N = len(nums)
        count = 1  # Start at 1 since a single element is always non-decreasing

        # Iterate through the array twice (simulating a doubled array)
        for i in range(1, 2 * N):
            # Compare current element with previous, using modulo to wrap around
            if nums[(i - 1) % N] <= nums[i % N]:
                count += 1  # Elements are in non-decreasing order, extend the window
            else:
                count = 1  # Break in order found, reset the consecutive count

            # If we found N consecutive non-decreasing elements, it's a valid rotation
            if count == N:
                return True

        # Edge case: single element array is always valid
        return N == 1
        """
        # Approach 2: Count Break/Pivot Points
        count, N = 0, len(nums)

        for i in range(N):
            # Compare each element with the next one (wrap around using modulo)
            # A "break point" is where a larger element is followed by a smaller one
            if nums[i] > nums[(i + 1) % N]:
                count += 1

            # A valid sorted+rotated array has AT MOST one break point (the rotation point).
            # More than one means it's invalid.
            if count > 1:
                return False

        return True
        """
