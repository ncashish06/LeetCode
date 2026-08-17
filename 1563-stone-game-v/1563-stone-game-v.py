class Solution:
    # Date Solved: 17 August 2026, Monday, POTD
    # Refer: codestorywithMIK
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # Approach-1: Recursion + Memo
        # Time: O(n^3), Space: O(n^2)
        n = len(stoneValue)
        t = [[-1] * 501 for _ in range(501)]

        # sys.setrecursionlimit(10000)

        def solve(l, r, cumSum):
            if l >= r:
                return 0  # Zero score. No further division possible

            if t[l][r] != -1:
                return t[l][r]

            score = 0
            for mid in range(l, r):
                leftSum = cumSum[mid] - (cumSum[l - 1] if l - 1 >= 0 else 0)  # [l..mid]
                rightSum = cumSum[r] - cumSum[mid]  # mid+1, r

                if leftSum < rightSum:
                    score = max(score, leftSum + solve(l, mid, cumSum))
                elif leftSum > rightSum:
                    score = max(score, rightSum + solve(mid + 1, r, cumSum))
                else:
                    score = max(
                        score,
                        leftSum + solve(l, mid, cumSum),
                        rightSum + solve(mid + 1, r, cumSum),
                    )

            t[l][r] = score
            return score

        cumSum = [0] * n
        cumSum[0] = stoneValue[0]
        for i in range(1, n):
            cumSum[i] = cumSum[i - 1] + stoneValue[i]

        return solve(0, n - 1, cumSum)
