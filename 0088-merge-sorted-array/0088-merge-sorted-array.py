class Solution:
    # Date Solved: 10 April 2026, Friday
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1st approach with extra space
        nums1_copy = nums1[:m]
        pointer1, pointer2 = 0, 0
        for i in range(m + n):
            if pointer2 >= n or (
                pointer1 < m and nums1_copy[pointer1] < nums2[pointer2]
            ):
                nums1[i] = nums1_copy[pointer1]
                pointer1 += 1
            else:
                nums1[i] = nums2[pointer2]
                pointer2 += 1
