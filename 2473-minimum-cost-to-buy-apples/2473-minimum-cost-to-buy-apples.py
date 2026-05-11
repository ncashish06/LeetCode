import heapq


class Solution:
    # Date Solved: 11 May 2026, Monday
    # Time: Per Dijkstra call: O((n + E) log n) where E = number of roads. Each node is popped from the heap once: O(n log n). Each edge is relaxed at most twice (bidirectional): O(E log n). We run Dijkstra n times (once per starting city), so total time: O(n × (n + E) log n)
    # Space: O(n + E) for adjacency list
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        # 1-indexed cities -> 0-indexed internally
        adj = [[] for _ in range(n)]
        for a, b, cost in roads:
            adj[a - 1].append((b - 1, cost))
            adj[b - 1].append((a - 1, cost))

        def dijkstra(src):
            # Returns shortest travel distances from src to all cities.
            dist = [float("inf")] * n
            dist[src] = 0
            heap = [(0, src)]
            while heap:
                d, u = heapq.heappop(heap)
                if d > dist[u]:
                    continue
                for v, w in adj[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(heap, (dist[v], v))
            return dist

        ans = []
        for i in range(n):
            dist = dijkstra(i)

            # Best option: go to city j (empty), buy apple, return (×k)
            # Total = (1+k)*dist[j] + appleCost[j]
            best = min(dist[j] + appleCost[j] + k * dist[j] for j in range(n))
            ans.append(best)

        return ans
