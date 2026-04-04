class Solution:
    # Date Solved: 3 April 2026, Friday
    def reverseString(self, s: List[str]) -> None:
        # 2 pointer approach (Swap first and last)
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        # Recursive way: in-place but not constant space (O(n) for the stack) as above
        """
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
        """
