class Solution:
    # Date Solved: 7 April 2026, Tuesday
    # Time: O(nq) where n is the length of nums, and q is the number of queries.
    # Space: O(1)
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        res = 0
        MOD = 10**9 + 7
        for q in range(len(queries)):
            l, r, k, v = queries[q]
            idx = l
            for idx in range(l, r + 1, k):  # for loop faster than while loop
                # while idx <=r:
                nums[idx] = (nums[idx] * v) % MOD
                # idx+=k

        for i in range(len(nums)):
            res ^= nums[i]

        return res
