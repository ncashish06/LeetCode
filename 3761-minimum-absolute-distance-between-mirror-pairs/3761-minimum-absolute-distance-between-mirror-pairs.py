class Solution:
    # Date Solved: 16 April 2026, Thursday
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        min_dist = float("inf")

        def reverse(x):
            rev = 0
            while x:
                x, mod = divmod(x, 10)
                rev = rev * 10 + mod
            return rev

        for index, num in enumerate(nums):
            if num in seen:
                min_dist = min(min_dist, index - seen[num])
            reverse_num = reverse(num)
            # prev_map[int(str(num)[::-1])] = index
            seen[reverse_num] = index
        return -1 if min_dist == float("inf") else min_dist
