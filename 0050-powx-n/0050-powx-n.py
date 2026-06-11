class Solution:
    # Date Solved: 11 June 2026, Thursday
    # NC150
    # Refer: codestorywithMIK, binary or fast exponentiation
    # This code used in 11 June 2026 POTD, LC. 3558 Number of Ways to Assign Edge Weights I
    # Time: O(logn), Space: O(logn) for recursive stack
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if x == 0: # To eliminate unnecessary computation when n is large and x is 0
                return 0
            if n == 0:
                return 1
            half = power(x, n // 2)
            res = half * half
            if n % 2 == 1:
                res *= x
            return res

        if n < 0:
            x = 1 / x
            n = -n

        return power(x, n)
