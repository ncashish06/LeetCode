class Solution:
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
            m = len(indices)
            
            for i, actual_idx in enumerate(indices):
                # i is the count of elements to the left
                # m - i - 1 is the count of elements to the right
                
                # Formula derived from your image:
                # Left part: (i * actual_idx) - prefix_sum
                # Right part: (total_sum - prefix_sum - actual_idx) - ((m - i - 1) * actual_idx)
                
                left_side = (i * actual_idx) - prefix_sum
                right_side = (total_sum - prefix_sum - actual_idx) - ((m - i - 1) * actual_idx)
                
                res[actual_idx] = left_side + right_side
                
                # Update prefix_sum for the next element in this group
                prefix_sum += actual_idx
                
        return res