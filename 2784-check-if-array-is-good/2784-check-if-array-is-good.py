class Solution:
    # Date Solved: 13 May 2026, Wednesday
    def isGood(self, nums: List[int]) -> bool:
        """
        # Approach 1: My approach. Time: O(nlogn)
        maxVal = max(nums)
        if len(nums) < maxVal + 1:
            return False
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] != i + 1:
                return False
        return nums[-1] == nums[-2]
        """
        # Approach 2: Optimized. Time: O(n)
        # Trick: Use numbers as index and negate values if visited
        # Refer: codestorywithMIK
        n = len(nums)
        expected_max = n - 1
        max_el_count = 0

        for num in nums:
            val = abs(num)  # Use abs since we negate values to mark visited

            if val > expected_max:
                return False
            elif val == expected_max:
                max_el_count += 1

            # Check if index 'val' has been visited before (negative = visited)
            if nums[val] < 0:
                # Revisiting a normal index means duplicate — invalid
                if val != expected_max:
                    return False
                # n-1 can appear twice at most, more than that is invalid
                elif max_el_count > 2:
                    return False
            else:
                # Mark index 'val' as visited by negating it
                nums[val] *= -1

        return True
