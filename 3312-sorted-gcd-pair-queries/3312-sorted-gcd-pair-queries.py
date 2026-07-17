class Solution:
    # Date Solved: 17 July 2026, Friday, POTD
    # Refer: Claude
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maxVal = max(nums)

        # cnt[x] = how many times x appears in nums
        cnt = [0] * (maxVal + 1)
        for x in nums:
            cnt[x] += 1

        # divCount[v] = how many numbers are divisible by v
        divCount = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            total = 0
            for multiple in range(v, maxVal + 1, v):
                total += cnt[multiple]
            divCount[v] = total

        # pairs[v] = pairs whose gcd is a multiple of v
        pairs = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            c = divCount[v]
            pairs[v] = c * (c - 1) // 2

        # gcdCount[v] = pairs whose gcd is EXACTLY v (peel off from the top)
        gcdCount = [0] * (maxVal + 2)
        for v in range(maxVal, 0, -1):
            total = pairs[v]
            k = 2 * v
            while k <= maxVal:
                total -= gcdCount[k]
                k += v
            gcdCount[v] = total

        # prefix[v] = number of pairs with gcd <= v
        prefix = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            prefix[v] += prefix[v - 1] + gcdCount[v]  # (fixed below)

        # (rewritten cleanly)
        prefix = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            prefix[v] = prefix[v - 1] + gcdCount[v]

        ans = []
        for q in queries:
            v = bisect.bisect_right(prefix, q)
            ans.append(v)
        return ans
