class Solution:
    # Date Solved: 11 April 2026, Saturday
    def minTimeToType(self, word: str) -> int:
        total_time = 0
        curr_pos = "a"

        for char in word:
            diff = abs(ord(char) - ord(curr_pos))
            min_dist = min(diff, 26 - diff)  # Clockwise vs Counter-clockwise
            total_time += min_dist + 1
            curr_pos = char
        return total_time
