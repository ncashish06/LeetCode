class Solution:
    # Date Solved: 3 August 2026, Monday
    # codestorywithMIK says it was asked recently in Phonepe OA
    # Refer: codestorywithMIK
    # In NC all but no video explanation
    # Time: O(m^2 * k) - m is the size of routes, and k is the maximum size of routes[i].
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        adj = defaultdict(list)

        for route in range(len(routes)):
            for stop in routes[route]:
                adj[stop].append(route)

        que = deque()
        visited = [False] * len(routes)

        for route in adj[source]:
            que.append(route)
            visited[route] = True

        busCount = 1
        while que:
            size = len(que)

            while size:
                size -= 1
                route = que.popleft()

                for stop in routes[route]:
                    if stop == target:
                        return busCount

                    for nextRoute in adj[stop]:
                        if not visited[nextRoute]:
                            visited[nextRoute] = True
                            que.append(nextRoute)

            busCount += 1

        return -1
