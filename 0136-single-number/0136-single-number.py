class Solution:
    # Date Solved: 12 April 2026, Sunday
    def singleNumber(self, nums: List[int]) -> int:
        """
        Approach 1: Hashset
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)[0]
        """
        """
        Bitwise XOR
        a ^ a = 0 (a number XORed with itself cancels out)
        a ^ 0 = a (XOR with 0 keeps the number unchanged)
        XOR is commutative and associative, so order does not matter
        All numbers that appear twice will cancel each other out and the number that appears once will remain
        """
        res = 0
        for num in nums:
            res = num ^ res
        return res
