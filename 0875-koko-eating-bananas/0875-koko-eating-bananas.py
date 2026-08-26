class Solution:
    # Date Solved: 25 August 2026, Tuesday
    # NC150
    # Refer: codestorywithMIK
    # Approach: Binary Search - Using same concept as LC2187 : Minimum Time to Complete Trips
    # Time: O(n*logm) where n=length of piles and m=maximum number of bananas in a piles
    # Space: O(1)
    def canEatAll(self, piles: List[int], givenHour: int, h: int) -> bool:
        actualHour = 0

        for x in piles:
            actualHour += x // givenHour

            if x % givenHour != 0:
                actualHour += 1

        return actualHour <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = l + (r - l) // 2

            if self.canEatAll(piles, mid, h):
                r = mid
            else:
                l = mid + 1

        return l
