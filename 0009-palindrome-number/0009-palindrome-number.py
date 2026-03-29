class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse, original = 0, x
        while (x>0):
            last_dig = x%10
            reverse = reverse*10 + last_dig
            x//=10
        return reverse == original
        