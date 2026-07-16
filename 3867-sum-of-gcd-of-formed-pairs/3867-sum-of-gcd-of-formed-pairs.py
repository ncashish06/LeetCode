class Solution:
    # Date Solved: 16 July 2026, Thursday
    # Refer: codestorywithMIK Post (no video as this is easy)
    # Time: O(nlogn + nlogM), M = max element.
    """
    Time complexity analysis:
    1. The loop for building prefix_gcd runs n times, and each math.gcd call costs O(log(min(a, b))), so this part is O(nlog M) where M is the max element value.
    2. Sorting prefix_gcd: O(n log n).
    3. The two-pointer pass: n/2 iterations, each with a gcd call, so O(n log M) again.
    Total: O(nlogn + nlogM). Since M (the max array value) and n are often comparable in magnitude, this is frequently just written as O(nlogn)
    """

    # Space: O(n)
    def gcdSum(self, nums: list[int]) -> int:
        # Just do what the question is asking. Simple Simulation
        n = len(nums)

        prefix_gcd = []
        max_el = -1
        for i in range(n):
            max_el = max(max_el, nums[i])
            prefix_gcd.append(math.gcd(nums[i], max_el))

        prefix_gcd.sort()

        result = 0
        i, j = 0, n - 1

        while i < j:
            result += math.gcd(prefix_gcd[i], prefix_gcd[j])
            i += 1
            j -= 1

        return result
