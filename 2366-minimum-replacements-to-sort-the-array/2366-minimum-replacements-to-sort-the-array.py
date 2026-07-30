class Solution:
    # Date Solved: 30 July 2026, Thursday
    # codestorywithMIK says asked recently by Datazip in Online Assessment
    # Refer: codestorywithMIK
    def minimumReplacement(self, nums: List[int]) -> int:
        # Using Greedy Approach
        # Time: O(n), Space: O(1)
        n = len(nums)
        result = 0

        for i in range(n - 2, -1, -1):
            splits = nums[i] // nums[i + 1]

            if nums[i] % nums[i + 1] != 0:
                splits += 1

            nums[i] = nums[i] // splits
            result += splits - 1

        return result
