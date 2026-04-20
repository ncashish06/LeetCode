class Solution:
    # Date Solved: 19 April 2026, Sunday
    def maxDistance(self, colors: List[int]) -> int:
        """
        # My solution below also worked
        n = len(colors)
        max_dist = 0
        for i in range(n):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, n - 1 - i)
        return max_dist
        """
        n = len(colors)
        i, j = 0, n - 1

        # Check from the end against the first element
        while colors[0] == colors[j]:
            j -= 1

        # Check from the beginning against the last element
        while colors[i] == colors[n - 1]:
            i += 1

        return max(j, n - 1 - i)
