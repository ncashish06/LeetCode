class Solution:
    # Date Solved: 8 June 2026, Monday, POTD
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        # Approach 1 - Using 3 extra lists
        # Time: O(n), Space: O(n)
        less, equal, greater = [], [], []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        less.extend(equal)
        less.extend(greater)
        return less
        # return less + equal + greater
        """
        # Approach 2 - Using index pointers
        # Time: O(n), Space: O(n) for output list
        count_less = sum(1 for num in nums if num < pivot)
        count_equal = sum(1 for num in nums if num == pivot)

        i = 0  # index for less than pivot
        j = count_less  # index for equal to pivot
        k = count_less + count_equal  # index for greater than pivot
        result = [0] * len(nums)

        for num in nums:
            if num < pivot:
                result[i] = num
                i += 1
            elif num == pivot:
                result[j] = num
                j += 1
            else:
                result[k] = num
                k += 1

        return result
