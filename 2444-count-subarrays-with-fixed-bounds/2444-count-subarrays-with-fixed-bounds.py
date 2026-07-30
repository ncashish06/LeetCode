class Solution:
    # Date Solved: 24 July 2026, Friday
    # codestorywithMIK says asked yesterday in Adobe OA.
    # Refer: codestorywithMIK
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        # Approach-1: Brute Force - Find all subarrays and check if min is minK and max is maxK
        # Time: O(n^2), Space: O(1)
        n = len(nums)
        count = 0

        for start in range(n):
            currentMin = nums[start]
            currentMax = nums[start]

            for end in range(start, n):
                currentMin = min(currentMin, nums[end])
                currentMax = max(currentMax, nums[end])

                if currentMin == minK and currentMax == maxK:
                    count += 1

        return count
        """
        # Approach-2 : Sliding Window
        # Time: O(n), Space: O(1)
        ans = 0

        minPosition = -1
        maxPosition = -1
        culpritIdx = -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                culpritIdx = i

            if nums[i] == minK:
                minPosition = i
            if nums[i] == maxK:
                maxPosition = i

            count = min(maxPosition, minPosition) - culpritIdx

            ans += 0 if count <= 0 else count

        return ans
