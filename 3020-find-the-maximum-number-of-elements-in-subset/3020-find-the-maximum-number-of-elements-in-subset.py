from collections import Counter
import math


class Solution:
    # Date Solved: 27 June 2026, Saturday, POTD
    # Refer: Claude
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        one_cnt = cnt.pop(1, 0)
        ans = one_cnt if one_cnt % 2 else one_cnt - 1

        for num in cnt:
            sq = int(math.isqrt(num))
            if sq * sq == num and sq in cnt and cnt[sq] > 1:
                continue

            res = 0
            x = num
            while x in cnt and cnt[x] > 1:
                res += 2
                x *= x

            ans = max(ans, res + (1 if x in cnt else -1))

        return ans
