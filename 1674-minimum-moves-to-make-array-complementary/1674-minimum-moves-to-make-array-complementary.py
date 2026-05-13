class Solution:
    # Date Solved: 12 May 2026, Tuesday
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        """
        # Approach 1: Brute force but easily understood: Time: O(limit x n)
        ans = float("inf")
        # Check every possible target sum from (1+1) up to (limit+limit)
        for t in range(2, 2 * limit + 1):
            moves = 0
            # For this target: check the cost of every pair (front and back)
            for i in range(n // 2):
                a = min(nums[i], nums[n - 1 - i])
                b = max(nums[i], nums[n - 1 - i])
                # RULE 1: pair already sums to target. Cost = 0 moves
                if a + b == t:
                    moves += 0
                # RULE 2: target reachable by changing just one number. Cost = 1 move
                # Lowest target reachable by changing b to 1: a + 1
                # Highest target reachable by changing a to limit: b + limit
                elif a + 1 <= t <= b + limit:
                    moves += 1
                # RULE 3: target too extreme, must change both numbers. Cost = 2 moves
                else:
                    moves += 2
            ans = min(ans, moves)
        return ans
        """
        # Approach 2: Instead of iterating over every possible t for every pair, you let each pair "announce" its cost transitions just once and the difference array accumulates all those announcements efficiently.
        # Time: O(limit + n)
        n = len(nums)

        # Size is 2*limit+2 because the "stop" marker for the last pair can land at index 2*limit+1 (when b=limit: b+limit+1 = 2*limit+1)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            # Start by assuming this pair always costs 2 moves for every T.
            # We'll carve out cheaper zones below using the difference array.
            diff[2] += 2

            # ZONE: 1 move (left side) — T in [a+1, a+b-1]
            # Changing just one element can reach these targets.
            # Mark the start of the discount at a+1.
            diff[a + 1] -= 1

            # ZONE: 0 moves — T == a+b exactly
            # The pair already sums to T. No change needed.
            # Drop cost by 1 more at a+b (now we're at 0).
            diff[a + b] -= 1

            # ZONE: 1 move (right side) — T in [a+b+1, b+limit]
            # We've gone past the perfect sum, cost rises back to 1.
            diff[a + b + 1] += 1

            # End of 1-move zone — T > b+limit needs 2 moves again.
            # Cost rises back to 2.
            diff[b + limit + 1] += 1

        # Sweep the difference array to find actual cost at each T.
        # Track the running total and find the minimum.
        ans = float("inf")
        current_cost = 0

        for t in range(2, 2 * limit + 1):
            current_cost += diff[t]
            ans = min(ans, current_cost)

        return ans
