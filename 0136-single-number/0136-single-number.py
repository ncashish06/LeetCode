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
        # Bitwise XOR
        res = 0
        for num in nums:
            res = num ^ res
        return res
        
