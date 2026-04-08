class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        res = 0
        for q in range(len(queries)):
            l, r, k, v = queries[q]
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (10**9 + 7)
                idx+=k
        
        for i in range(len(nums)):
            res^=nums[i]

        return res