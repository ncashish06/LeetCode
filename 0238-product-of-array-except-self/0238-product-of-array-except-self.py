class Solution:
    # Date Solved: 5 June 2026, Friday
    # Refer: codestorywithMIK
    # Blind 75
    """
    # Approach 1: Using Division: Time: O(n), Space: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product_without_zero = 1

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product_without_zero *= n

        result = []
        for n in nums:
            if n != 0:
                # If there's any zero in array, this element's result must be 0
                if zero_count > 0:
                    result.append(0)
                else:
                    result.append(product_without_zero // n)
            else:
                # More than one zero: even the zero position yields 0
                if zero_count > 1:
                    result.append(0)
                else:
                    result.append(product_without_zero)

        return result

    # Approach 2: Using Extra Space (prefix and suffix arrays)
    # Time: O(n), Space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n  # left[i]  = product of all elements to the left of i
        right = [1] * n  # right[i] = product of all elements to the right of i

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # result[i] = product of everything except nums[i]
        return [left[i] * right[i] for i in range(n)]
    """

    # Approach 3: Constant Space (prefix in result, suffix on the fly)
    # Time: O(n) | Space: O(1)  [output array doesn't count as extra space]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Forward pass: result[i] holds product of all elements to the left of i
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Backward pass: multiply in the suffix product on the fly
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
