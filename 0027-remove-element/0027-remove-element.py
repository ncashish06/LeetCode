class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 2 pointer approach (specifically, Read-Write Two-Pointer Pattern)
        # See Problem 26 as well
        last = 0
        for curr in range(
            len(nums)
        ):  # start from 0 as 1st element maybe the element to be removed
            if nums[curr] != val:
                nums[last] = nums[curr]
                last += 1
        return last
