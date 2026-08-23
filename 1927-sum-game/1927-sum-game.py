class Solution:
    # Date Solved: 23 August 2026, Sunday, POTD
    # Refer: Claude
    # Time: O(n), Space: O(1)
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        sum1 = sum2 = 0
        cnt1 = cnt2 = 0

        for i in range(half):
            if num[i] == "?":
                cnt1 += 1
            else:
                sum1 += int(num[i])

        for i in range(half, n):
            if num[i] == "?":
                cnt2 += 1
            else:
                sum2 += int(num[i])

        diff = sum1 - sum2
        q = cnt1 + cnt2

        # Odd total number of '?' -> Alice always wins
        if q % 2 == 1:
            return True

        # Even total -> Bob wins iff diff exactly balances out to 0
        # when both play optimally filling '?' with digits averaging 4.5 (9/2) each
        return diff != 9 * (cnt2 - cnt1) // 2
