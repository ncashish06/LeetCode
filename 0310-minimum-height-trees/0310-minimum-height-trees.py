class Solution:
    # Date Solved: 11 June 2026, Thursday
    # NC250
    # Refer: codestorywithMIK. This is a topological sort problem. Starting from leaf node and moving towards the center of the graph. We find the minimum height from the center of the graph.
    # Time: O(V+E), Space : O(V+E)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            indegree[u] += 1
            indegree[v] += 1
            adj[u].append(v)
            adj[v].append(u)

        # add leaf nodes and remove later
        leaves = []
        for i in range(n):
            if indegree[i] == 1:
                leaves.append(i)
        queue = deque(leaves)

        remaining = n
        while remaining > 2:
            size = len(queue)
            remaining -= size

            for _ in range(size):
                u = queue.popleft()
                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 1:
                        queue.append(v)

        return list(queue)
