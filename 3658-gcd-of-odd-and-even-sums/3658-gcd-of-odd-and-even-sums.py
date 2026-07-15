from math import gcd


class Solution:
    # Date Solved: 15 July 2026, Wednesday, POTD
    # Refer: codestorywithMIK for the derivation of the formula
    def gcdOfOddEvenSums(self, n: int) -> int:
        """
        # Approach 1: Simple Maths
        # Time : O(log(n)), Space : O(1)
        sum_odd = n * n
        sum_even = n * (n + 1)
        return gcd(sum_odd, sum_even)
        """
        # Approach 2: Simple Maths and Constant Time
        # Time : O(1), Space : O(1)
        # sumOdd = n*n, sumEven = n*(n+1)
        # Since two consecutive integers are always coprime, gcd(n,n+1)=1
        # gcd(n*n, n*(n+1)) = n * gcd(n, n+1) = n * 1 = n
        return n
