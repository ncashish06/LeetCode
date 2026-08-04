class Solution:
    # Date Solved: 4 August 2026, Tuesday, POTD
    # Refer: codestorywithMIK
    def findMissingElements(self, nums: List[int]) -> List[int]:
        """
        # Approach 1:
        # Time: O(nlogn + T), T = total number of elements between maxEl and minEl
        # Space: O(1) extra (excluding output)
        nums.sort()

        curr = nums[0]
        result = []

        i = 0
        while i < len(nums):
            if curr < nums[i]:  # missing curr
                result.append(curr)
            else:
                i += 1
            curr += 1

        return result
        """
        # Approach 2:
        # Time: O(n + T), T = total number of elements between maxEl and minEl
        # Space: O(1) extra (fixed-size presence array, since 1 <= nums[i] <= 100)
        present = [False] * 101  # as constraints: 1 <= nums[i] <= 100

        max_el = nums[0]
        min_el = nums[0]
        for num in nums:
            max_el = max(max_el, num)
            min_el = min(min_el, num)
            present[num] = True

        result = []
        for curr in range(min_el, max_el + 1):
            if not present[curr]:
                result.append(curr)

        return result
