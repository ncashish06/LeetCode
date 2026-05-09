class Solution:
    # Date Solved: 8 May 2026, Friday
    # Refer: NeetCode 250 solution
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Intuition: Rotating an array by k is equivalent to moving the last k elements to the front. 
        We can achieve this with three reversals. 
        First, reverse the entire array. 
        Now the last k elements are at the front, but in reverse order. 
        Reverse the first k elements to fix their order. 
        Finally, reverse the remaining elements to restore their original order.
        """
        n = len(nums)
        # When k is larger than the array length n, rotating by k is the same as rotating by k % n.
        k = k % n

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
