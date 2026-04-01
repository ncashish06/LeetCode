class Solution:
    import heapq
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        # This is modified  Dijkstra's algorithm (Greedy)
        # Note that graph = [[]] * n won't work. You think you're making: [[], [], []], but this creates one list in memory and then creates three references (pointers) to that exact same list.
        adj_list = [[] for _ in range(n)]
        for u, v, travel_time in roads:
            adj_list[u].append([v, travel_time])
            adj_list[v].append([u, travel_time])

        # track the minimum time to reach each intersection
        min_time_to_reach = [float('inf')] * n
        ways_to_reach = [0] * n

        min_time_to_reach[0] = 0
        ways_to_reach[0] = 1

        pq = [[0, 0]]  # (weight, node)

        while pq:
            current_time, u = heapq.heappop(pq)

            # Skip if already have a shorter path
            if current_time > min_time_to_reach[u]:
                continue

            for neighbor, travel_time in adj_list[u]:
                new_time = current_time + travel_time

                if new_time < min_time_to_reach[neighbor]:
                    min_time_to_reach[neighbor] = new_time
                    ways_to_reach[neighbor] = ways_to_reach[u]
                    heapq.heappush(pq, [new_time, neighbor])

                # Found another path that ties the current minimum time
                elif new_time == min_time_to_reach[neighbor]:
                    ways_to_reach[neighbor] = (ways_to_reach[neighbor] + ways_to_reach[u]) % MOD
                    
        return ways_to_reach[n - 1]