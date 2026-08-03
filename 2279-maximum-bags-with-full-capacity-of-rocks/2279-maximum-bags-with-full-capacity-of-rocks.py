class Solution:
    # Date Solved: 3 August 2026, Monday
    # codestorywithMIK says it was asked recently in Infosys OA
    # Refer: codestorywithMIK
    # Time: O(nlogn)
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        count = 0
        vec = [0] * n

        for i in range(n):
            vec[i] = capacity[i] - rocks[i]

        vec.sort()

        for i in range(n):
            if additionalRocks >= vec[i]:
                additionalRocks -= vec[i]
                count += 1
            else:
                break

        return count
