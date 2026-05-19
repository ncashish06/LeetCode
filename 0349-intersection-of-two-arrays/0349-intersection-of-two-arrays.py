class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Approach 1: structy.net
        Date: 16 April 2026, Thursday
        Time: O(n+m) but takes O(n) extra space
        """
        # result = []
        # items_set = set(nums1)

        # for element in nums2:
        #     if element in items_set:
        #         result.append(element)
        #         items_set.remove(element)

        # return result

        """
        Approach 2:
        Date: 19 May 2026, Monday 
        Refer: LC 2540. Minimum Common Value
        Time: O(nlogn + mlogm), Space: O(1) extra space assuming in-place sorting 
        (Python's Timsort uses O(n) auxiliary space internally)
        """
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        result = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                if not result or result[-1] != nums1[p1]:  # avoid duplicates
                    result.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return result
