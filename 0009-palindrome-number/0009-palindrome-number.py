class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        # Only reversing the back half of the number. Stop once 'reverted' equals or exceeds 'remaining'
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        # If length is even, x should equal revertedNumber (e.g., 12 | 21 -> 12 == 12)
        # If length is odd, we get rid of the middle digit via // 10 (e.g., 1 | 23 -> 1 == 2)
        return x == revertedNumber or x == revertedNumber // 10
        