class Solution:
    # Date Solved: 11 April 2026, Saturday
    def minimumDistance(self, word: str) -> int:
        def get_dist(p1, p2):
            if p1 is None or p2 is None:
                return 0
            r1, c1 = divmod(ord(p1) - ord("A"), 6)
            r2, c2 = divmod(ord(p2) - ord("A"), 6)
            return abs(r1 - r2) + abs(c1 - c2)

        memo = {}

        def solve(idx, other_pos):
            if idx == len(word):
                return 0

            state = (idx, other_pos)
            if state in memo:
                return memo[state]

            curr_char = word[idx]
            prev_char = word[idx - 1]

            res1 = get_dist(prev_char, curr_char) + solve(idx + 1, other_pos)

            res2 = get_dist(other_pos, curr_char) + solve(idx + 1, prev_char)

            memo[state] = min(res1, res2)
            return memo[state]

        return solve(1, None)
