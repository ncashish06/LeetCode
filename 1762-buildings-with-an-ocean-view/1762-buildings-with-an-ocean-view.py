class Solution:
    # Date Solved: 24 May 2026, Sunday
    # Dhruv Patel (ASU) mentioned that this was asked in Meta interview
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        max_height = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]

        result.reverse()
        return result  # or return result[::-1]
