class Solution:
    # Date Solved: 22 May 2026, Friday, POTD
    # Refer: codestorywithMIK, Neetcode
    def check(self, nums: List[int]) -> bool:
        # Approach 1: Count Peek/Pivot/Rotation Points (Only 1 peek element/index should be present)
        n = len(nums)
        peak = 0

        for i in range(n):
            # Compare each element with the next one (wrap around using modulo)
            if nums[i] > nums[(i + 1) % n]:
                peak += 1

            if peak > 1:
                return False

        return True
