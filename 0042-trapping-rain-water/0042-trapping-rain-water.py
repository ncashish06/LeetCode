class Solution:
    def trap(self, height: List[int]) -> int:
        # This is kind of DP
        n = len(height)
        if n==0:
            return 0

        total_volume = 0
        left_wall_limit, right_wall_limit = [0]*n, [0]*n

        left_wall_limit[0] = height[0]
        for i in range(1, n):
            left_wall_limit[i] = max(left_wall_limit[i-1], height[i]) #tallest bar to the left including itself

        right_wall_limit[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_wall_limit[i]=max(right_wall_limit[i+1], height[i]) #tallest bar to the right including itself
            
        for i in range(n): 
            water_level = min(left_wall_limit[i], right_wall_limit[i])
            total_volume += water_level - height[i]

        return total_volume
