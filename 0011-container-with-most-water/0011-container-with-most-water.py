class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        n = len(height)
        right = n-1
        maximum_water = 0
        while left<right:
            maximum_water = max(min(height[left], height[right])*(right-left), maximum_water)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maximum_water