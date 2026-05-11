class Solution:
    # Date Solved: 10 May 2026, Sunday
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            str_num = str(nums[i])
            for char in str_num:
                res.append(int(char))
        return res
