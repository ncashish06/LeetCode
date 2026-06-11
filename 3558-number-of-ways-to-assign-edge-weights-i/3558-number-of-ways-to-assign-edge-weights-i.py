class Solution:
    MOD = 10**9 + 7

    # Date Solved: 11 June 2026, Thursday, POTD
    # Refer: codestorywithMIK
    # Python's pow method does the same binary or fast exponentiation
    # Approach: total_possibilities, 2^d = even_possibilites + odd_possibilites = 2*odd_possibilites
    # odd_possibilites = 2^(d-1)
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def getMaxDepth(node, parent):
            depth = 0
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                depth = max(depth, getMaxDepth(neighbor, node) + 1)
            return depth

        maxDepth = getMaxDepth(1, 0)
        return pow(2, maxDepth - 1, self.MOD)
