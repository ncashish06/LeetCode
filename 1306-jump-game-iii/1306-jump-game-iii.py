from collections import deque


class Solution:
    # Date Solved: 16 May 2026, Saturday
    # Refer: codestorywithMIK
    def canReach(self, arr: List[int], start: int) -> bool:
        # Approach 1: BFS
        # Time : O(n), Space: O(n) — queue space
        n = len(arr)
        queue = deque([start])

        while queue:
            curr = queue.popleft()

            if arr[curr] == 0:
                return True

            # Already visited (marked negative) -> skip
            if arr[curr] < 0:
                continue

            # Calculate both jump destinations
            right = curr + arr[curr]  # jump right
            left = curr - arr[curr]  # jump left

            # Enqueue valid in-bounds neighbors
            if 0 <= right < n:
                queue.append(right)
            if 0 <= left < n:
                queue.append(left)

            # Mark current index as visited by negating
            arr[curr] *= -1

        return False
        """
        # Approach 2: DFS
        # Time : O(n), Space: O(n) — recursion stack space
        n = len(arr)

        def dfs(i):
            # Out of bounds or already visited (marked negative)
            if i < 0 or i >= n or arr[i] < 0:
                return False

            if arr[i] == 0:
                return True

            # Save jump distance before negating
            jump = arr[i]

            # Mark visited by negating — prevents cycles
            arr[i] *= -1

            left = dfs(i - jump)
            right = dfs(i + jump)

            return left or right

        return dfs(start)
        """
