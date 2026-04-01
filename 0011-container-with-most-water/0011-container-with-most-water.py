class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx = 0
        right_idx = len(height) - 1
        max_water_volume = 0
        
        while left_idx < right_idx:
            width = right_idx - left_idx
            container_height = min(height[left_idx], height[right_idx]) #height limited by min of 2 heights
            current_water_volume = width * container_height
            max_water_volume = max(max_water_volume, current_water_volume)
            if height[left_idx] < height[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1
                
        return max_water_volume