class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        p1 = p2 = 0

        for i in range(n):
            curr = max(nums[i] + p2, p1)
            temp = p1
            p1 = curr
            p2 = temp
            curr += 1
        return p1