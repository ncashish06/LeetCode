class Solution:
    # Date Solved: 22 April 2026, Wednesday
    # Prefix sum and Hash table
    # Same question as Leetcode 2121. Intervals Between Identical Elements
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        indices_map = {}
        for idx, val in enumerate(nums):
            if val not in indices_map:
                indices_map[val] = []
            indices_map[val].append(idx)

        for indices in indices_map.values():
            total_sum = sum(indices)
            prefix_sum = 0

            for i, actual_idx in enumerate(indices):
                # i is the count of elements to the left
                # len(indices) - i - 1 is the count of elements to the right

                left_side = (i * actual_idx) - prefix_sum
                right_side = (total_sum - prefix_sum - actual_idx) - (
                    (len(indices) - i - 1) * actual_idx
                )

                res[actual_idx] = left_side + right_side
                prefix_sum += actual_idx

        return res
