class Solution:
    # Date Solved: 27 June 2026, Saturday, POTD
    # Refer: codestorywithMIK
    def maximumLength(self, nums: List[int]) -> int:
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1

        ones = cnt.get(1, 0)
        result = ones if ones % 2 == 1 else ones - 1

        for num in cnt:
            if num == 1:
                continue

            curr = num
            length = 0
            while cnt.get(curr, 0) > 1:
                length += 2
                curr = curr * curr

            length += 1 if curr in cnt else -1

            result = max(result, length)

        return result
