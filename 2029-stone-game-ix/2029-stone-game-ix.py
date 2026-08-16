class Solution:
    # Date Solved: 16 August 2026, Sunday, POTD
    # Refer: codestorywithMIK
    # Time: O(n), Space: O(1)
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt0 = cnt1 = cnt2 = 0
        for val in stones:
            if (typ := val % 3) == 0:
                cnt0 += 1
            elif typ == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
        return cnt1 - cnt2 > 2 or cnt2 - cnt1 > 2
