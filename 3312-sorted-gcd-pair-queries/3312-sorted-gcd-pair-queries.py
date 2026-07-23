class Solution:
    # Date Solved: 17 July 2026, Friday, POTD
    # Refer: NC Ashish for Approach 1: Brute force and codestorywithMIK for Approach 2
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        # Approach 1: Brute force. Just do what the question is asking. Simple Simulation
        # This will not work as given constraint is 10^5. You can't go O(n^2).
        # Time: O(n^2 log n)
        # Building all pairs: O(n^2) iterations, each computing math.gcd(a,b) costs O(log(min(a, b))) — so this part is O(n^2*log(min_num)) + O(n^2 log n) sort
        # Space: O(n^2) for gcd_pair list
        n = len(nums)
        gcd_pair = []
        result = []
        for i in range(n):
            for j in range(i + 1, n):
                gcd_pair.append(math.gcd(nums[i], nums[j]))

        gcd_pair.sort()
        for query in queries:
            result.append(gcd_pair[query])
        return result
        """
        # Approach 2:
        # By codestorywithMIK: Factorisation + Cumulative Sum + Binary Search
        # Time : O(n*sqrt(M) + M*log M + Q*log M), M = maxVal
        # Space : O(M), M = maxVal
        n = len(nums)
        maxVal = max(nums)

        # SECTION 1: Divisor frequency counting
        # Time : O(n * sqrt(maxVal)) — for each of n nums, we loop up to sqrt(num)
        # Space: O(maxVal) — the divisorFreq array
        divisorFreq = [0] * (maxVal + 1)
        for num in nums:
            j = 1
            while j * j <= num:
                if num % j == 0:
                    divisorFreq[j] += 1
                    if num // j != j:
                        divisorFreq[num // j] += 1
                j += 1

        # SECTION 2: Pairs-with-gcd via inclusion-exclusion
        # Time : O(maxVal * log(maxVal)) — outer loop is O(maxVal)
        # Space: O(maxVal) — the pairsWithGcd array
        pairsWithGcd = [0] * (maxVal + 1)
        for g in range(maxVal, 0, -1):
            count = divisorFreq[g]
            # nC2 number of pairs
            pairsWithGcd[g] = count * (count - 1) // 2

            # Correction time
            mult = 2 * g
            while mult <= maxVal:
                pairsWithGcd[g] -= pairsWithGcd[mult]
                mult += g

        prefixCountGcd = [0] * (maxVal + 1)
        for g in range(1, maxVal + 1):
            prefixCountGcd[g] = prefixCountGcd[g - 1] + pairsWithGcd[g]

        # SECTION 3: Answering queries via binary search
        # Time : O(Q * log(maxVal)) — Q queries, each binary search over range [1, maxVal]
        # Space: O(Q) — the result list (excluding output, this loop uses O(1) extra space)
        result = []
        for idx in queries:
            l, r = 1, maxVal
            temp = 1
            while l <= r:
                mid_gcd = l + (r - l) // 2
                if prefixCountGcd[mid_gcd] > idx:
                    temp = mid_gcd
                    r = mid_gcd - 1
                else:
                    l = mid_gcd + 1
            result.append(temp)

        return result
