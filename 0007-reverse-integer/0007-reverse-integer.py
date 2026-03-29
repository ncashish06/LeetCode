class Solution:
    def reverse(self, x: int) -> int:
        x_copy = x
        x = abs(x)
        rev = 0
        while(x>0):
            last = x%10
            rev=rev*10+last
            x=x//10

        limit = 2**31
        if rev < -limit or rev >limit:
            return 0

        return -rev if x_copy<0 else rev