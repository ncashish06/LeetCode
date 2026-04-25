class Solution:
    # Date Solved: 25 April 2026, Saturday
    # Refer Namaste DSA Video 8 (Warm up)
    def secondHighest(self, s: str) -> int:
        first, second = float("-inf"), float("-inf")
        for char in s:
            if char.isdigit():
                num = int(char)

                if num > first:
                    second = first
                    first = num
                elif num > second and num != first:  # to skip duplicates
                    second = num

        return int(second) if second != float("-inf") else -1
