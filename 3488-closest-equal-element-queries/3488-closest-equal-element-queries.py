class Solution:
    # Date Solved: 15 April 2026, Wednesday
    
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        # Time Complexity: O(n+mlogn)
        # Space Complexity: O(n)
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
        """
    # Time Complexity: O(n+m)
    # Space Complexity: O(n)
        n = len(nums)
        # These will store the index of the nearest identical element
        # found to the left and right, respectively.
        left_neighbor_idx = [0] * n
        right_neighbor_idx = [0] * n
        
        # pos keeps track of the most recent index seen for each value
        pos = {}

        # FORWARD PASS (Find nearest left neighbor)
        # We iterate from -n to n-1. 
        # The range [-n, -1] represents the "previous" rotation of the array.
        for i in range(-n, n):
            # If we are in the "actual" array indices [0, n-1]
            if i >= 0:
                # Look up the last time we saw this number. 
                # If never seen, we use -n as a placeholder.
                left_neighbor_idx[i] = pos.get(nums[i], -n)
            
            # Update the dictionary with the current index.
            # (i + n) % n ensures we map -n...n to the correct value in nums.
            pos[nums[(i + n) % n]] = i

        # Clear dictionary to reuse for the backward pass
        pos.clear()

        # --- BACKWARD PASS (Find nearest right neighbor) ---
        # We iterate from 2n-1 down to 0.
        # The range [2n-1, n] represents the "next" rotation of the array.
        for i in range(2 * n - 1, -1, -1):
            if i < n:
                # Look up the next time this number appears in the "future".
                # If never seen, we use 2n as a placeholder.
                right_neighbor_idx[i] = pos.get(nums[i], 2 * n)
            
            pos[nums[i % n]] = i

        # --- FINAL QUERY PROCESSING ---
        results = []
        for x in queries:
            # x is the index provided by the query.
            # The distance to the left neighbor is (x - index_of_left_neighbor).
            dist_l = x - left_neighbor_idx[x]
            # The distance to the right neighbor is (index_of_right_neighbor - x).
            dist_r = right_neighbor_idx[x] - x
            
            # In a circular array, if the only neighbor found is the element 
            # itself (one full rotation away), the distance will be exactly n.
            # The problem asks for "any OTHER index j", so n is invalid.
            if dist_l == n:
                results.append(-1)
            else:
                # The answer is the minimum of the two circular directions.
                results.append(min(dist_l, dist_r))

        return results