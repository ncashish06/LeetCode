class Solution:
    # Date Solved: 30 August 2026, Sunday, POTD
    # Refer: codestorywithMIK
    # Time: O(n), Space: O(1)
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minElIdx = 0
        maxElIdx = 0

        for i in range(1, n):
            if nums[i] < nums[minElIdx]:
                minElIdx = i
            if nums[i] > nums[maxElIdx]:
                maxElIdx = i

        if minElIdx < maxElIdx:  # minIdx is left index if minIdx is less than maxIdx
            left = minElIdx
            right = maxElIdx
        else:  # minIdx is right index if minIdx is greater than maxIdx
            left = maxElIdx
            right = minElIdx

        option1 = left + 1 + n - right  # remove from front, then back
        option2 = right + 1  # remove both from front
        option3 = n - left  # remove both from back

        ans = option1
        if option2 < ans:
            ans = option2
        if option3 < ans:
            ans = option3

        return ans
