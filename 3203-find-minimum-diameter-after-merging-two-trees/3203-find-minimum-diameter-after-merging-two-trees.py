class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        # Date Solved: 23 May 2026, Saturday
        # Time: O(V+E), Space: O(V+E)
        # Refer: codestorywithMIK
        # Uses logic from LC 1245. Tree Diameter
        # Different than LC 543. Diameter of Binary Tree (Easy)
        adj1 = self.build_adj(edges1)
        adj2 = self.build_adj(edges2)

        d1 = self.find_diameter(adj1)
        d2 = self.find_diameter(adj2)

        combined = (d1 + 1) // 2 + (d2 + 1) // 2 + 1

        return max(d1, d2, combined)

    def build_adj(self, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def find_diameter(self, adj):
        farthest_node, _ = self.bfs(adj, 0)
        _, diameter = self.bfs(adj, farthest_node)
        return diameter

    def bfs(self, adj, source):
        queue = deque([source])
        visited = {source}

        distance = 0
        farthest_node = source

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                farthest_node = curr

                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            if queue:
                distance += 1

        return farthest_node, distance
