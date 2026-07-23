class Solution:
    # Date Solved: 23 July 2026, Thursday
    # codestorywithMIK says Asked Recently by Google in OA for Summer Internship, 2027.
    # In NC All. NC's video explanation not that clear as codestorywithMIK's.
    # Refer: codestorywithMIK
    """
    Rule of thumb:
    - If edge weights are uniform/identical (or restricted to {0,1}), a BFS variant suffices and is usually faster/simpler than Dijkstra.
    - If weights are arbitrary non-negative values, you need Dijkstra's greedy priority-queue approach BFS's FIFO order can't guarantee optimality there.
    """

    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        """
        # Approach 1: Modified Dijkstra
        # Time: O(E log V), Space: O(V + E)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        d1 = [float("inf")] * (n + 1)
        d2 = [float("inf")] * (n + 1)
        d1[1] = 0

        pq = [(0, 1)]  # (timePassed, node)

        while pq:
            time_passed, node = heapq.heappop(pq)

            # Second time popping n => that time is the second minimum
            if d2[n] != float("inf") and node == n:
                return d2[n]

            # If light is red when we arrive, wait until it turns green
            mult = time_passed // change
            if mult % 2 == 1:
                time_passed = change * (mult + 1)

            for nbr in adj[node]:
                new_time = time_passed + time
                if d1[nbr] > new_time:
                    d2[nbr] = d1[nbr]
                    d1[nbr] = new_time
                    heapq.heappush(pq, (new_time, nbr))
                elif d2[nbr] > new_time and d1[nbr] != new_time:
                    d2[nbr] = new_time
                    heapq.heappush(pq, (new_time, nbr))

        return -1
        """
        # Approach 2: BFS
        # Time: O(V + E), Space: O(V + E)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        d1 = [float("inf")] * (n + 1)
        d2 = [float("inf")] * (n + 1)
        d1[1] = 0

        queue = deque([(1, 1)])  # (node, freq) - freq 1 = first visit, 2 = second visit

        while queue:
            node, freq = queue.popleft()
            time_passed = d1[node] if freq == 1 else d2[node]

            # Second time reaching n => that time is the second minimum
            if d2[n] != float("inf") and node == n:
                return d2[n]

            # If light is red when we arrive, wait until it turns green
            mult = time_passed // change
            if mult % 2 == 1:
                time_passed = change * (mult + 1)

            for nbr in adj[node]:
                new_time = time_passed + time
                if d1[nbr] == float("inf"):
                    d1[nbr] = new_time
                    queue.append((nbr, 1))
                elif d2[nbr] == float("inf") and d1[nbr] != new_time:
                    d2[nbr] = new_time
                    queue.append((nbr, 2))

        return -1
