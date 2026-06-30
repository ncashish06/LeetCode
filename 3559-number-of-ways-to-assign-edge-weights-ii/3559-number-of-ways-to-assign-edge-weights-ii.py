import math


class Solution:
    # Date Solved: 12 June 2026, Friday, POTD
    # Refer: codestorywithMIK Binary Lifting (DP) playlist, 4th of 4 videos
    # Approach (Using Binary Lifting): Build an ancestor table via DFS + binary lifting and answer each LCA query by lifting nodes using binary bits.
    # Time : O(Nlog N + Qlog N)
    # Space : O(Nlog N)
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        cols = int(math.log2(n)) + 1

        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)

        depth = [0] * n
        ancestorTable = [[-1] * cols for _ in range(n)]

        # Iterative DFS to avoid recursion depth issues
        def dfs(root):
            stack = [(root, -1)]
            while stack:
                node, parent = stack.pop()
                ancestorTable[node][0] = parent
                for ngbr in adj[node]:
                    if ngbr == parent:
                        continue
                    depth[ngbr] = depth[node] + 1
                    stack.append((ngbr, node))

        dfs(0)

        # Build ancestor table (binary lifting)
        for j in range(1, cols):
            for node in range(n):
                if ancestorTable[node][j - 1] != -1:
                    ancestorTable[node][j] = ancestorTable[ancestorTable[node][j - 1]][
                        j - 1
                    ]

        def findLCA(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            k = depth[u] - depth[v]
            for j in range(cols):
                if k & (1 << j):
                    u = ancestorTable[u][j]

            if u == v:
                return u

            for j in range(cols - 1, -1, -1):
                if ancestorTable[u][j] == -1:
                    continue
                if ancestorTable[u][j] != ancestorTable[v][j]:
                    u = ancestorTable[u][j]
                    v = ancestorTable[v][j]

            return ancestorTable[u][0]

        # Precompute powers of 2
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (2 * pow2[i - 1]) % MOD

        result = []
        for u, v in queries:
            u -= 1
            v -= 1
            lca = findLCA(u, v)
            d = depth[u] + depth[v] - 2 * depth[lca]

            if d == 0:
                result.append(0)
            else:
                result.append(pow2[d - 1])

        return result
