class Solution:
    # Date Solved: 25 June 2026, Thursday, POTD
    # Refer: codestorywithMIK
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        """
        # Approach 1: Brute force TLE, Time: O(n^3)
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i, n):
                count = 0
                for k in range(i, j + 1):
                    if nums[k] == target:
                        count += 1
                if count > (j - i + 1) // 2:
                    res += 1
        return res

        # Approach 2: Brute force, Time: O(n^2)
        n = len(nums)
        res = 0

        for i in range(n):
            count = 0
            for j in range(i, n):
                if nums[j] == target:
                    count += 1
                if count > (j - i + 1) // 2:
                    res += 1
        return res
        """
        # Approach 3: Optimized Brute force (no division), Time: O(n^2)
        n = len(nums)
        res = 0

        for i in range(n):
            count = 0
            for j in range(i, n):
                # Inspired by Boyer-Moore: Same +1/-1 trick to track if target is "winning" but different. Boyer-Moore resets candidate when count hits 0
                if nums[j] == target:
                    count += 1
                else:
                    count -= 1
                if count > 0:
                    res += 1
        return res
