class Solution:
    # Date Solved: 18 May 2026, Monday
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # m = len(nums1), n = len(nums2)
        """
        # Approach 1 (Set)
        # T.C: O(m+n), S.C: O(m)
        st = set(nums1)

        for num in nums2:
            if num in st:
                return num

        return -1

        # Approach 2: Binary search
        # T.C: O(m log n), S.C: O(1)
        def binarySearch(nums: List[int], target: int) -> bool:
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        for num in nums1:
            if binarySearch(nums2, num):
                return num
        return -1
        """
        # Approach 3: 2 pointers
        # T.C: O(m+n), S.C: O(1)
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return -1
