class Solution:
    # Date Solved: 14 July 2026, Tuesday
    # From codestorywithMIK's Line Sweep Playlist
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """
        # Approach 1: Difference Array Technique
        # Time: O(n), Space: O(max year)
        diff = [0] * 2051  # Years range from 1950 to 2050

        # Apply Difference Array Technique
        for birth, death in logs:
            diff[birth] += 1
            diff[death] -= 1  # not alive in death year

        max_pop = 0
        curr_pop = 0
        result = 1950

        # Sweep through years
        for year in range(1950, 2051):
            curr_pop += diff[year]
            if curr_pop > max_pop:
                max_pop = curr_pop
                result = year

        return result
        """
        # Approach 2: Line Sweep Technique
        # Time: O(n*logn), Space: O(n)
        events = []

        for birth, death in logs:
            events.append((birth, 1))  # birth
            events.append((death, -1))  # death

        events.sort()

        curr = 0
        max_pop = 0
        result = 0

        for year, delta in events:
            curr += delta
            if curr > max_pop:
                max_pop = curr
                result = year

        return result
