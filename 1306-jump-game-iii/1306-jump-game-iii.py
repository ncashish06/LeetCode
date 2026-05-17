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

            if curr - arr[curr] >= 0:
                queue.append(curr - arr[curr])  # Jump left

            if curr + arr[curr] < n:
                queue.append(curr + arr[curr])  # Jump right

            # Mark visited by negating
            arr[curr] = -arr[curr]

        return False
        """
        # Approach 2: DFS
        # Time : O(n), Space: O(n) — recursion stack space
        if start < 0 or start >= len(arr) or arr[start] < 0:
            return False

        if arr[start] == 0:
            return True

        # Mark visited by negating
        arr[start] = -arr[start]

        return self.canReach(arr, start - arr[start]) or self.canReach(arr, start + arr[start])
        """
