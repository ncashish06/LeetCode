class Solution:
    # Date Solved: 21 August 2026, Friday, POTD
    # Refer: Claude
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        def count_le(x: int) -> int:
            # count of distinct amounts <= x achievable by ANY single coin,
            # via inclusion-exclusion over subsets of coins
            total = 0
            for mask in range(1, 1 << n):
                l = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        l = lcm(l, coins[i])
                        bits += 1
                if bits % 2 == 1:
                    total += x // l
                else:
                    total -= x // l
            return total

        # k-th multiple of smallest coin is a safe upper bound
        lo, hi = (1, min(coins) * k)
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
