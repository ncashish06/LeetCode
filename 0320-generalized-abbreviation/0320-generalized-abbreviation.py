class Solution:
    # Date Solved: 15 July 2026, Wednesday, Weekly Premium W3
    # Time: O(n*2^n) — 2^n possible abbreviations, each takes O(n) to build
    # Space: O(n) recursion depth (excluding output)
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []

        def backtrack(index, current, count):
            if index == len(word):
                if count > 0:
                    current += str(count)
                result.append(current)
                return

            # Option 1: skip this character (abbreviate it) -> increase count
            backtrack(index + 1, current, count + 1)

            # Option 2: keep this character as-is
            # First, flush any pending count as a number, then add the letter
            backtrack(
                index + 1, current + (str(count) if count > 0 else "") + word[index], 0
            )

        backtrack(0, "", 0)
        return result
