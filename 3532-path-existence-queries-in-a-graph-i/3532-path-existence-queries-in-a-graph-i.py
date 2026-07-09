class Solution:
    # Date Solved: 9 July 2026, Thursday, POTD
    # Refer: codestorywithMIK. Union-find approach is overkill here.
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        """
        # Approach 1: BFS, but slow
        # Time: O((V+E) + q), Space: O(V+E)
        adj = collections.defaultdict(list)
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                adj[i].append(i + 1)
                adj[i + 1].append(i)

        component = [-1] * n
        compId = 0

        for i in range(n):
            if component[i] == -1:
                # BFS from node i
                component[i] = compId
                queue = deque([i])
                while queue:
                    cur = queue.popleft()
                    for ngbr in adj[cur]:
                        if component[ngbr] == -1:
                            component[ngbr] = compId
                            queue.append(ngbr)
                compId += 1

        return [component[u] == component[v] for u, v in queries]
        """
        # Approach 2: Simple observation - assign components
        # Time: O(n + q), Space: O(n)
        component = [0] * n
        compId = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                compId += 1
            component[i] = compId

        return [component[u] == component[v] for u, v in queries]
