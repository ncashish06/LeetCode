from collections import defaultdict, deque


class Solution:
    # Date Solved: 17 May 2026, Sunday
    # Time: O(n), Space: O(n)
    # Minimum steps/jumps (Shortest Path) in Unweighted Graph = BFS
    # DFS fails here: memoization breaks when all 3 dependencies (left, right, teleport) exist simultaneously.
    # DFS explores in random order and caches the first result found, which may not be the shortest path.
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        # Indices map
        mp = defaultdict(list)
        for i in range(n):
            mp[arr[i]].append(i)

        visited = [False] * n
        visited[0] = True

        queue = deque([0])
        steps = 0

        while queue:
            # Process all nodes at current BFS level (same step count)
            size = len(queue)

            for _ in range(size):
                curr = queue.popleft()

                if curr == n - 1:
                    return steps

                # Left Jump
                left = curr - 1
                if left >= 0 and not visited[left]:
                    visited[left] = True
                    queue.append(left)

                # Right Jump
                right = curr + 1
                if right < n and not visited[right]:
                    visited[right] = True
                    queue.append(right)

                # Teleport to all same-value indices
                for idx in mp[arr[curr]]:
                    if not visited[idx]:
                        visited[idx] = True
                        queue.append(idx)

                # CRITICAL: Clear the bucket after processing
                # Without this, future nodes with the same value will re-scan this entire list -> O(n) redundant work per node which leads to TLE
                del mp[arr[curr]]

            steps += 1

        return -1
