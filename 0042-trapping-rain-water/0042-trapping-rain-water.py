class Solution:
    def trap(self, height: List[int]) -> int:
        # This is kind of DP
        n = len(height)
        trapped_water = 0
        max_left, max_right = [0]*n, [0]*n
        max_left[0], max_right[n-1] = height[0], height[n-1]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])

        for j in range(n-2, -1, -1):
            max_right[j]=max(max_right[j+1], height[j])
            
        for k in range(n): 
            trapped_water+=min(max_left[k], max_right[k]) - height[k]
            total_trapped_water = trapped_water if trapped_water >= 0 else 0 

        return total_trapped_water
