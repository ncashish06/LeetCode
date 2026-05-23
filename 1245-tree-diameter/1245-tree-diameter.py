from collections import defaultdict, deque


class Solution:
    # Date Solved: 23 May 2026, Saturday
    # Time: O(V+E), Space: O(V+E)
    # Refer: codestorywithMIK
    # Different than LC 543. Diameter of Binary Tree (Easy)
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        n = len(edges) + 1

        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # First BFS from node 0 to find the farthest node
        farthest_node, _ = self.find_farthest_node(n, adj, 0)

        # Second BFS from farthest node to find the diameter
        _, diameter = self.find_farthest_node(n, adj, farthest_node)

        return diameter

    def find_farthest_node(self, n, adj, source):
        queue = deque([source])
        visited = [False] * n
        visited[source] = True

        max_distance = 0
        farthest_node = source

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                farthest_node = curr  # last node processed at this level

                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            if queue:
                max_distance += 1

        return farthest_node, max_distance
