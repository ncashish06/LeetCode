class Solution:
    # Date Solved: 8 July 2026, Wednesday, POTD
    # Refer: codestorywithMIK
    # Approach: Pre Store all relevant data and use them
    # Time : O(n+q), n = len(s) and q = total queries
    # Space : O(n)
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        nonZeroCount = [0] * n  # non-zero digits count in s[0..i]
        numberUpTo = [0] * n  # number formed from non-zero digits in s[0..i]
        digitSumUpTo = [0] * n  # digit sum of s[0..i]
        pow10 = [0] * (n + 1)  # 10^i mod MOD

        pow10[0] = 1
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        nonZeroCount[0] = 1 if s[0] != "0" else 0
        numberUpTo[0] = int(s[0])
        digitSumUpTo[0] = int(s[0])

        for i in range(1, n):
            digit = int(s[i])
            nonZeroCount[i] = nonZeroCount[i - 1] + (1 if digit != 0 else 0)

        for i in range(1, n):
            digit = int(s[i])
            if digit != 0:
                numberUpTo[i] = (numberUpTo[i - 1] * 10 + digit) % MOD
            else:
                numberUpTo[i] = numberUpTo[i - 1]

        for i in range(1, n):
            digitSumUpTo[i] = digitSumUpTo[i - 1] + int(s[i])

        q = len(queries)
        result = [0] * q

        for i in range(q):
            l, r = queries[i][0], queries[i][1]

            startCount = 0 if l == 0 else nonZeroCount[l - 1]
            endCount = nonZeroCount[r]
            subStrLen = endCount - startCount

            if subStrLen == 0:
                result[i] = 0
                continue

            numBefore = 0 if l == 0 else numberUpTo[l - 1]
            # To prevent negatives, we use MOD like below as we are substracting here.
            x = (numberUpTo[r] - (numBefore * pow10[subStrLen] % MOD) + MOD) % MOD
            sum_x = digitSumUpTo[r] - (0 if l == 0 else digitSumUpTo[l - 1])
            result[i] = (x * sum_x) % MOD

        return result
