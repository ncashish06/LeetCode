class Solution:
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
