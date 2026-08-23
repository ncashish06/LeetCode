class Solution:
    # Date Solved: 21 August 2026, Friday, POTD
    # Refer: codestorywithMIK
    # Time: O(log(maxCoin*k)*(2^n)*n*log(maxCoin)), Space: O(1)
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def countSmaller(mid: int) -> int:
            correctedCount = 0
            n = len(coins)

            # 2^n - 1 non-empty subsets
            for expressions in range(1, (1 << n)):
                lcm = 0
                order = 0  # count of coins taken in this subset

                for i in range(n):
                    if expressions & (1 << i):
                        order += 1
                        if lcm == 0:
                            lcm = coins[i]
                        else:
                            lcm = lcm * coins[i] // gcd(lcm, coins[i])

                if order % 2 == 0:  # even -> subtract
                    correctedCount -= mid // lcm
                else:  # odd -> add
                    correctedCount += mid // lcm

            return correctedCount

        l, r = 1, max(coins) * k
        result = -1

        while l <= r:
            mid = l + (r - l) // 2

            if countSmaller(mid) >= k:
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result
