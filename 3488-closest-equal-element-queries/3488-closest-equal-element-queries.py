class Solution:
    # Date Solved: 15 April 2026, Wednesday
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        indices_map = {}
        # indices are appended in the sorted order
        for idx, num in enumerate(nums):
            if num not in indices_map:
                indices_map[num] = [idx]
            else:
                indices_map[num].append(idx)

        results = []

        for q_idx in queries:
            target_val = nums[q_idx]
            indices = indices_map[target_val]

            if len(indices) <= 1:
                results.append(-1)
                continue

            import bisect

            pos = bisect.bisect_left(indices, q_idx)

            min_dist = float("inf")

            # Element to the left (same circle or wrap-around)
            left_neighbor = indices[(pos - 1) % len(indices)]
            dist_left = abs(q_idx - left_neighbor)
            min_dist = min(min_dist, dist_left, n - dist_left)

            # Element to the right (same circle or wrap-around)
            right_neighbor = indices[(pos + 1) % len(indices)]
            dist_right = abs(q_idx - right_neighbor)
            min_dist = min(min_dist, dist_right, n - dist_right)

            results.append(min_dist)

        return results
