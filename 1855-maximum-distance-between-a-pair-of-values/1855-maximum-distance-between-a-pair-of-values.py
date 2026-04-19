class Solution:
    # Date Solved: 18 April 2026, Saturday
    # 2 pointers approach, similar to LeetCode problem 88: Merge Sorted Arrays
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        max_dist = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1

        return max_dist
