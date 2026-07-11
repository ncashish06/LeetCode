class Solution:
    # Date Solved: 11 July 2026, Saturday, POTD
    # In NC All
    # Refer: codestorywithMIK
    # Approach-1 (Using BFS)
    # Time : O(V+E), Space : O(V+E)
    def bfs(self, i, adj, visited, counts):
        que = deque([i])
        visited[i] = True

        while que:
            curr = que.popleft()
            counts[0] += 1  # v
            counts[1] += len(adj[curr])  # e

            for ngbr in adj[curr]:
                if not visited[ngbr]:
                    visited[ngbr] = True
                    que.append(ngbr)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        result = 0

        # Build the graph
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            counts = [0, 0]  # [v, e]
            self.bfs(i, adj, visited, counts)

            v, e = counts
            if v * (v - 1) == e:
                result += 1

        return result
