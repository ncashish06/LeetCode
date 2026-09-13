class Solution:
    # Date Solved: 12 August 2026, Wednesday
    # Blind 75
    # Refer: B2Go, codestorywithMIK
    def maxArea(self, height: List[int]) -> int:
        """
        # Approach 1: Brute force
        # Time: O(n^2), Space: O(1)
        max_water = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                water = min(height[i], height[j]) * (j - i)
                max_water = max(max_water, water)
        return max_water
        """
        # Approach 2: Two Pointers, Greedy
        # Time: O(n), Space: O(1)
        n = len(height)
        left, right = 0, n - 1
        max_water = 0

        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:  # if both left and right have same height then move both pointers inwards
                left += 1
                right -= 1
        return max_water
