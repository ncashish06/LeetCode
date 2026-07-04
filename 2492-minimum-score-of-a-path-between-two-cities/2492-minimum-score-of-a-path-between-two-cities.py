from collections import deque, defaultdict


class Solution:
    # Date Solved: 4 July 2026, Saturday, POTD
    # Refer: codestorywithMIK or NeetCode All
    # Time: O(V+E), Space: O(V+E), Where V is the number of vertices and E is the number of edges.
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)

        for a, b, dist in roads:
            adj[a].append((b, dist))
            adj[b].append((a, dist))

        visited = [False] * (n + 1)
        result = float("inf")

        queue = deque([1])
        visited[1] = True

        while queue:
            u = queue.popleft()

            for v, c in adj[u]:
                result = min(result, c)

                if not visited[v]:
                    visited[v] = True
                    queue.append(v)

        return result
