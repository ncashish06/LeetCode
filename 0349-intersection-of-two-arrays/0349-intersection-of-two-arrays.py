class Solution:
    # Date Solved: 16 April 2026, Thursday
    # Refer: structy.net
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        items_set = set(nums1)

        for element in nums2:
            if element in items_set:
                result.append(element)
                items_set.remove(element)

        return result
