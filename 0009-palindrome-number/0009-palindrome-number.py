class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse = 0
        while (x>reverse):
            last_dig = x%10
            reverse = reverse*10 + last_dig
            x//=10
        return reverse == x or x==reverse//10
        