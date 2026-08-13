class Solution:
    # Date Solved: 12 August 2026, Wednesday
    # Blind 75
    # Refer: codestorywithMIK for optimal and NeetCode for brute-force and optimal
    def maxArea(self, height: List[int]) -> int:
        """
        # Approach 1: Brute force
        # Time: O(n^2), Space: O(1)
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                res = max(res, min(height[i], height[j]) * (j - i))
        return res
        """
        # Approach 2: Two Pointers, Greedy
        # Time: O(n), Space: O(1)
        n = len(height)
        i, j = 0, n - 1
        water = 0

        while i < j:
            # start from the smallest one and calculate water
            h = min(height[i], height[j])
            w = j - i
            area = h * w
            water = max(water, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return water
