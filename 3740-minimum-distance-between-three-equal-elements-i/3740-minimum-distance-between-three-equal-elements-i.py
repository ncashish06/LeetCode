class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices_map = {}
        n = len(nums)
        for idx, val in enumerate(nums):
            if val not in indices_map:
                indices_map[val] = [idx]
            else:
                indices_map[val].append(idx)

        min_indices_length = float("inf")
        k_size = 3

        for val, indices in indices_map.items():
            indices_length = len(indices)
            if indices_length >= 3:
                for i in range(indices_length - k_size + 1):
                    current_dist = 2 * (indices[i + 2] - indices[i])
                    min_indices_length = min(min_indices_length, current_dist)
                
        return min_indices_length if min_indices_length != float('inf') else -1