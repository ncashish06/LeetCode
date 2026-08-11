class Solution:
    # Date Solved: 11 August 2026, Tuesday, POTD
    # Refer: codestorywithMIK
    def missingInteger(self, nums: List[int]) -> int:
        # Approach-1: Using set
        # Time: O(n), Space: O(n)
        n = len(nums)
        st = set(nums)
        sequential = nums[0]

        for j in range(1, n):
            if nums[j] == nums[j - 1] + 1:
                sequential += nums[j]
            else:
                break

        while sequential in st:  # O(n)
            sequential += 1

        return sequential
        """
        # Approach-2: Using sorting
        # Time: O(nlogn), Space: O(1)
        n = len(nums)

        sequential = nums[0]
        for j in range(1, n):
            if nums[j] == nums[j - 1] + 1:
                sequential += nums[j]
            else:
                break

        nums.sort()
        for i in range(n):
            if nums[i] == sequential:
                sequential += 1

        return sequential
        """
