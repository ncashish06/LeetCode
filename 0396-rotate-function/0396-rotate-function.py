class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
    
        # Calculate initial sum of elements and F(0)
        total_sum = sum(nums)
        F = sum(i * val for i, val in enumerate(nums))
        
        ans = F
        
        # Use the sliding window/mathematical relationship:
        # F(k) = F(k-1) + sum - n * nums[n - k]
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            ans = max(ans, F)
            
        return int(ans)