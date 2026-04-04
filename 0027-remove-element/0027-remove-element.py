class Solution:
    # Date Solved: 3 April 2026, Friday
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


"""
Since, order of elements doesn't matter. If the elements you want to remove are rare, we just swap the element with last element in the array.
In above approach, we constantly copying elements forward. If we had 1,000 elements and only needed to remove one, we still perform 999 "write" operations. This new approach avoids that by using swapping.
If I find a value I don't want, I'll just grab the very last element in the array, put it here to replace the bad one, and then shrink the array size. Again. all this because order doesn't matter.

        curr = 0
        n = len(nums)
        while curr<n:
            if nums[curr] == val:
                nums[curr] = nums[n - 1]
                n-=1
            else:
                curr+=1
        return curr
"""
