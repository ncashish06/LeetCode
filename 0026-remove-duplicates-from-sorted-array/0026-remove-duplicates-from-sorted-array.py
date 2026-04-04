class Solution:
    # Date Solved: 3 April 2026, Friday
    def removeDuplicates(self, nums: List[int]) -> int:
        # integer array = +ve and -ve, non-decreasing is not equal to increasing. It means it can have subsequent number which are same (duplicates)
        # 2 pointer approach (specifically, Read-Write Two-Pointer Pattern)
        # See Problem 27 as well
        if not nums:
            return 0
        last = 0  # index of the last unique number
        for curr in range(1, len(nums)):
            if nums[curr] > nums[last]:  # or simple not equal to check also can be done
                last += 1
                nums[last] = nums[curr]
        return last + 1
