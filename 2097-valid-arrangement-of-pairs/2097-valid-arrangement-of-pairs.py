class Solution:
    # Date Solved: 24 July 2026, Friday
    # codestorywithMIK says Asked recently for Uber Internship.
    # Refer: codestorywithMIK
    # Prerequisites: Go through Euler Path and Circuits (Part I-III) in Graph Concepts & Qns Playlist of codestorywithMIK
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Approach-1: DFS Using Stack - Hierholzer's Algorithm to find Euler Path
        # Time : O(V+E) for normal DFS, Space : O(V+E)
        adj = defaultdict(list)

        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for u, v in pairs:
            adj[u].append(v)  # u --> v
            outdegree[u] += 1
            indegree[v] += 1

        # Find the startNode of the Euler Path
        startNode = pairs[0][0]
        for node in adj:
            if outdegree[node] - indegree[node] == 1:
                startNode = node
                break

        # Simply do the Hierholzer DFS (iterative, using a stack)
        eulerPath = []
        stack = [startNode]

        while stack:
            curr = stack[-1]
            if adj[curr]:
                nxt = adj[curr].pop()
                stack.append(nxt)
            else: # no more neighbors left
                eulerPath.append(curr)
                stack.pop()

        # Build the result
        eulerPath.reverse()
        result = []
        for i in range(len(eulerPath) - 1):
            result.append([eulerPath[i], eulerPath[i + 1]])

        return result
