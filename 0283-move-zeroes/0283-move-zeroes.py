class Solution:
    # Date Solved: 10 April 2026, Friday
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Similar concept as in LC problem 26 and 27
        # 2 passes: Time: O(n)
        """
        non_zero_pointer = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:  # Keep moving non-zero elements before
                nums[non_zero_pointer] = nums[i]
                non_zero_pointer += 1

        for i in range(non_zero_pointer, n):  # remaining slors filled by 0s
            nums[i] = 0
        """
        
        # 1 pass: Time: O(n)
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
