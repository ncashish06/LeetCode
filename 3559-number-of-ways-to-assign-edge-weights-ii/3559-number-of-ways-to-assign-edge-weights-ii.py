from collections import deque


class Solution:
    # Date Solved: 12 June 2026, Friday, POTD
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = max(1, (n).bit_length())
        depth = [0] * (n + 1)
        parent = [0] * (n + 1)
        visited = [False] * (n + 1)

        # BFS from root (node 1)
        q = deque([1])
        visited[1] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[v] = u
                    q.append(v)

        # Binary lifting table
        up = [[0] * (n + 1) for _ in range(LOG)]
        up[0] = parent[:]
        for k in range(1, LOG):
            for v in range(1, n + 1):
                up[k][v] = up[k - 1][up[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        # Precompute powers of 2
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD

        ans = []
        for u, v in queries:
            l = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[l]
            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow2[dist - 1])

        return ans
