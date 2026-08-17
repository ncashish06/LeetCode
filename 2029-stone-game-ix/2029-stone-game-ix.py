class Solution:
    # Date Solved: 16 August 2026, Sunday, POTD
    # Refer: codestorywithMIK
    # Approach: Modular Arithmetic and Count Comparison
    # Time: O(n), Space: O(1)
    def stoneGameIX(self, stones: List[int]) -> bool:
        c0 = 0
        c1 = 0
        c2 = 0

        for stone in stones:
            if stone % 3 == 0:
                c0 += 1
            elif stone % 3 == 1:
                c1 += 1
            else:
                c2 += 1

        if c0 % 2 == 0:  # even
            return (c1 >= 1 and c2 >= 1) and (c2 >= c1 or c1 >= c2)

        return abs(c1 - c2) >= 3
