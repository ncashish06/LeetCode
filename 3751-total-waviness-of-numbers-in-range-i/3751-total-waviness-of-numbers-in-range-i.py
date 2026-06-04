class Solution:
    # Date Solved: 4 June 2026, Thursday
    def totalWaviness(self, num1: int, num2: int) -> int:
        def findWaveScore(num):
            s = str(num)
            if len(s) < 3:
                return 0
            score = 0
            for i in range(1, len(s) - 1):
                if s[i] > s[i - 1] and s[i] > s[i + 1]:  # peak
                    score += 1
                if s[i] < s[i - 1] and s[i] < s[i + 1]:  # valley
                    score += 1
            return score

        total_score = 0
        for num in range(num1, num2 + 1):
            total_score += findWaveScore(num)
        return total_score
        # return sum(findWaveScore(num) for num in range(num1, num2 + 1)) # Pythonic way
