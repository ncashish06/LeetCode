class Solution:
    # Date Solved: 27 May 2026, Wednesday
    # Refer: structy.net or Alvin The Programmer
    def isStrobogrammatic(self, num: str) -> bool:
        inverse_char = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        n = len(num)
        for i in range(n):
            front = num[i]
            back = num[n - i - 1]
            if back not in inverse_char or front != inverse_char[back]:
                return False
        return True
