class Solution:
    # Date Solved: 9 April 2026, Thursday
    # Same solution for Problem 3741(Medium).
    def minimumDistance(self, nums: List[int]) -> int:
        indices_map = {}
        n = len(nums)
        for idx, num in enumerate(nums):
            if num not in indices_map:
                indices_map[num] = [idx]
            else:
                indices_map[num].append(idx)

        min_total_dist = float("inf")
        window_size = 3

        for num, indices in indices_map.items():
            if len(indices) < 3:
                continue

            for i in range(len(indices) - window_size + 1):  # Standard Sliding Window "Start-Point" Template
                first_idx = indices[i]
                third_idx = indices[i + 2]
                # In sorted triplet i<j<k, the distance is (j-i)+(k-j)+(k-i),simplifies to 2k-2i.
                current_dist = 2 * (third_idx - first_idx)
                min_total_dist = min(min_total_dist, current_dist)

        return min_total_dist if min_total_dist != float("inf") else -1
