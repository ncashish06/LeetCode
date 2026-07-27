class Solution:
    # Date Solved: 27 July 2026, Monday, POTD
    # Time: O(n), Space: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        sec_largest = 0

        for num in nums:
            if num > largest:
                sec_largest = largest
                largest = num
            else:
                sec_largest = max(sec_largest, num)

        return (largest - 1) * (sec_largest - 1)
