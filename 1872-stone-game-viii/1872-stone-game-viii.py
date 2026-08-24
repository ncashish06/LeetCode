class Solution:
    # Date Solved: 24 August 2026, Monday, POTD
    # Refer: codestorywithMIK
    # Time: O(n), Space: O(n)
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        pre = list(accumulate(stones))
        f = [0] * n
        f[n - 1] = pre[n - 1]
        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], pre[i] - f[i + 1])
        return f[1]
